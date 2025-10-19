from pyvkbot import Bot
from pyvkbot import Keyboard
from config import TOKEN, GROUP_ID

bot = Bot(token=TOKEN, group_id=GROUP_ID)


@bot.message("Hello")
def hello(bot: Bot, message: dict[str, int]):
    bot.send_message(peer_id=message["peer_id"], text="Hello, World")


bot.start_polling(lambda: print("Bot Started"))
