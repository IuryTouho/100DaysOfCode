from telegram.ext import *
import telegram
import constants,responses


def start_command(update,context):
    update.message.reply_text(f"Olá {update.message.from_user['first_name']} Seja bem-vindo.")

def help_command(update,context):
    update.message.reply_text("oi olá -> retorna uma saudação\n ")

def handle_message(update,context):
    txt = str(update.message.text).lower()
    response = responses.sample_response(txt)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update: {update} Contexto: {context.error} ")

def main():
    """
    updater = Updater(constants.API_KEY, True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(CommandHandler(Filters.text,handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
    """

    bot = telegram.Bot(token=constants.API_KEY)
    
    bot.dispatcher.add_handler(telegram.CommandHandler("start", start_command))
    bot.dispatcher.add_handler(telegram.CommandHandler("help",help_command))
    bot.dispatcher.add_handler(CommandHandler(Filters.text,handle_message))
    bot.add_error_handler(error)

    bot.start_polling()
main()
