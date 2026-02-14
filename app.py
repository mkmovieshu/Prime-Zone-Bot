import os
import threading
import asyncio
from flask import Flask
from pyrogram import idle
from bot import bot  # మీ బాట్ ఇన్‌స్టాన్స్

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TechifyBots is running successfully!'

def run_bot():
    """బ్యాక్‌గ్రౌండ్‌లో బాట్‌ను రన్ చేసే ఫంక్షన్"""
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        # బాట్‌ను స్టార్ట్ చేయడం
        loop.run_until_complete(bot.start())
        print("Telegram Bot Started! 🎉")
        
        # బాట్ నిరంతరం రన్ అవ్వడానికి idle
        loop.run_until_complete(idle())
    except Exception as e:
        print(f"Bot Error: {e}")

# Gunicorn మల్టిపుల్ వర్కర్లను వాడుతుంది. 
# కాబట్టి బాట్ కేవలం ఒకేసారి స్టార్ట్ అయ్యేలా చూసుకోవాలి.
if __name__ == "__main__":
    # ఇది లోకల్ రన్ కోసం మాత్రమే
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
else:
    # Render (Gunicorn) లో రన్ అయ్యేటప్పుడు
    threading.Thread(target=run_bot, daemon=True).start()
