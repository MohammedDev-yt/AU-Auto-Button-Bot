# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import Client, filters


@Client.on_message(
    filters.command("id")
)
async def id(_, message):

    await message.reply_text(
        f"Chat ID: `{message.chat.id}`"
    )
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #


