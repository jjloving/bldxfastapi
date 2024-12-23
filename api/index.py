from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from telegram import Update
from .bot import application, logger

app = FastAPI()

@app.get("/api/health")
async def health_check():
    return {"status": "alive"}

@app.post("/api/webhook")
async def webhook(request: Request):
    try:
        update = Update.de_json(await request.json(), application.bot)
        await application.process_update(update)
        return JSONResponse(content={"status": "ok"})
    except Exception as e:
        logger.error(f"Error processing update: {str(e)}")
        return JSONResponse(content={"status": "error", "message": str(e)})

@app.get("/")
async def root():
    return {"message": "Bot is running"}

# This file is required for Vercel serverless functions
# It simply exports the FastAPI app from main.py 