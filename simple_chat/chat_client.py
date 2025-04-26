import asyncio
from websockets.asyncio.client import connect
from aioconsole import ainput 

async def handle_server():
    # async with connect("ws://localhost:8765") as client:
    async with connect("ws://192.168.1.25:8765") as client:
        async def receive_message():
            while True:
                message = await client.recv()
                print(f'\nserver: {message}')  
                
        async def send_message():
            while True:
                message = await ainput("input : ")
                
                if message.lower() in {"exit", "quit"}:
                    print("Exiting...")
                    await client.close()
                    break
                
                elif message.strip():
                    print(message)
                    await client.send(message)
                    
                else:
                    print('can not send empty message')

        await asyncio.gather(receive_message(), send_message())

if __name__ == "__main__":
    asyncio.run(handle_server())
