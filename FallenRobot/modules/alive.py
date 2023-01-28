import random

from pyrogram import __version__ as pyrover
from telegram import __version__ as telever
from telethon import Button
from telethon import __version__ as tlhver

from FallenRobot import OWNER_USERNAME, SUPPORT_CHAT, dispatcher
from FallenRobot import telethn as tbot
from FallenRobot.events import register

PHOTO = [
    "https://telegra.ph/file/4e145e0da2e5806146ab3.mp4",
    "https://telegra.ph//file/b5c9d15d1910aa8704e49.jpg",
    "https://telegra.ph//file/20f0125c1d2d6d4936066.mp4",
    "https://telegra.ph//file/87555787817294c04c5ae.jpg",
    "https://telegra.ph//file/839218d66895b355fee1f.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ {dispatcher.bot.first_name}**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [『𝗣𝗢𝗜𝗦𝗘𝗡』| ͢ ̶ͥ ̶ ̶ͣ ͓ ̶ͫ𝐃αиgєяουѕ𓄂⃝🔱𝐅ιgнτєя](https://t.me/{OWNER_USERNAME})** \n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", f"https://t.me/{dispatcher.bot.username}?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


__mod_name__ = "Aʟɪᴠᴇ"
