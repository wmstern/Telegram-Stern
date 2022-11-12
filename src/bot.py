import os
from telegram import (
    Update
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)


async def TestCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Tested by: {update.effective_user.first_name}')

async def HelpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Commands:\n\n/test")

def main() -> None:
    """Run bot."""

    app = ApplicationBuilder().token(os.environ.get("BOT_TOKEN", "")).build()

    app.add_handler(CommandHandler("test", TestCommand))
    app.add_handler(CommandHandler("help", HelpCommand))

    app.run_polling()

main()
