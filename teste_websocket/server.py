import asyncio
import logging
import websockets

async def echo(websocket):
    async for message in websocket:
        logging.info("SERVIDOR RECEBEU: ", message)
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future() #RODA PRA SEMPRE

if __name__ == "__main__":
    asyncio.run(main())