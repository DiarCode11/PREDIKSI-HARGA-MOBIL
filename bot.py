import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.loop import MessageLoop
from typing import Dict
from telepot import Bot
from predict import list_of_merk
from prediksi_obj import PrediksiHarga

class TeleBot:
    def __init__(self, token: str) -> None:
        """
        Inisialisasi bot dengan token dan memberikan default value untuk status lampu dan permainan Tic Tac Toe
        """
        self.bot: Bot = Bot(token)
        self.handlers: Dict[str, function] = {}
        self.all_prediksi: Dict[int, PrediksiHarga] = {}

    def handle_message(self, msg: Dict) -> None:
        """
        Menangani pesan pada bot telegram
        """
        chat_id = msg['chat']['id']
        username = msg['from']['username']
        if (msg['text'] == '/start') or (msg['text'] == '/start@Teamtwo_bot'):
            self.bot.sendMessage(chat_id, "<strong>Selamat datang di Bot Prediksi Harga Mobil</strong>\n\nUntuk menggunakan chatbot ini sangatlah mudah. Kamu hanya perlu menginputkan atribut-atribut dari mobil seperti merk, tahun pembuatan, dan lain sebagainya. Untuk memulai layanan bot kamu bisa klik /mulai 😊", parse_mode="HTML")
        elif (msg['text'] == '/mulai') or (msg['text'] == '/mulai@Teamtwo_bot'):
            buttons = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text=x, callback_data=x.lower()) for x in list_of_merk[i:i+2]]
                for i in range(0, len(list_of_merk), 2)
            ])

            self.bot.sendMessage(chat_id, 'Silakan pilih merk:', reply_markup=buttons)
            return

        # if the first letter is a number
        if msg['text'][0].isdigit():
            finished, prediksi = self.handle_input_text(msg['text'], user_id=username)
            if not finished and prediksi is not None:
                self.bot.sendMessage(chat_id, "Baik, silahkan masukan km perjalanan (cth: 100000)")
            elif finished and prediksi is not None:
                harga = prediksi.prediksi_harga()
                self.delete_prediction(prediksi.message_id)
                self.bot.sendMessage(chat_id, f"Detail Prediksi\n\nMerk: {prediksi.merk}\nTahun: {prediksi.year}\nKM perjalanan: {prediksi.km_driven} km\nBahan bakar: {prediksi.fuel}\nTipe seller: {prediksi.seller_type}\nTransmisi: {prediksi.transmission}\nOwner: {prediksi.owner}" + "\n\nPrediksi harga: " + str(harga))
            return
    
    def handle_input_text(self, text: str, user_id: int):
        """
        Mencari prediksi yang belum diinputkan oleh user
        """
        for message_id, prediksi in self.all_prediksi.items():
            if prediksi.user_id == user_id:
                if prediksi.year is None:
                    prediksi.set_year(text)
                    return (False, prediksi)
                elif prediksi.km_driven is None:
                    prediksi.set_km_driven(text)
                    return (True, prediksi)
        return (False, None)
    
    def delete_prediction(self, message_id: int) -> None:
        """
        Menghapus objek prediksi berdasarkan message_id
        """
        if message_id in self.all_prediksi:
            self.all_prediksi[message_id].delete()
            del self.all_prediksi[message_id]
        
                    
    
    def add_new_prediction(self, prediksi: PrediksiHarga) -> None:
        """
        Menambahkan objek prediksi ke dictionary
        """
        prediksi.save()
        self.all_prediksi[prediksi.message_id] = prediksi
        
    def get_prediction(self, message_id: int) -> PrediksiHarga:
        """
        Mengembalikan objek prediksi berdasarkan message_id
        """
        if message_id not in self.all_prediksi:
            prediction = PrediksiHarga.load(message_id)
            if prediction is not None:
                self.add_new_prediction(prediction)
                return prediction
            return None
        return self.all_prediksi[message_id]
    
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