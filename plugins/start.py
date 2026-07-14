# ------------------------- #
# Don't Remove Credit
# Owner @Mr_Mohammed_29
# ------------------------- #

import asyncio

from pyrogram import Client, filters, enums
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from database import add_user
from config import (
    START_TEXT,
    ABOUT_TEXT
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #


START_IMAGE = "https://graph.org/file/8cc7c4d5f0989b8efad96-f5d88bacd8e8049c9b.jpg"


# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def buttons():

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "• Uᴘᴅᴀᴛᴇs •",
                    url="https://t.me/Aero_Unity"
                ),
                InlineKeyboardButton(
                    "• Oᴡɴᴇʀ •",
                    url="https://t.me/Mr_Mohammed_29"
                )
            ],
            [
                InlineKeyboardButton(
                    "• Aʙᴏᴜᴛ •",
                    callback_data="about"
                )
            ]
        ]
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(
    filters.command("start")
    & filters.private
)
async def start(client, message):

    await add_user(
        message.from_user.id
    )


    m = await message.reply_text(
        "Dᴇᴍᴏɴ Kɪɴɢ..."
    )


    for text in [
        "⚡️",
        "😈",
        "Rɪᴍᴜʀᴜ...",
        "Tᴇᴍᴘᴇsᴛ!"
    ]:

        await asyncio.sleep(0.5)
        await m.edit_text(text)


    await m.delete()


    await message.reply_sticker(
        "CAACAgUAAxkBAAEXmw5plIsM5lyaJfj5NwNp13QSrbW9NQACnBsAAlztqVYRMk2x1suA_B4E"
    )


    await client.send_photo(
        chat_id=message.chat.id,
        photo=START_IMAGE,
        caption=START_TEXT.format(
            mention=message.from_user.mention
        ),
        parse_mode=enums.ParseMode.HTML,
        reply_markup=buttons()
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_callback_query(
    filters.regex("about")
)
async def about(client, query):

    about_buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "• Hᴏᴍᴇ •",
                    callback_data="home"
                )
            ]
        ]
    )


    await query.message.delete()


    await client.send_photo(
        chat_id=query.message.chat.id,
        photo=START_IMAGE,
        caption=ABOUT_TEXT,
        parse_mode=enums.ParseMode.HTML,
        reply_markup=about_buttons
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_callback_query(
    filters.regex("home")
)
async def home(client, query):

    await query.message.delete()


    await client.send_photo(
        chat_id=query.message.chat.id,
        photo=START_IMAGE,
        caption=START_TEXT.format(
            mention=query.from_user.mention
        ),
        parse_mode=enums.ParseMode.HTML,
        reply_markup=buttons()
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
