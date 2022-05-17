
from common.func import escape_telegram_char

async def send_escaped_message(self, user_id: int, message: types.message, **kwargs):
    await self.send_message(user_id, escape_telegram_char(message), **kwargs)
