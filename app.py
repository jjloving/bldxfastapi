from quart import Quart, request, jsonify
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import asyncio
import os
import logging

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

app = Quart(__name__)

# Initialize the Telegram bot
TELEGRAM_TOKEN = "7545746171:AAFsI8zRnrs0_INPxO6eFrCHKkukAs9FRmM"
application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

async def start(update: Update, context: CallbackContext):
    try:
        logger.info("Start command received")
        user = update.effective_user
        username = user.username or user.first_name
        logger.info(f"Processing start command for user: {username}")
        
        # 1. Send welcome message with a welcome image
        welcome_photo_url = "https://i.imgur.com/aDHfR5m.jpg"  # Fixed Imgur URL
        welcome_caption = f"👋 Welcome to BLDX TON Miner App, {username}! 🚀\nLet's get started on your mining journey."
        logger.info("Sending welcome message")
        await update.message.reply_photo(photo=welcome_photo_url, caption=welcome_caption)
        
        # 2. Wait for a few seconds
        await asyncio.sleep(3)
        
        # 3. Send the main miner message with buttons
        miner_photo_url = "https://i.imgur.com/6JUmXY9.jpg"  # Fixed Imgur URL
        miner_caption = (
            "Get Ready, Get Set, Mine TON! 🚀⛏️💰\n"
            "Start your journey with **BLDX TON Miner** and unlock exciting rewards! 🚀"
        )
        keyboard = [
            [InlineKeyboardButton("Open BLDX Miner", url="https://t.me/BOLDXOfficial_Bot?ref=zikky")],
            [InlineKeyboardButton("Join Community", url="https://t.me/bldxtonminers")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        logger.info("Sending miner message")
        await update.message.reply_photo(photo=miner_photo_url, caption=miner_caption, reply_markup=reply_markup)
        logger.info("Start command completed successfully")
    except Exception as e:
        logger.error(f"Error in start command: {str(e)}", exc_info=True)
        await update.message.reply_text("An error occurred. Please try again later.")

# Register the command handler
application.add_handler(CommandHandler("start", start))

@app.route('/webhook', methods=['POST'])
async def webhook():
    try:
        logger.info("Webhook request received")
        data = await request.get_json()
        logger.info(f"Webhook data: {data}")
        
        update = Update.de_json(data, application.bot)
        logger.info("Update object created")
        
        await application.process_update(update)
        logger.info("Update processed successfully")
        
        return jsonify({'status': 'ok'})
    except Exception as e:
        logger.error(f"Webhook error: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/', methods=['GET'])
async def index():
    return jsonify({'status': 'Bot is running'})

@app.route('/health', methods=['GET'])
async def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    # Verify the webhook
    logger.info("Starting the application...")
    logger.info(f"Webhook URL should be set to: https://e06c-105-112-121-21.ngrok-free.app/webhook")
    
    # Run the app using hypercorn with asyncio
    port = int(os.environ.get('PORT', 5000))
    asyncio.run(app.run_task(host='0.0.0.0', port=port)) 