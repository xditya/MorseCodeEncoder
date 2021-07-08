# Morse Code Encoder.
# < (c) @xditya >

from telethon import events, Button, TelegramClient
from decouple import config
import logging
from helpers import encode_deocde, send_start

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.info("Starting...")

APP_ID = 6
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

try:
    BOT_TOKEN = config("BOT_TOKEN")
except:
    logging.warning("Please create a .env file with BOT_TOKEN.")
    exit()

try:
    bot = TelegramClient("BotzHub", APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
except Exception as e:
    logging.info(f"Error\n{e}")
    exit(0)


@bot.on(
    events.NewMessage(incoming=True, func=lambda e: e.is_private, pattern="^/start$")
)
async def start_ms(event):
    await send_start(event, "message")


@bot.on(events.callbackquery.CallbackQuery(data="start_back"))
async def back_to_strt(event):
    await send_start(event, "edt")


@bot.on(events.callbackquery.CallbackQuery(data="help_me"))
async def help_me(event):
    await event.edit(
        f"""**Help menu!**\n
Commands available:
`/encode <text>` - Encode text in english to morse code.
`/deocde <text>` - Decode text from morse code to english.""",
        buttons=Button.inline("Back", data="start_back"),
    )


@bot.on(
    events.NewMessage(incoming=True, func=lambda e: e.is_private, pattern="^/encode")
)
async def encoder(event):
    await encode_deocde(event, "encode")


@bot.on(
    events.NewMessage(incoming=True, func=lambda e: e.is_private, pattern="^/decode")
)
async def decoder(event):
    await encode_deocde(event, "decode")


logging.info("Started. Join @BotzHub for more :)")
bot.run_until_disconnected()
