import re
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, MessageHandler, ContextTypes, filters
)
from telegram.constants import ChatMemberStatus

# ដាក់ Token នៅទីនេះ (សុវត្ថិភាព: កុំបង្ហាញ Token សាធារណៈ)
TOKEN = "7204817778:AAEMYRDiqGzRf2PmEfDD0kL3_jb0tOiDMdc"

# --- Detect URL pattern (simple check) ---
URL_PATTERN = re.compile(r'https?://|www\.')

async def is_admin(update: Update, user_id: int) -> bool:
    if update.effective_chat.type not in ['group', 'supergroup']:
        return False
    try:
        member = await update.effective_chat.get_member(user_id)
        return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except Exception:
        return False

async def auto_delete_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    message = update.message
    user_id = message.from_user.id

    # Check if message contains link
    if URL_PATTERN.search(message.text):
        # Skip if sender is admin
        if await is_admin(update, user_id):
            return
        try:
            await message.delete()
        except Exception:
            pass

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), auto_delete_link))
    app.run_polling()
