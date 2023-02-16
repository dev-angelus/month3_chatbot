from aiogram import types

from aiogram import types

async def on_user_joined(message: types.Message):
    await message.delete()

async def filter_messages(message: types.Message):
    if "Плохое слово" in message.text:
        await message.delete()

async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply('это команда должна быть ответом на сообщение!')
        return
    await message.bot.delete_message(chat_id=config.GROUP_ID, message.message_id)
    await message.bot.kick_chat_member(chat_id=config.GROUP_ID,user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply('Пользователь забанен!')



# async def is_admin(message:types.Message):
#     print(message.from_user)
#     author = message.from_user.id
#     admins = await message

#
# async def check_bad_words(message:types.Message):
#     bad_words = ("дурак","тупой")
#     if message.chat.type != 'private':
#         for word in bad_words:
#             if word in (message.text.lower(), replace(' ','')):
#                 await message.answer(f"{message.from_user.first_name}, не ругайся!")
#                 await message.delete()
#                 break
#
# async def pin_message(message: types.Message):
#     if message.chat.type != 'private':
#         print(message.reply_to_message)
#         if message.reply_to_message:
#             await message.reply_to_message.pin()

