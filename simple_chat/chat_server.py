import asyncio
from websockets.asyncio.server import serve
from aioconsole import ainput

async def handle_client(websocket):
    async def receive_message():
        async for message in websocket:
            print(f'\nclient: {message}')

    async def send_message():
        while True:
            message = await ainput("input : ")
            
            if message.strip():
                await websocket.send(message)
            
            else:
                print('can not send empty message')

    await asyncio.gather(receive_message(), send_message())

async def main():
    async with serve(handle_client, "0.0.0.0", 8765):
        print("Server started on 0.0.0.0:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
