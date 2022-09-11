# README.md를 꼭 읽어주세요!
URL = "(여기에 붙여넣으세요)"

import asyncio
from pyppeteer import launch
import requests

async def main():
    browser = await launch(headless=True,args=['--no-sandbox'],autoClose=False)
    page = await browser.newPage()
    await page.goto(URL)
    cdp = await page.target.createCDPSession()
    await cdp.send('Network.enable')
    # await cdp.send("Page.enable")
    
    def logAction(action):
        if (action["response"]["payloadData"] != "#pong"):
            # action["response"]["payloadData"] 가 후원의 정보입니다!
            print(action["response"]["payloadData"])
    cdp.on('Network.webSocketFrameReceived', logAction)
    print("ready")
    while True:
        await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())
