from flask import Flask, request
from telegram import Bot, Update
import os

# التوكن الخاص بالبوت من Environment Variable
TOKEN = os.environ.get("TOKEN")
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
    # ضع هنا رابط Render الخاص بك
    bot.set_webhook(f"https://<your-render-app>.onrender.com/{TOKEN}")
    app.run(host="0.0.0.0", port=port)