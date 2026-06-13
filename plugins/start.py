# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from database import add_user
from config import (
    START_TEXT,
    ABOUT_TEXT,
    OWNER_TEXT
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(
    filters.command("start")
    & filters.private
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def start(_, message):

    await add_user(
        message.from_user.id
    )

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📢 Updates",
                    url="https://t.me/Anime_UpdatesAU"
                )
            ],
            [
                InlineKeyboardButton(
                    "👤 Owner",
                    url="https://t.me/Mr_Mohammed_29"
                )
            ],
            [
                InlineKeyboardButton(
                    "ℹ️ About",
                    callback_data="about"
                )
            ]
        ]
    )

    await message.reply_text(
        START_TEXT,
        reply_markup=buttons
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_callback_query(
    filters.regex("about")
)
async def about(_, query):

    await query.message.edit_text(
        ABOUT_TEXT
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
