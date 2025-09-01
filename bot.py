import os # 导入 os 模块
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# --- 配置 ---
# 从环境变量中读取 BOT_TOKEN，如果找不到，就使用一个默认提示
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_NOT_FOUND")
# 你的 Web App URL，这个可以公开
WEB_APP_URL = "https://dewee-dev.github.io/HK_Dec/index.html" # ‼️ 替换成你的 GitHub Pages URL

# --- 机器人逻辑 ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理 /start 命令，发送一个带有 Web App 按钮的消息"""
    keyboard = [
        [InlineKeyboardButton("打开加解密工具", web_app={"url": WEB_APP_URL})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "你好！点击下面的按钮来打开内嵌的加解密工具：",
        reply_markup=reply_markup
    )

def main():
    """主函数，启动机器人"""
    if BOT_TOKEN == "YOUR_BOT_TOKEN_NOT_FOUND":
        print("错误：未找到 BOT_TOKEN 环境变量！请在 Render 中设置它。")
        return

    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    print("机器人正在运行...")
    application.run_polling()

if __name__ == "__main__":
    main()
