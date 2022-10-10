#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [MediaToTelegraphLink bot by TeLe TiPs] (https://github.com/teletips/MediaToTelegraphLink-TeLeTiPs)

from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file
import os

teletips=Client(
    "MediaToTelegraphLink",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

@teletips.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f"""
اهلا {message.from_user.mention},
🔮أنا هنا لإنشاء روابط التلجراف لملفات الوسائط الخاصة بك.

👨🏼‍💻ما عليك سوى إرسال ملف وسائط صالح مباشرة إلى هذه الدردشة.
♻️انواع الملفات الصالحه هي:- 'jpeg', 'jpg', 'png', 'mp4' and 'gif'.

🌐لأنشاء الروابط في **المجموعات**,اضفني لمجموعه خارقه اي عامه وارسل الامر <code>/tl</code> ردا علي ملف وسائط صالح.
🖥 | [𝑺𝑶𝑼𝑹𝑪𝑬 𝑽𝑨𝑴𝑩𝑰𝑹🌀](https://t.me/XxvprxX)

☣️ | [ᯓ˹ 𝐕𝘼𝙈𝘽𝙄𝙍𖣥⃟⃟⃟⃟⃟🇵🇸فمـبــيرـ͢）⛧](https://t.me/XxlllllllllllllllllllllllllllxX)
            """
    await teletips.send_message(message.chat.id, text, disable_web_page_preview=True)
    

@teletips.on_message(filters.media & filters.private)
async def get_link_private(client, message):
    try:
        text = await message.reply("🔮انتظر قليلا...")
        async def progress(current, total):
            await text.edit_text(f"📥 جاري التنزيل... {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            local_path = await message.download(location, progress=progress)
            await text.edit_text("📤 جاري الرفع الي التليجراف...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | رابط التليجراف**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | فشل رفع الملف**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return                 
    except Exception:
        pass        

@teletips.on_message(filters.command('tl'))
async def get_link_group(client, message):
    try:
        text = await message.reply("🔮انتظر قليلا...")
        async def progress(current, total):
            await text.edit_text(f"📥 جاري التنزيل... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("📤 جاري الرفع الي التليجراف...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | رابط التليجراف**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | فشل رفع الملف**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass                                           

print("Bot is alive!")
teletips.run()

#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
