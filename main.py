from bot import TeleBot
from handlers import add_handlers
from dotenv import load_dotenv
import os

load_dotenv()

# Get the API token from the environment variable
TOKEN = os.environ.get('TOKEN')

# Main function yang dipanggil saat program dijalankan secara langsung
if __name__ == "__main__":
    # Membuat objek TeleBot dengan token yang diambil dari environment variable
    tele_bot = TeleBot(TOKEN)
    # Menambahkan handler untuk perintah
    add_handlers(tele_bot)
    # Menjalankan bot
    tele_bot.run()
    