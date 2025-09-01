import os
from flask import Flask, request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup

# --- 配置 ---
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_NOT_FOUND")
WEB_APP_URL = "https://dewee-dev.github.io/HK_Dec/index.html"
WEBHOOK_PATH = "/webhook"
PORT = int(os.environ.get("PORT", 10000))  # Render 会自动分配端口

# --- Flask 应用 ---
app = Flask(__name__)
bot = Bot(token=BOT_TOKEN)

# --- Webhook 路由 ---
@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    if update.message and update.message.text == "/start":
        keyboard = [
            [InlineKeyboardButton("🔐 打开加解密工具", web_app={"url": WEB_APP_URL})]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(
            chat_id=update.message.chat_id,
            text=(
                "👋 欢迎使用 *HK 加解密工具*！\n\n"
                "这是一个专为小程序代码加密/解密设计的在线工具。\n"
                "点击下方按钮即可打开网页，无需安装，无需注册。\n\n"
                "🧪 快速、安全、开箱即用！"
            ),
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    return "ok"

# --- 启动 Flask 服务并设置 Webhook ---
if __name__ == "__main__":
    bot.set_webhook(url=f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}{WEBHOOK_PATH}")
    app.run(host="0.0.0.0", port=PORT)
