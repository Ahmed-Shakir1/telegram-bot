from flask import Flask, request
from telegram import Bot, Update
import os

# ضع التوكن هنا أو استخدم Environment Variable لاحقًا
TOKEN = "8667305239:AAHgNJg8TMDmR1ZGH7pZ0i8645M6Cbq4PSE"
bot = Bot(TOKEN)

app = Flask(__name__)

# صفحة اختبارية للتأكد من أن البوت يعمل
@app.route("/", methods=["GET"])
def home():
    return "Bot is alive!"

# Webhook لتلقي الرسائل
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)
    if update.message and update.message.text == "/start":
        chat_id = update.message.chat.id
        bot.send_message(chat_id, "أهلاً بك! البوت يعمل الآن 🚀")
    return {"ok": True}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    bot.set_webhook(f"https://telegram-bot-qwn8.onrender.com/{TOKEN}")
    app.run(host="0.0.0.0", port=port)