
import asyncio
from pyppeteer import launch
import time
from dotenv import load_dotenv
import os

load_dotenv()
code = os.getenv("CODE")
import sys

print('hello world')
print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')

print('hello world')


async def main():
    browser = await launch(options={'args': ['--no-sandbox'], 'devtools':True, 'headless':True})
    page = await browser.newPage()
    await page.setViewport({ 'width': 800, 'height': 600 })
    # await page.goto('https://google.com')

    await page.goto('https://trinket.io/features/pygame')
    time.sleep(5)
    await page.keyboard.down('ControlLeft')
    await page.keyboard.press('KeyA')
    await page.keyboard.up('ControlLeft')
    # await page.screenshot({'path': './all.png'})
    time.sleep(1)
    await page.keyboard.type("import os; os.system({c});".format(c=sys.argv[1]))
    time.sleep(1)
#     await page.screenshot({'path': './trinket.png'})
    await page.mouse.click(780, 560, { 'button': 'left' })
    time.sleep(2)
    # await page.screenshot({'path': './click.png'})
    num = 10
    for x in range(num):
    #code
        time.sleep(10)
        await page.screenshot({'path': './res.png'})
        await page.keyboard.press('h')
        await page.keyboard.press('ArrowUp')
    
    print('stooop')
    print('stopp')

    print('stooop')
    print('stopp')
    print('stooop')
    print('stopp')
    print('stooop')
    print('stopp')


    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
