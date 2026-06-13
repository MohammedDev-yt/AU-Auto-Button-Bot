# ------------------------- #
# Don't Remove Credit
# Owner @Mr_Mohammed_29
# ------------------------- #

from config import LOG_CHANNEL


async def send_log(client, text):

    try:

        await client.send_message(
            chat_id=LOG_CHANNEL,
            text=f"""
📌 <b>BOT LOG</b>

{text}
""",
            parse_mode="html"
        )

    except Exception as e:

        print(
            f"LOG ERROR: {e}"
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
