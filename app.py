from flask import Flask
from bot import bot
import asyncio
import threading

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TechifyBots is Running!'

def run_bot():
    """బాట్‌ను విడిగా రన్ చేయడానికి ఒక ఫంక్షన్"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    # బాట్‌ను స్టార్ట్ చేయడం
    loop.run_until_complete(bot.start())
    print("టెలిగ్రామ్ బాట్ స్టార్ట్ అయ్యింది! 🎉")
    
    # బాట్ నిరంతరం రన్ అవ్వడానికి idle అవసరం లేదు, 
    # ఎందుకంటే లూప్ రన్ అవుతూనే ఉంటుంది.
    from pyrogram import idle
    loop.run_until_complete(idle())

# బాట్‌ను బ్యాక్‌గ్రౌండ్ థ్రెడ్‌లో స్టార్ట్ చేయడం
threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    # లోకల్‌గా టెస్ట్ చేసేటప్పుడు
    app.run(host="0.0.0.0", port=10000)
    
