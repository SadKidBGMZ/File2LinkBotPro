from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start', 'help']))
async def start_handler(_, m: Message):
    await m.reply_photo("https://telegra.ph/file/e2021d883907638b3d7fa.jpg",
    caption="**Hᴇʏ! 😚\n\nI Aᴍ Fɪʟᴇ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴇʀ Bᴏᴛ 🤖\n\nI Cᴀɴ Sᴛʀᴇᴀᴍ Yᴏᴜʀ Vɪᴅᴇᴏ Tᴏ! ⏯️\n\nSᴇɴᴅ Aɴʏ Fɪʟᴇ Tᴏ Gᴇᴛ Lɪɴᴋ 🔗**",
                                 reply_markup=InlineKeyboardMarkup([
                                     [InlineKeyboardButton("🍿 Join Our Channel 🍿", url="https://t.me/iPopcornMovie")],
                                     [InlineKeyboardButton("💬 Add Me To Your Groups 💬", url="http://t.me/iPopcornMovieSearchBot?startgroup=botstart")]
                                 ]))
