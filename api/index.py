from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from telegram import Update
from .bot import application, logger
import json

app = FastAPI()

@app.get("/api/health")
async def health_check():
    return {"status": "alive", "bot_initialized": bool(application)}

@app.post("/api/webhook")
async def webhook(request: Request):
    try:
        # Log the incoming request
        body = await request.body()
        logger.info(f"Received webhook request: {body.decode()}")
        
        # Parse the update
        update_dict = json.loads(body)
        update = Update.de_json(update_dict, application.bot)
        
        # Process the update
        await application.process_update(update)
        
        return JSONResponse(content={"status": "ok"})
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        # Return 200 status even on error to prevent Telegram from retrying
        return JSONResponse(
            status_code=200,
            content={"status": "error", "message": str(e)}
        )

@app.get("/")
async def root():
    return {
        "message": "Bot is running",
        "bot_token_exists": bool(application.bot.token),
        "webhook_path": "/api/webhook"
    }

# This file is required for Vercel serverless functions
# It simply exports the FastAPI app from main.py 