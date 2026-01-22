import asyncio
import websockets

async def main():
    url = "wss://echo.websocket.events"
    async with websockets.connect(url) as ws:
        await ws.send("hello websocket")
        msg = await ws.recv()
        print("recv:", msg)

if __name__ == "__main__":
    asyncio.run(main())