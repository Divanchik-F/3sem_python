from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import aiohttp
from bs4 import BeautifulSoup
from random import randint

link_start = 'https://www.google.com/search?q='
link_end = '&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiMtMmd_av7AhWRvosKHa-ECi8Q_AUoAXoECAIQAw&biw=1161&bih=726&dpr=2'
secret_token = '5612247104:AAFE3rAKpLaXavIBI18DJo5PUu50zxVcCdw'  
bot = Bot(token=secret_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm Image bot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply("Let's find your image!")
    text = message.text
    print(text)
    async with aiohttp.ClientSession() as session:
        url = link_start + text + link_end
        async with session.get(url) as ans:
            if ans.status == 200:
                html = await ans.text()
                page = BeautifulSoup(html, 'lxml')
                imgs = page.select('img[src]')
                try:
                    img_url = imgs[0]['src']
                    await bot.send_photo(message.chat.id, photo=img_url)
                except IndexError:
                    await message.reply('No images found!')
            else:
                await message.reply("Can't connect to url with images!")


if __name__ == '__main__':
    executor.start_polling(dp)
