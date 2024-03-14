import datetime
import telegram
from telegram.ext import Updater, CommandHandler

# Funzione per ottenere il numero del giorno
def day_counter() -> int:
    start_date = datetime.datetime(2024, 3, 12)  # Data di inizio del progetto
    today = datetime.datetime.now()
    delta = today - start_date
    return delta.days + 1

# Funzione per inviare il messaggio di benvenuto
def send_welcome_message(context) -> None:
    message = "Benvenuti nel giorno {} di Project 1861, dove ogni giorno conta.".format(day_counter())
    context.bot.send_message(chat_id='@project_1861', text=message)

# Funzione per aggiornare il countdown
def update_countdown(context) -> None:
    remaining_time = datetime.datetime(2029, 4, 16) - datetime.datetime.now()
    countdown = remaining_time.total_seconds()
    days = int(countdown // (24 * 3600))
    hours = int((countdown % (24 * 3600)) // 3600)
    minutes = int((countdown % 3600) // 60)
    seconds = int(countdown % 60)
    message = "Countdown: {} giorni, {} ore, {} minuti, {} secondi".format(days, hours, minutes, seconds)
    context.bot.send_message(chat_id='@project_1861', text=message)

def main():
    bot_token = '7139403290:AAGpxmnFfTUySWMlw-cO8JN7IqeeID8DAaE'  # Inserisci il token del tuo bot
    updater = Updater(bot_token, use_context=True)

    # Aggiungi gestore per il comando /start
    updater.dispatcher.add_handler(CommandHandler("start", send_welcome_message))

    # Avvia il countdown
    updater.job_queue.run_repeating(update_countdown, interval=1, first=0)

    # Avvia il bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
