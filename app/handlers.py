from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def echo(message: Message):
    answer = 'Приветствую! Я чат-бот Белгородской областной клинической больницы Святителя Иоасафа. ' \
             'Если у вас возникли вопросы, вы можете задать их мне.'
    
    await message.answer(answer, reply_markup=kb.main_keyboard())


@router.callback_query(F.data == "about")
async def about(callback: CallbackQuery):
    answer = 'ОГБУЗ «Белгородская областная клиническая больница Святителя Иоасафа» -  это крупнейшее ' \
             'многопрофильное учреждение Белгородской области, стабильно занимающее позицию лидера среди ' \
             'медицинских организаций, участвующих в оказании специализированной и высокотехнологичной ' \
             'медицинской помощи.'\
             '\nМы гордимся нашей историей,  сохраняем накопленный опыт и непрерывно развиваемся, используя ' \
             'мировую практику во всех областях диагностики, лечения и реабилитации.' \
             '\nВ составе учреждения 55 специализированных  отделений, консультативно-диагностический центр, ' \
             'консультативная поликлиника, центр медицинской реабилитации, что позволяет оказывать полный спектр ' \
             'медицинских услуг – от  консультации  врача до высокотехнологичной диагностики, сложных ' \
             'хирургических вмешательств и реабилитации.' \
             '\nУ нас работают только высококвалифицированные специалисты, кандидаты и доктора медицинских ' \
             'наук.  Профессионализм  сотрудников и высокий потенциал технического оснащения позволяют оказывать ' \
             'медицинскую помощь,  отвечающую современным требованиям.' \
             '\nМы ориентированы на пациента, мультидисциплинарный подход осуществляется путем совместной ' \
             'работы врачей разных специальностей и эффективной маршрутизации на всех этапах оказания ' \
             'медицинской помощи.' \
             '\nНаша деятельность выстроена на принципах качества и безопасности.  Сертификат «Качество и ' \
             'безопасность медицинской деятельности» - это результат командной работы и высокая оценка ' \
             'труда всего коллектива.'
    
    await callback.message.edit_text(answer, reply_markup=kb.back_keyboard())


@router.callback_query(F.data == "main")
async def main(callback: CallbackQuery):
    answer = 'Приветствую! Я чат-бот Белгородской областной клинической больницы Святителя Иоасафа. ' \
             'Если у вас возникли вопросы, вы можете задать их мне.'
    
    await callback.message.edit_text(answer, reply_markup=kb.main_keyboard())


@router.callback_query(F.data == "work_time")
async def work_time(callback: CallbackQuery):
    answer = 'Поликлиника: с 08:00 до 15:30 (выходные: суббота, воскресенье).\n' \
             'Дневной стационар: с 09:00 до 18:00, без выходных.\n' \
             'Стационар: круглосуточно.\n' \
             'Консультативно-диагностическое отделение перинатального центра: с 08:00 до 18:00 (выходные: суббота, воскресенье).\n' \
             'Центр медицинской реабилитации: с 08:00 до 20:00 (выходные: суббота, воскресенье).'
    
    await callback.message.edit_text(answer, reply_markup=kb.back_keyboard())


