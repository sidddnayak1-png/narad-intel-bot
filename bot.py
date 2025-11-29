import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Use environment variable from Render
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")  

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Narad Intel Bot is online.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    
    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
