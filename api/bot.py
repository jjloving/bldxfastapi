from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import asyncio
import logging
import os
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start command handler
async def start(update: Update, context: CallbackContext):
    try:
        user = update.effective_user
        username = user.username or user.first_name

        welcome_photo_url = "https://imgur.com/aDHfR5m"
        welcome_caption = f"👋 Welcome to BLDX TON Miner App, {username}! 🚀\nLet's get started on your mining journey."
        await update.message.reply_photo(photo=welcome_photo_url, caption=welcome_caption)

        await asyncio.sleep(3)

        miner_photo_url = "https://imgur.com/a/HmwURF1"
        miner_caption = (
            "Get Ready, Get Set, Mine TON! 🚀⛏️💰\n"
            "Start your journey with BLDX TON Miner and unlock exciting rewards! 🚀"
        )
        keyboard = [
            [InlineKeyboardButton("Open BLDX Miner", url="https://t.me/BLDXTONbot")],
            [InlineKeyboardButton("Join Community", url="https://t.me/bldxtonminers")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_photo(photo=miner_photo_url, caption=miner_caption, reply_markup=reply_markup)
        logger.info(f"Successfully sent messages to user {username}")
    except Exception as e:
        logger.error(f"Error in start command: {str(e)}")
        await update.message.reply_text("An error occurred. Please try again later.")

# Initialize bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    logger.error("No BOT_TOKEN found in environment variables")
    raise ValueError("No BOT_TOKEN found in environment variables")

application = ApplicationBuilder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start)) 