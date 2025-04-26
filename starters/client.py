import asyncio
from websockets.asyncio.client import connect

async def hello():
    # async with connect("ws://192.168.1.22:8765") as client:
    async with connect("ws://localhost:8765") as client:
        while True:
            message = input("input : ")
            
            if message.lower() in {"exit", "quit"}:
                print("Exiting...")
                break
            
            await client.send(message)
            reply = await client.recv()
            print(f'server : {reply}')
        
if __name__ == "__main__":
    asyncio.run(hello())