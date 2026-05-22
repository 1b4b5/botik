import asyncio
from aiogram import Bot, Dispatcher, types

bot = Bot("8808151894:AAG2XY7nrh22icY_k2pVHLxdsPFeSnQdUUk")
dp = Dispatcher()

CHANNEL_ID = -1003923008648 

# Связка: message_id сообщения в канале → user_id человека
links = {}

@dp.message()
async def handler(message: types.Message):

    # Если пишет человек (не канал)
    if message.chat.id != CHANNEL_ID:

        # Бот отправляет сообщение в твой канал
        sent = await bot.send_message(
            CHANNEL_ID,
            message.text
        )

        # Запоминаем: сообщение в канале → человек
        links[sent.message_id] = message.from_user.id

    # Если сообщение пришло из канала (ты отвечаешь)
    else:
        if message.reply_to_message:
            bot_msg_id = message.reply_to_message.message_id

            # Если бот знает, кому принадлежало сообщение
            if bot_msg_id in links:
                target = links[bot_msg_id]

                # Отправляем ответ человеку
                await bot.send_message(target, message.text)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())