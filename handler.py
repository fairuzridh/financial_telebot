from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
from state_handler_input import CATEGORY, DESCRIPTION, NOMINAL, INSTRUMENT, NOTE
from mapping_trans import category_mapping


async def start(update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Silakan pilih kategori transaksi yang ingin Anda catat.", 
        reply_markup=ReplyKeyboardMarkup(category_mapping, one_time_keyboard=True))
    return CATEGORY

async def get_category(update, context:ContextTypes.DEFAULT_TYPE):
    category = update.message.text
    context.user_data['category'] = category
    print(f"Selected category: {category}")

    await update.message.reply_text("Masukkan deskripsi transaksi:")
    return DESCRIPTION

async def get_description(update, context:ContextTypes.DEFAULT_TYPE):
    description = update.message.text
    context.user_data['description'] = description
    print(f"Entered description: {description}")

    await update.message.reply_text("Masukkan nominal transaksi:")
    return NOMINAL

async def get_nominal(update, context:ContextTypes.DEFAULT_TYPE):
    nominal = update.message.text
    context.user_data['nominal'] = nominal
    print(f"Entered nominal: {nominal}")

    await update.message.reply_text("Pilih instrumen transaksi:")
    return INSTRUMENT

async def get_instrument(update, context:ContextTypes.DEFAULT_TYPE):
    instrument = update.message.text
    context.user_data['instrument'] = instrument
    print(f"Selected instrument: {instrument}")

    await update.message.reply_text("Masukkan catatan tambahan (opsional):")
    return NOTE

async def get_note(update, context:ContextTypes.DEFAULT_TYPE):
    note = update.message.text
    context.user_data['note'] = note
    print(f"Entered note: {note}")
    print(f"Collected data: {context.user_data}")

    # Simpan transaksi ke database atau lakukan tindakan lain sesuai kebutuhan
    await update.message.reply_text("Transaksi berhasil dicatat!")
    return ConversationHandler.END

async def confirm_transaction(update, context:ContextTypes.DEFAULT_TYPE):
    category = context.user_data.get('category')
    description = context.user_data.get('description')
    nominal = context.user_data.get('nominal')
    instrument = context.user_data.get('instrument')
    note = context.user_data.get('note')

    confirmation_message = (
        f"Apakah Anda yakin ingin mencatat transaksi berikut?\n\n"
        f"Kategori: {category}\n"
        f"Deskripsi: {description}\n"
        f"Nominal: {nominal}\n"
        f"Instrumen: {instrument}\n"
        f"Catatan: {note if note else 'Tidak ada catatan'}\n\n"
        "Ketik 'ya' untuk konfirmasi atau 'tidak' untuk membatalkan."
    )

    if context.user_data.get('confirmation') == 'ya':
        # Simpan transaksi ke database atau lakukan tindakan lain sesuai kebutuhan
        await update.message.reply_text("Transaksi berhasil dicatat!")
        return ConversationHandler.END
    else:
        cancel_message = "Pencatatan transaksi dibatalkan."
        await update.message.reply_text(cancel_message)
        # return 
    await update.message.reply_text(confirmation_message)
    return NOTE

async def cancel(update, context:ContextTypes.DEFAULT_TYPE):
    print(context.user_data)
    await update.message.reply_text("Pencatatan transaksi dibatalkan.")
    return ConversationHandler.END


form_input_transaction = ConversationHandler(
    entry_points=[CommandHandler('add', start)],
    states={
        CATEGORY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_category)],
        DESCRIPTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_description)],
        NOMINAL: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_nominal)],
        INSTRUMENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_instrument)],
        NOTE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_note)]
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)