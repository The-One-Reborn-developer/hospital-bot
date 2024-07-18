from aiogram import Router


router = Router()


@router.message()
async def echo(message):
    await message.reply(message.text)