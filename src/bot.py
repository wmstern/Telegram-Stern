import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def TestCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Tested by: {update.effective_user.first_name}')


app = ApplicationBuilder().token(os.environ.get("BOT_TOKEN", "")).build()

app.add_handler(CommandHandler("test", TestCommand))

app.run_polling()
