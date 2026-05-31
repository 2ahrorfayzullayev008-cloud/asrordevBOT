from telegram import Update
from telegram.ext import ContextTypes
from data.content import TEXTS
from utils.keyboards import projects_keyboard

async def projects_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get('lang', 'uz')
    t = TEXTS.get(lang, TEXTS['uz'])

    await update.message.reply_text(
        text=t['projects'],
        parse_mode="MarkdownV2",
        reply_markup=projects_keyboard(lang)
    )
