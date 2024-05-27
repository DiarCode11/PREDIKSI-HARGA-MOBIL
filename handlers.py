from bot import TeleBot
from prediksi_obj import PrediksiHarga
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from predict import list_of_merk, list_of_fuel, list_of_seller_type, list_of_owner, list_of_transmission

# STEP PERTAMA
def buttons_merk(teleBot: TeleBot, query_id: int, chat_id: int, message_id: int, user_id: int, chat_type:str):
    teleBot.bot.answerCallbackQuery(query_id, text='Pilih merk:')
    msg_id = (chat_id, message_id)

    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=x, callback_data=x.lower()) for x in list_of_merk]
	])

    teleBot.bot.editMessageText(msg_id, 'Selamat datang di Bot Prediksi Harga Mobil...\n\nSilakan pilih merk:')
    teleBot.bot.editMessageReplyMarkup(msg_id, reply_markup=buttons)

def buttons_merk_handler(merk: str):
    def handler(teleBot: TeleBot, query_id: int, chat_id: int, message_id: int, user_id: int, chat_type:str):
        teleBot.bot.answerCallbackQuery(query_id, text=f'Merk yang dipilih: {merk}')
        prediksi = PrediksiHarga(message_id, user_id)
        prediksi.set_merk(merk)
        prediksi.save()
        fuel_buttons(teleBot, query_id, chat_id, message_id, user_id, chat_type)
    return handler

# STEP KEDUA
def fuel_buttons(teleBot: TeleBot, query_id: int, chat_id: int, message_id: int, user_id: int, chat_type:str):
    teleBot.bot.answerCallbackQuery(query_id, text='Pilih merk:')
    msg_id = (chat_id, message_id)

    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=x, callback_data=x.lower()) for x in list_of_fuel]
	])
    
    teleBot.bot.editMessageText(msg_id, 'Silahkan pilih jenis bahan bakar:')
    teleBot.bot.editMessageReplyMarkup(msg_id, reply_markup=buttons)

def fuel_buttons_handler(fuel: str):
    def handler(teleBot: TeleBot, query_id: int, chat_id: int, message_id: int, user_id: int, chat_type:str):
        prediksi: PrediksiHarga = PrediksiHarga.load(message_id)
        if prediksi.user_id != user_id:
            return
        teleBot.bot.answerCallbackQuery(query_id, text=f'Bahan bakar yang dipilih: {fuel}')
        prediksi.set_fuel(fuel)
        prediksi.save()
        seller_type_buttons(teleBot, query_id, chat_id, message_id, user_id, chat_type)
    return handler

# STEP 3
def seller_type_buttons(teleBot: TeleBot, query_id: int, chat_id: int, message_id: int, user_id: int, chat_type:str):
    teleBot.bot.answerCallbackQuery(query_id, text='Pilih jenis seller:')
    msg_id = (chat_id, message_id)

    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [
            [InlineKeyboardButton(text=x, callback_data=x.lower()) for x in list_of_seller_type[:2]],
            [InlineKeyboardButton(text=x, callback_data=x.lower()) for x in list_of_seller_type[2:]]
        ]
    ])
    
    teleBot.bot.editMessageText(msg_id, 'Silahkan pilih jenis seller:')
    teleBot.bot.editMessageReplyMarkup(msg_id, reply_markup=buttons)
    
def seller_type_buttons_handler(seller_type: str):
    def handler(teleBot: TeleBot, query_id: int, chat_id: int, message_id: int, user_id: int, chat_type:str):
        prediksi: PrediksiHarga = PrediksiHarga.load(message_id)
        if prediksi.user_id != user_id:
            return
        teleBot.bot.answerCallbackQuery(query_id, text=f'Seller yang dipilih: {seller_type}')
        prediksi.set_seller_type(seller_type)
        prediksi.save()
        transmission_buttons(teleBot, query_id, chat_id, message_id, user_id, chat_type)
    
    return handler

# STEP 4
def transmission_buttons(teleBot: TeleBot, query_id: int, chat_id: int, message_id: int, user_id: int, chat_type:str):
    teleBot.bot.answerCallbackQuery(query_id, text='Pilih jenis transmisi:')
    msg_id = (chat_id, message_id)

    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=x, callback_data=x.lower()) for x in list_of_transmission]
    ])
    
    teleBot.bot.editMessageText(msg_id, 'Silahkan pilih jenis transmisi:')
    teleBot.bot.editMessageReplyMarkup(msg_id, reply_markup=buttons)

def transmission_buttons_handler(transmission: str):
    def handler(teleBot: TeleBot, query_id: int, chat_id: int, message_id: int, user_id: int, chat_type:str):
        prediksi: PrediksiHarga = PrediksiHarga.load(message_id)
        if prediksi.user_id != user_id:
            return
        teleBot.bot.answerCallbackQuery(query_id, text=f'Transmisi yang dipilih: {transmission}')
        prediksi.set_transmission(transmission)
        prediksi.save()
        owner_buttons(teleBot, query_id, chat_id, message_id, user_id, chat_type)

    return handler

# STEP 5
def owner_buttons(teleBot: TeleBot, query_id: int, chat_id: int, message_id: int, user_id: int, chat_type:str):
    teleBot.bot.answerCallbackQuery(query_id, text='Pilih owner:')
    msg_id = (chat_id, message_id)

    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [
            [InlineKeyboardButton(text=x, callback_data=x.lower()) for x in list_of_owner[:len(list_of_owner)//2]],
            [InlineKeyboardButton(text=x, callback_data=x.lower()) for x in list_of_owner[len(list_of_owner)//2:]],
        ]
    ])
    
    teleBot.bot.editMessageText(msg_id, 'Silahkan pilih owner:')
    teleBot.bot.editMessageReplyMarkup(msg_id, reply_markup=buttons)
    
def owner_buttons_handler(owner: str):
    def handler(teleBot: TeleBot, query_id: int, chat_id: int, message_id: int, user_id: int, chat_type:str):
        prediksi: PrediksiHarga = PrediksiHarga.load(message_id)
        if prediksi.user_id != user_id:
            return
        teleBot.bot.answerCallbackQuery(query_id, text=f'Owner yang dipilih: {owner}')
        prediksi.set_owner(owner)
        prediksi.save()
        teleBot.bot.sendMessage(chat_id, "Berapa tuh harganya?")
    return handler
    
def add_handlers(teleBot: TeleBot):
    for merk in list_of_merk:
        teleBot.add_handler(merk.lower(), buttons_merk_handler(merk))

    for fuel in list_of_fuel:
        teleBot.add_handler(fuel.lower(), fuel_buttons_handler(fuel))
    
    for seller_type in list_of_seller_type:
        teleBot.add_handler(seller_type.lower(), seller_type_buttons_handler(seller_type))

    for transmission in list_of_transmission:
        teleBot.add_handler(transmission.lower(), transmission_buttons_handler(transmission))

    for owner in list_of_owner:
        teleBot.add_handler(owner.lower(), owner_buttons_handler(owner))
    