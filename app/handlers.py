from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def echo(message: Message):
    answer = 'Приветствую! Я чат-бот Белгородской областной клинической ' \
             'больницы Святителя Иоасафа. ' \
             'Если у вас возникли вопросы, вы можете задать их мне.'
    
    await message.answer(answer, reply_markup=kb.main_keyboard())


@router.callback_query(F.data == "about")
async def about(callback: CallbackQuery):
    with open('app/info/about.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.back_keyboard())


@router.callback_query(F.data == "main")
async def main(callback: CallbackQuery):
    answer = 'Приветствую! Я — чат-бот Белгородской областной клинической ' \
             'больницы Святителя Иоасафа. ' \
             'Если у Вас возникли вопросы, вы можете задать их мне.'
    
    await callback.message.edit_text(answer, reply_markup=kb.main_keyboard())


@router.callback_query(F.data == "work_time")
async def work_time(callback: CallbackQuery):
    with open('app/info/work_time.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.back_keyboard())


@router.callback_query(F.data == "contacts")
async def contacts(callback: CallbackQuery):
    with open('app/info/contacts.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.back_keyboard())