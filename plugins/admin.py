
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import Client, filters

from config import OWNER_ID
from database import (
    add_admin,
    remove_admin,
    get_admins
)

# ------------------------- #
# OWNER CHECK
# ------------------------- #

def owner(_, __, msg):

    return (
        msg.from_user
        and msg.from_user.id == OWNER_ID
    )


owner_filter = filters.create(owner)

# ------------------------- #
# ADD ADMIN
# ------------------------- #

@Client.on_message(
    filters.command("addadmin") & owner_filter
)
async def add_admin_cmd(client, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "Usᴀɢᴇ:\n/addadmin USER_ID"
        )

    uid = int(message.command[1])

    await add_admin(uid)

    # 🔔 NOTIFY USER
    try:
        await client.send_message(
            uid,
            "🎊 Cᴏɴɢʀᴀᴛs, Yᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴘʀᴏᴍᴏᴛᴇᴅ ᴛᴏ Aᴅᴍɪɴ!\ɴ\ɴYᴏᴜ ᴄᴀɴ ɴᴏᴡ ᴜsᴇ ᴀᴅᴍɪɴ ғᴇᴀᴛᴜʀᴇs ᴏғ ᴛʜᴇ ʙᴏᴛ."
        )
    except:
        pass

    await message.reply_text(
        f"✅ Admin Added\n{uid}"
    )

# ------------------------- #
# REMOVE ADMIN
# ------------------------- #

@Client.on_message(
    filters.command("removeadmin") & owner_filter
)
async def remove_admin_cmd(client, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/removeadmin USER_ID"
        )

    uid = int(message.command[1])

    await remove_admin(uid)

    # 🔔 NOTIFY USER
    try:
        await client.send_message(
            uid,
            "⚠️ You have been removed from Admin role."
        )
    except:
        pass

    await message.reply_text(
        f"✅ Admin Removed\n{uid}"
    )

# ------------------------- #
# LIST ADMINS
# ------------------------- #

@Client.on_message(
    filters.command("admins") & owner_filter
)
async def admins_cmd(client, message):

    admins = await get_admins()

    if not admins:
        return await message.reply_text("No admins")

    text = "👮 Admins List\n\n"

    for uid in admins:

        try:
            user = await client.get_users(uid)

            name = user.first_name or "No Name"
            username = f"@{user.username}" if user.username else "No Username"

            text += f"• {name} ({username}) - `{uid}`\n"

        except:
            text += f"• Unknown - `{uid}`\n"

    await message.reply_text(text)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
