import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters

from handlers.start import start_handler
from handlers.about import about_handler
from handlers.projects import projects_handler
from handlers.skills import skills_handler
from handlers.contact import contact_handler
from handlers.reviews import reviews_handler
from handlers.callback import callback_handler
from data.content import TEXTS
from utils.keyboards import main_menu_keyboard, about_keyboard, contact_keyboard, skills_keyboard, reviews_keyboard

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def text_handler(update: Update, context):
    text = update.message.text
    lang = context.user_data.get('lang', 'uz')
    t = TEXTS.get(lang, TEXTS['uz'])

    if text == t['reply_main']:
        await update.message.reply_text(
            text=t['welcome'],
            parse_mode="MarkdownV2",
            reply_markup=main_menu_keyboard(lang)
        )
    elif text == t['reply_about']:
        photo_path = 'data/profile.jpg'
        if os.path.exists(photo_path):
            with open(photo_path, 'rb') as photo:
                await update.message.reply_photo(
                    photo=photo,
                    caption=t['about'],
                    parse_mode="MarkdownV2",
                    reply_markup=about_keyboard(lang)
                )
        else:
            await update.message.reply_text(
                text=t['about'],
                parse_mode="MarkdownV2",
                reply_markup=about_keyboard(lang)
            )
    elif text == t['reply_contact']:
        await update.message.reply_text(
            text=t['contact'],
            parse_mode="MarkdownV2",
            reply_markup=contact_keyboard(lang)
        )
    elif text == t['reply_skills']:
        await update.message.reply_text(
            text=t['skills'],
            parse_mode="MarkdownV2",
            reply_markup=skills_keyboard(lang)
        )
    elif text == t['reply_reviews']:
        await update.message.reply_text(
            text=t['reviews'],
            parse_mode="MarkdownV2",
            reply_markup=reviews_keyboard(lang)
        )
    else:
        await update.message.reply_text(
            text=t['unknown'],
            parse_mode="MarkdownV2",
            reply_markup=main_menu_keyboard(lang)
        )

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN is not set in .env")
        return

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("about", about_handler))
    application.add_handler(CommandHandler("projects", projects_handler))
    application.add_handler(CommandHandler("skills", skills_handler))
    application.add_handler(CommandHandler("contact", contact_handler))
    application.add_handler(CommandHandler("reviews", reviews_handler))
    application.add_handler(CallbackQueryHandler(callback_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
