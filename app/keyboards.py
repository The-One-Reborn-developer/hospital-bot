from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="О Больнице", callback_data="about"),
                InlineKeyboardButton(text="Режим работы", callback_data="work_time"),
            ],
            [
                InlineKeyboardButton(text="Схема проезда", callback_data="map"),
                InlineKeyboardButton(text="Контакты", callback_data="contacts"),
            ],
            [
                InlineKeyboardButton(text="Часто задаваемые вопросы", callback_data="faq"),
            ],
        ]
    )


def about_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Назад", callback_data="main"),
            ],
        ]
    )