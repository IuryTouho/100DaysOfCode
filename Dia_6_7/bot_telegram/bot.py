from telegram import Update
from telegram.ext import *
import constants,responses


def start_command(update,context):
    update.message.reply_text(f"Olá {update.message.from_user['first_name']} Seja bem-vindo.")

def help_command(update,context):
    update.message.reply_text("oi olá -> retorna uma saudação\n ")

async def handle_message(update,context):
    txt = str(update.message.text).lower()
    response = responses.sample_response(txt)

    await update.message.reply_text(response)

def error(update, context):
    print(f"Update: {update} Contexto: {context.error} ")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


def main():
    app = ApplicationBuilder().token(constants.API_KEY).build()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    

    app.run_polling()
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
   


main()
