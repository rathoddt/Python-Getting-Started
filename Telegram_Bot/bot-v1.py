from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN: Final = "7119703753:AAEgZ7l8KTLIvrfsZwRMm_OrsZM_3toTvhQ"
BOT_USERNAME: Final = "@dilip_signal_bot"

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE ):
    await update.message.reply_text("Thanks for chatting with me. I am a signal bot")
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE ):
    await update.message.reply_text("Please type somthing so tha I can respond")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE ):
    await update.message.reply_text("custom command console")


#Responses
def handle_response(text: str) -> str:
    processed : str = text.lower()
    if "Hello" in processed:
        return "Hey there!"

    if "How are u" in processed:
        return "I am good"

    return "I do not understand what you wrote"
    
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text :str = update.message.text

    print(f'User ({update.message.chat.id}) {message_type}: {text}')

    if message_type=="group":
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print("BOT:", response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update :{update} caused following error {context.error}')


if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)
    print("Polling...")
    app.run_polling(poll_interval=2)
    




          
    
