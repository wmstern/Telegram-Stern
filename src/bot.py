import os
import logging

from telegram import __version__ as TG_VER
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

from telegram import (
    Update
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def StartCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        rf"Hi {user.mention_html()}!\n\nCommands:\n\n/help\n/start\n/test",
        reply_markup=ForceReply(selective=True)
    )

async def HelpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Commands:\n\n/help\n/start\n/test")

async def TestCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(f'Tested by: {update.effective_user)

def main() -> None:
    """Run bot."""

    app = ApplicationBuilder().token(os.environ.get("BOT_TOKEN", "")).build()

    app.add_handler(CommandHandler("start", StartCommand))
    app.add_handler(CommandHandler("test", TestCommand))
    app.add_handler(CommandHandler("help", HelpCommand))

    app.run_polling()

if __name__ == "__main__":
    main()
