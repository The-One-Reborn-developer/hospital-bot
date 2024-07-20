from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="О Больнице",
                                     callback_data="about")
            ],
            [
                InlineKeyboardButton(text="Режим работы",
                                     callback_data="work_time")
            ],
            [
                InlineKeyboardButton(text="Адрес и схема проезда",
                                     callback_data="driveway")
            ],
            [
                InlineKeyboardButton(text="Контакты",
                                     callback_data="contacts")
            ],
            [
                InlineKeyboardButton(text="Часто задаваемые вопросы",
                                     callback_data="faq")
            ],
        ]
    )


def back_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="main")
            ],
        ]
    )


def faq_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Правила госпитализации",
                                     callback_data="hospitalization_rules")
            ],
            [
                InlineKeyboardButton(text="Сроки госпитализации",
                                     callback_data="hospitalization_length")
            ],
            [
                InlineKeyboardButton(text="Правила записи на обследование",
                                     callback_data="register_rules")
            ],
            [
                InlineKeyboardButton(text="Как получить консультацию специалиста",
                                     callback_data="consultation_rules")
            ],
            [
                InlineKeyboardButton(text="Консультация травмотологов-ортопедов",
                                     callback_data="traumatology_consultation")
            ],
            [
                InlineKeyboardButton(text="О видах медицинской помощи",
                                     callback_data="about_med_help")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="main")
            ],
        ]
    )


def faq_back_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )