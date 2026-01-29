import asyncio
import socket

import websockets


async def main():
    host = "echo.websocket.events"
    url = f"wss://{host}"

    # 打印 Python 实际解析到的地址（关键诊断）
    try:
        infos = socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)
        addrs = sorted({sockaddr[0] for *_, sockaddr in infos})
        print("getaddrinfo OK:", addrs)
    except socket.gaierror as e:
        print("getaddrinfo FAILED:", repr(e))
        raise

    async with websockets.connect(url) as ws:
        await ws.send("hello websocket")
        msg = await ws.recv()
        print("recv:", msg)


if __name__ == "__main__":
    asyncio.run(main())