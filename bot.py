import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.loop import MessageLoop
from typing import Dict
from telepot import Bot
from predict import list_of_merk

class TeleBot:
    def __init__(self, token: str) -> None:
        """
        Inisialisasi bot dengan token dan memberikan default value untuk status lampu dan permainan Tic Tac Toe
        """
        self.bot: Bot = Bot(token)
        self.lamp_status: str = "Off"
        self.handlers: Dict[str, function] = {}
        self.distance: int = None

    def handle_message(self, msg: Dict) -> None:
        """
        Menangani pesan pada bot telegram
        """
        chat_id = msg['chat']['id']
        if (msg['text'] == '/mulai') or (msg['text'] == '/mulai@Teamtwo_bot'):
            buttons = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=x, callback_data=x.lower()) for x in list_of_merk[i:i+2]]
                for i in range(0, len(list_of_merk), 2)
            ])

            self.bot.sendMessage(chat_id, 'Selamat datang di Bot Prediksi Harga Mobil...\n\nSilakan pilih merk:', reply_markup=buttons)
            
    def run(self) -> None:
        """
        Menjalankan bot dan menangani pesan dengan menggunakan `MessageLoop`
        """
        MessageLoop(self.bot, {'chat': self.handle_message, 'callback_query': self.on_callback_query}).run_as_thread()
        print('Bot sedang berjalan...')
        while True:
            pass
            
    def add_handler(self, command: str, handler) -> None:
        """
        Menambahkan handler untuk command tertentu
        """
        self.handlers[command] = handler

    def on_callback_query(self, msg: Dict) -> None:
        """
        Menangani callback query (ketika tombol ditekan)
        """
        query_id, _, query_data = telepot.glance(msg, flavor='callback_query')
        chat_id = msg['message']['chat']['id']
        message_id = msg['message']['message_id']
        username = msg['from']['username']
        # print(msg)
        
        # Memeriksa apakah pesan diterima dalam obrolan grup atau pesan pribadi
        chat_type = msg['message']['chat']['type']

        # Mengecek jenis chat dan isi dari var msg
        print(f"Callback query ditekan secara {chat_type}")
        # print(f"Isi msg: {msg}")
        
        self.handlers[query_data](self, query_id, chat_id, message_id, username, chat_type)