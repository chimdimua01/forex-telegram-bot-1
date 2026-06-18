from telegram.ext import Application, MessageHandler, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

LINK_EXNESS = "https://one.exnessonelink.com/a/4lhbhlsedv"
REF_EXNESS = "4lhbhlsedv"

LINK_VANTAGE = "https://vigco.co/la-com-inv/vi/r4XceuuV"
REF_VANTAGE = "r4XceuuV"

ADMIN = "@TradeZenQMT"

KEYWORDS = [
    "link", "xin link", "đăng ký", "dang ky",
    "backcom", "back com", "hoàn phí", "hoan phi",
    "exness", "vantage", "ref", "mã ref", "ma ref",
    "mở tài khoản", "mo tai khoan", "copy trade", "copy"
]

async def auto_reply(update, context):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    if any(keyword in text for keyword in KEYWORDS):
        message = (
            "📌 CHƯƠNG TRÌNH HOÀN PHÍ GIAO DỊCH TỰ ĐỘNG\n\n"
            "Khi giao dịch sàn Exness hoặc Vantage, để tối ưu lợi nhuận tốt hơn, "
            "team có hỗ trợ chương trình Backcom/Hoàn phí giao dịch tự động cho member đăng ký qua link nhóm.\n\n"
            "✅ Backcom sàn Exness:\n"
            f"{LINK_EXNESS}\n"
            f"Mã Ref: {REF_EXNESS}\n\n"
            "✅ Backcom sàn Vantage:\n"
            f"{LINK_VANTAGE}\n"
            f"Mã đối tác: {REF_VANTAGE}\n\n"
            f"Mọi thông tin chi tiết liên hệ Admin: {ADMIN}"
        )

        await update.message.reply_text(message)

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN chưa được cài trong Render Environment")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("BOT DANG CHAY...")
    app.run_polling()

if __name__ == "__main__":
    main()
