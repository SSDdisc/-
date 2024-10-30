import telebot

TOKEN = '7784738994:AAGiQGRXrrbRwgcctejDNQGXJ4kQdwXe-68'
bot = telebot.TeleBot(TOKEN)

seats = {
    '1A': True,
    '1B': True,
    '1C': True,
    '2A': True,
    '2B': True,
    '2C': True,
    '3A': True,
    '3B': True,
    '3C': True,
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Добро пожаловать в бот для бронирования авиабилетов!\n"
                          "Введите /view для просмотра свободных мест или /book для бронирования места.")

@bot.message_handler(commands=['view'])
def view_seats(message):
    available_seats = [seat for seat, is_free in seats.items() if is_free]
    if available_seats:
        bot.reply_to(message, "Свободные места: " + ", ".join(available_seats))
    else:
        bot.reply_to(message, "К сожалению, свободных мест нет.")

@bot.message_handler(commands=['book'])
def book_seat(message):
    bot.reply_to(message, "Введите номер места, которое вы хотите забронировать (например, 1A):")
    bot.register_next_step_handler(message, process_booking)

def process_booking(message):
    seat_number = message.text.strip().upper()  
    
    if seat_number(message):  
        if seats[seat_number]:  
            seats[seat_number] = False 
            bot.reply_to(message, f"Место {seat_number} успешно забронировано!")
        else:
            bot.reply_to(message, f"Место {seat_number} уже забронировано.")
    else:
        bot.reply_to(message, "Неверный номер места. Пожалуйста, попробуйте снова.")

if __name__ == '__main__':
    bot.polling(none_stop=True)
