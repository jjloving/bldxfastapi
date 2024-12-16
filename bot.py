from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import asyncio  # Import asyncio for delay

# Start command handler
async def start(update: Update, context: CallbackContext):
    user = update.effective_user  # Get the user's info
    username = user.username or user.first_name  # Fallback to first name if no username
    
    # 1. Send welcome message with a welcome image
    welcome_photo_url = "https://imgur.com/aDHfR5m"  # Replace with your welcome image URL
    welcome_caption = f"👋 Welcome to BLDX TON Miner App, {username}! 🚀\nLet's get started on your mining journey."
    await update.message.reply_photo(photo=welcome_photo_url, caption=welcome_caption)
    
    # 2. Wait for a few seconds
    await asyncio.sleep(3)  # Delay for 3 seconds
    
    # 3. Send the main miner message with buttons
    miner_photo_url = "https://imgur.com/a/6JUmXY9"  # Replace with your miner image URL
    miner_caption = (
        "Get Ready, Get Set, Mine TON! 🚀⛏️💰\n"
        "Start your journey with **BLDX TON Miner** and unlock exciting rewards! 🚀"
    )
    keyboard = [
        [InlineKeyboardButton("Open BLDX Miner", url="https://t.me/BOLDXOfficial_Bot?ref=zikky")],
        [InlineKeyboardButton("Join Community", url="https://t.me/bldxtonminers")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the miner message with buttons
    await update.message.reply_photo(photo=miner_photo_url, caption=miner_caption, reply_markup=reply_markup)

# Main function to run the bot
def main():
    application = ApplicationBuilder().token("7667533446:AAEW0BafwTz6HHuhTBUrjdISoqFmkk9Bi4s").build()

    # Add command handler
    application.add_handler(CommandHandler("start", start))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
