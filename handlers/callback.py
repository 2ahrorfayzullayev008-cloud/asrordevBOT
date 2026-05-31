import logging
import os
from telegram import Update
from telegram.ext import ContextTypes
from data.content import TEXTS
from utils.keyboards import (
    main_menu_keyboard, about_keyboard, projects_keyboard,
    skills_keyboard, contact_keyboard, reviews_keyboard,
    rating_done_keyboard, default_reply_keyboard
)

logger = logging.getLogger(__name__)

async def safe_edit(query, context, text, reply_markup):
    if query.message.photo:
        await query.message.delete()
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text=text,
            parse_mode="MarkdownV2",
            reply_markup=reply_markup
        )
    else:
        await query.edit_message_text(
            text=text,
            parse_mode="MarkdownV2",
            reply_markup=reply_markup
        )

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    try:
        # Handle language selection
        if data in ['lang_uz', 'lang_ru', 'lang_en']:
            lang = data.split('_')[1]
            context.user_data['lang'] = lang
            t = TEXTS[lang]
            
            await context.bot.send_message(
                chat_id=query.message.chat_id,
                text=t['lang_selected'],
                reply_markup=default_reply_keyboard(lang)
            )
            await query.message.delete()
            return

        lang = context.user_data.get('lang', 'uz')
        t = TEXTS.get(lang, TEXTS['uz'])

        if data == "main":
            await safe_edit(query, context, t['welcome'], main_menu_keyboard(lang))
            
        elif data == "about":
            photo_path = 'data/profile.jpg'
            if os.path.exists(photo_path):
                await query.message.delete()
                with open(photo_path, 'rb') as photo:
                    await context.bot.send_photo(
                        chat_id=query.message.chat_id,
                        photo=photo,
                        caption=t['about'],
                        parse_mode="MarkdownV2",
                        reply_markup=about_keyboard(lang)
                    )
            else:
                await safe_edit(query, context, t['about'], about_keyboard(lang))
                
        elif data == "projects":
            await safe_edit(query, context, t['projects'], projects_keyboard(lang))
            
        elif data == "skills":
            await safe_edit(query, context, t['skills'], skills_keyboard(lang))
            
        elif data == "contact":
            await safe_edit(query, context, t['contact'], contact_keyboard(lang))
            
        elif data == "reviews":
            await safe_edit(query, context, t['reviews'], reviews_keyboard(lang))
            
        elif data.startswith("rate_"):
            number = int(data.split("_")[1])
            rating_text = t['rating_texts'].get(number, "Rahmat\\!")
            
            await safe_edit(query, context, rating_text, rating_done_keyboard(lang))
            
            owner_chat_id = os.getenv("OWNER_CHAT_ID")
            if owner_chat_id:
                username = query.from_user.username or query.from_user.first_name
                notification_text = f"⭐ Yangi baho: {number}/5\nFoydalanuvchi: @{username}"
                await context.bot.send_message(
                    chat_id=owner_chat_id,
                    text=notification_text
                )

    except Exception as e:
        logger.error(f"Error in callback_handler: {e}")
