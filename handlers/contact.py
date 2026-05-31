from telegram import Update
from telegram.ext import ContextTypes
from data.content import TEXTS
from utils.keyboards import contact_keyboard

async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get('lang', 'uz')
    t = TEXTS.get(lang, TEXTS['uz'])

    await update.message.reply_text(
        text=t['contact'],
        parse_mode="MarkdownV2",
        reply_markup=contact_keyboard(lang)
    )
