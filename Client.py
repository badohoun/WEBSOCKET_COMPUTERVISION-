# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:27:27 2020

@author: admin1
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 00:18:58 2020
@author: BADOHOUN
"""

# WS client example

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:9001"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())