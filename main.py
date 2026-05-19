from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler
# from telegram import ReplyKeyboardMarkup
from config import BOT_TOKEN
from handler import form_input_transaction
# from mapping_trans import transaction_data


user_tele = {}
reply_keyboard = [["/show", "/add"], ["/help"]]

async def start(update, context:ContextTypes.DEFAULT_TYPE):
    tele_id = update.effective_chat.id
    name = update.effective_chat.first_name
    print(f"Message from {tele_id} = (Start) user is start the bot")

    user_tele["tele_id"] = tele_id

    message = (
        f"Selamat Datang, {name}! 👋\n\n"
        "Saya adalah bot keuangan pribadi yang akan membantu Anda mencatat dan mengelola transaksi keuangan Anda. 💰\n\n"
        "Kegunaan saya meliputi:\n"
        "1. Mencatat transaksi keuangan dengan mudah.\n"
        "2. Menyediakan laporan keuangan yang jelas dan terperinci.\n\n"
        "Ketik /help untuk melihat daftar perintah yang tersedia. Saya siap membantu Anda mengelola keuangan dengan lebih baik! 🚀"
    )
    await update.message.reply_text(message, parse_mode="Markdown")

async def show_transaction(update, context:ContextTypes.DEFAULT_TYPE):
    tele_id = update.effective_chat.id
    print(f"Message from {tele_id} = (Show Transaction) user is show transaction")

    if tele_id != user_tele.get("tele_id"):
        print("Response from Bot = (Invalid) User not registered.")
        await update.message.reply_text("Silakan mulai dengan perintah /start terlebih dahulu.")
        return
    
    if not transaction_data:
        print("Response from Bot = (Invalid) No transactions found.")
        await update.message.reply_text("Belum ada transaksi yang tercatat.")
        return

    message = "Daftar Transaksi:\n\n"
    print(f"Response from Bot = (Show) Total transactions: {len(transaction_data)}")
    for t in transaction_data:
        if t.tele_id == tele_id:
            message += (
                f"{t.id}. \n"
                f"📆Date           : {t.created_date.strftime('%a %Y-%m-%d')}\n"
                f"🛒Category    : {t.category}\n"
                f"📝Description : {t.description}\n"
                f"💲Nominal     : {t.nominal if t.nominal.is_integer() else t.nominal:,.0f}\n"
                f"💳Instrument  : {t.instrument}\n"
            )
    await update.message.reply_text(message, parse_mode="Markdown")

async def add_transaction(update, context:ContextTypes.DEFAULT_TYPE):
    tele_id = update.effective_chat.id
    context_args = context.args
    print(f"Message from {tele_id} = (Add Transaction) user is adding transaction")
    print(f"Context args: {context_args}")

    if tele_id != user_tele.get("tele_id"):
        await update.message.reply_text("Silakan mulai dengan perintah /start terlebih dahulu.")
        return
    
    message = "Fitur menambahkan transaksi masih dalam pengembangan. Mohon tunggu update selanjutnya."
    await update.message.reply_text(message, parse_mode="Markdown")

async def help(update, context:ContextTypes.DEFAULT_TYPE):
    tele_id = update.effective_chat.id
    print(f"Message from {tele_id} = (Help) user is asking for help")

    message = (
        "Berikut adalah daftar perintah yang tersedia:\n\n"
        "`/start` \n- Memulai bot dan menampilkan menu utama\n"
        "`/show` \n- Menampilkan daftar transaksi yang telah tercatat\n"
        "`/add` \n- Menambahkan transaksi baru (fitur dalam pengembangan)\n"
        "`/help` \n- Menampilkan bantuan\n"
    )
    await update.message.reply_text(message, parse_mode="Markdown")

async def error_handler(update, context:ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")
    if update and hasattr(update, 'message') and update.message:
        try:
            await update.message.reply_text("Terjadi kesalahan pada bot. Silakan coba lagi nanti.", parse_mode="Markdown")
        except Exception:
            pass


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("show", show_transaction))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(form_input_transaction)

    app.add_error_handler(error_handler)
    print("Bot is already running...")

    app.run_polling()


if __name__ == "__main__":
    main()