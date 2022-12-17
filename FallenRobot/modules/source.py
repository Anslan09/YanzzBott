from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from pyrogram import __version__ as z
from telegram import __version__ as o
from telethon import __version__ as s
from platform import python_version as y

from FallenRobot import pbot, OWNER_ID, BOT_NAME, BOT_USERNAME, START_IMG


@pbot.on_message(filters.command(["repo", "beli", "sc"]))
async def repo(_, message: Message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""**ʜᴇʏ {message.from_user.mention},

ɪ ᴀᴍ [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ :** Euuon
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

Ingin deploy bot ini?
Klik button di bawah
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Daftar",
                        url="https://t.me/idnrobot",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Repo"
