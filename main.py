import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# إعداداتك الخاصة
TOKEN = "7336582531:AAEU6Lp9Z7tP9pZIn2o3yC51H-i7vJnd7j8"
ADMIN_ID = 5664150532

# إعداد السجلات
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# دالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("🔍 فحص يوزر", callback_data="check_user")],
        [InlineKeyboardButton("💎 اشتراك شهري", callback_data="subscribe")],
        [InlineKeyboardButton("📊 الإحصائيات", callback_data="stats")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"هلا بيك {user.first_name} ببوت الفحص الصاروخي! 🚀\n\nإختار شتريد تسوي من القائمة جوة 👇",
        reply_markup=reply_markup
    )
    
    if user.id != ADMIN_ID:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🔔 مستخدم جديد دخل للبوت:\nالاسم: {user.first_name}\nاليوزر: @{user.username}\nالآيدي: {user.id}"
        )

# دالة الأزرار
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "stats":
        await query.edit_message_text(text="📊 الإحصائيات قيد التحديث...")
    elif query.data == "subscribe":
        await query.edit_message_text(text="💳 ميزة الاشتراك ستتوفر قريباً.")
    elif query.data == "check_user":
        await query.edit_message_text(text="🔎 أرسل اليوزر للفحص...")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_
