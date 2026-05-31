from telegram import Update
from telegram.ext import ContextTypes
from data.content import TEXTS
from utils.keyboards import language_keyboard

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Determine greeting based on existing language or default to uz
    lang = context.user_data.get('lang', 'uz')
    greeting = TEXTS[lang]['greeting']
    
    await update.message.reply_text(
        text=greeting,
        parse_mode="Markdown",
        reply_markup=language_keyboard()
    )
