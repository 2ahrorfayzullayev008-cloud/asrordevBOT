from telegram import Update
from telegram.ext import ContextTypes
from data.content import TEXTS
from utils.keyboards import about_keyboard

async def about_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get('lang', 'uz')
    t = TEXTS.get(lang, TEXTS['uz'])
    
    await update.message.reply_text(
        text=t['about'],
        parse_mode="MarkdownV2",
        reply_markup=about_keyboard(lang)
    )
