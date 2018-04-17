from telegram import ChatAction
from telegram.ext import CommandHandler, MessageHandler,Updater,Filters
import db
import mysql.connector


def message(bot,update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    update.message.reply_text("I'm sorry, i understand only commands!")

def showTasks(bot, update):
    tasks = db.showTasks()
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    if len(tasks)== 0:
        update.message.reply_text("Nothing to do here!")
    else:
        update.message.reply_text(tasks)

def newTask(bot,update,args):
    arg=' '.join(args)
    db.addTask(arg)

def removeTask(bot,update,args):
    arg=' '.join(args)
    db.removeTask(arg)


def removeAllTasks(bot,update,args):
    arg = ' '.join(args)
    db.removeAll(arg)


def main():
    updater = Updater("555762929:AAE7ZLNOkRtF_OjGwAPOKTEizhQRG-iFK18")
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text,message))

    dp.add_handler(CommandHandler("showTasks", showTasks))
    dp.add_handler(CommandHandler("newTask", newTask,pass_args=True))
    dp.add_handler(CommandHandler("removeTask", removeTask,pass_args=True))
    dp.add_handler(CommandHandler("removeAllTasks", removeAllTasks,pass_args=True))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()