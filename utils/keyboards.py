from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from data.content import TEXTS

def language_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data="lang_uz"),
            InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def default_reply_keyboard(lang='uz'):
    t = TEXTS.get(lang, TEXTS['uz'])
    keyboard = [
        [t['reply_main'], t['reply_about']],
        [t['reply_skills'], t['reply_contact']],
        [t['reply_reviews']]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, input_field_placeholder=t['reply_placeholder'])

def main_menu_keyboard(lang='uz'):
    t = TEXTS.get(lang, TEXTS['uz'])
    keyboard = [
        [
            InlineKeyboardButton(t['btn_about'], callback_data="about"),
            InlineKeyboardButton(t['btn_projects'], callback_data="projects")
        ],
        [
            InlineKeyboardButton(t['btn_skills'], callback_data="skills"),
            InlineKeyboardButton(t['btn_contact'], callback_data="contact")
        ],
        [
            InlineKeyboardButton(t['btn_reviews'], callback_data="reviews")
        ],
        [
            InlineKeyboardButton(t['btn_portfolio'], url="https://asrordeveloper.afayzullayev499.workers.dev")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def back_keyboard(lang='uz'):
    t = TEXTS.get(lang, TEXTS['uz'])
    keyboard = [
        [InlineKeyboardButton(t['btn_back'], callback_data="main")]
    ]
    return InlineKeyboardMarkup(keyboard)

def about_keyboard(lang='uz'):
    t = TEXTS.get(lang, TEXTS['uz'])
    keyboard = [
        [
            InlineKeyboardButton(t['btn_back'], callback_data="main"),
            InlineKeyboardButton(t['btn_contact'], callback_data="contact")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def projects_keyboard(lang='uz'):
    t = TEXTS.get(lang, TEXTS['uz'])
    keyboard = [
        [
            InlineKeyboardButton(t['btn_back'], callback_data="main"),
            InlineKeyboardButton(t['btn_portfolio'], url="https://asrordeveloper.afayzullayev499.workers.dev")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def skills_keyboard(lang='uz'):
    t = TEXTS.get(lang, TEXTS['uz'])
    keyboard = [
        [
            InlineKeyboardButton(t['btn_back'], callback_data="main"),
            InlineKeyboardButton(t['btn_projects'], callback_data="projects")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def contact_keyboard(lang='uz'):
    t = TEXTS.get(lang, TEXTS['uz'])
    keyboard = [
        [InlineKeyboardButton(t['btn_email'], url="https://mail.google.com/mail/?view=cm&fs=1&to=afyazullayev499@gmail.com")],
        [InlineKeyboardButton("💬 Telegram", url="https://t.me/asror_programmer")],
        [InlineKeyboardButton("💼 LinkedIn", url="https://www.linkedin.com/in/asror-dev")],
        [InlineKeyboardButton("🐙 GitHub", url="https://github.com/asror-coder1")],
        [InlineKeyboardButton(t['btn_back'], callback_data="main")]
    ]
    return InlineKeyboardMarkup(keyboard)

def reviews_keyboard(lang='uz'):
    t = TEXTS.get(lang, TEXTS['uz'])
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data="rate_1"),
            InlineKeyboardButton("2", callback_data="rate_2"),
            InlineKeyboardButton("3", callback_data="rate_3"),
            InlineKeyboardButton("4", callback_data="rate_4"),
            InlineKeyboardButton("5", callback_data="rate_5")
        ],
        [InlineKeyboardButton(t['btn_back'], callback_data="main")]
    ]
    return InlineKeyboardMarkup(keyboard)

def rating_done_keyboard(lang='uz'):
    t = TEXTS.get(lang, TEXTS['uz'])
    keyboard = [
        [InlineKeyboardButton(t['btn_back'], callback_data="main")]
    ]
    return InlineKeyboardMarkup(keyboard)
