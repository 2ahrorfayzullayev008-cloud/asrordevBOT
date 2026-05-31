from telegram import Update
from telegram.ext import ContextTypes
from data.content import TEXTS
from utils.keyboards import skills_keyboard

async def skills_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get('lang', 'uz')
    t = TEXTS.get(lang, TEXTS['uz'])

    await update.message.reply_text(
        text=t['skills'],
        parse_mode="MarkdownV2",
        reply_markup=skills_keyboard(lang)
    )
