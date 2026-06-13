# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import Client, filters

from config import OWNER_ID
from database import count_users

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def owner(_, __, msg):

    return (
        msg.from_user
        and msg.from_user.id == OWNER_ID
    )


owner_filter = filters.create(owner)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(
    filters.command("stats")
    & owner_filter
)
async def stats(
    client,
    message
):

    users = await count_users()


    await message.reply_text(
        f"""
📊 Bot Stats

👤 Users: {users}
"""
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
