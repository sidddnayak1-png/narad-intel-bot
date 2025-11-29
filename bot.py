import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")  # Make sure this is set in Render

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Narad Intel Bot is online!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
