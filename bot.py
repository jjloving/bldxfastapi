from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import asyncio
import logging

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
        
        # 1. Send welcome message with a welcome image
        welcome_photo_url = "https://imgur.com/aDHfR5m"  # Updated with user's image
        welcome_caption = f"👋 Welcome to BLDX TON Miner App, {username}! 🚀\nLet's get started on your mining journey."
        await update.message.reply_photo(photo=welcome_photo_url, caption=welcome_caption)
        
        # 2. Wait for a few seconds
        await asyncio.sleep(3)
        
        # 3. Send the main miner message with buttons
        miner_photo_url = "https://imgur.com/a/HmwURF1"  # Using same image for consistency
        miner_caption = (
            "Get Ready, Get Set, Mine TON! 🚀⛏️💰\n"
            "Start your journey with BLDX TON Miner and unlock exciting rewards! 🚀"
        )
        keyboard = [
            [InlineKeyboardButton("Open BLDX Miner", url="https://t.me/BOLDXOfficial_Bot?ref=zikky")],
            [InlineKeyboardButton("Join Community", url="https://t.me/bldxtonminers")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Send the miner message with buttons
        await update.message.reply_photo(photo=miner_photo_url, caption=miner_caption, reply_markup=reply_markup)
        logger.info(f"Successfully sent messages to user {username}")
    except Exception as e:
        logger.error(f"Error in start command: {str(e)}")
        await update.message.reply_text("An error occurred. Please try again later.")

def main():
    # Initialize bot
    logger.info("Starting bot...")
    application = ApplicationBuilder().token("7545746171:AAFsI8zRnrs0_INPxO6eFrCHKkukAs9FRmM").build()

    # Add command handler
    application.add_handler(CommandHandler("start", start))

    # Run the bot
    logger.info("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
