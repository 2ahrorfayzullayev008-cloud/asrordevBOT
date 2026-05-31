from telegram import Update
from telegram.ext import ContextTypes
from data.content import TEXTS
from utils.keyboards import reviews_keyboard

async def reviews_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get('lang', 'uz')
    t = TEXTS.get(lang, TEXTS['uz'])

    await update.message.reply_text(
        text=t['reviews'],
        parse_mode="MarkdownV2",
        reply_markup=reviews_keyboard(lang)
    )
