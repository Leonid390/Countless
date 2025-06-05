from logic import *
from config import *
from telebot import TeleBot

bot = TeleBot(API_TOKEN)
correct_answer = None
point_count = 0 

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я бот по соревнованиям в вычислениях!) 
""")
    
@bot.message_handler(commands=['lvl1'])
def lvl1_comm(message):
    global correct_answer
    saying_0, answer = problem_generator_lvl1()
    saying_str = ' '.join(str(item) for item in saying_0)
    correct_answer = answer
    bot.send_message(message.chat.id, saying_str)

@bot.message_handler(func=lambda message: True)
def answer_check(message):
    global correct_answer
    global point_count
    try:
        user_response = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите число.")
        return

    if correct_answer is None:
        # Нет активной задачи
        return

    if user_response == correct_answer:
        bot.send_message(message.chat.id, "Правильно!")
        point_count = point_count + 1
    else:
        bot.send_message(message.chat.id, f"Неправильно. Правильный ответ: {correct_answer}")                    

@bot.message_handler(commands=['my_score'])
def total_score(message):
    bot.send_message(message.chat.id, point_count)

if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()