import asyncio
from websockets.asyncio.client import connect
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

session = PromptSession()

async def chat():
    name = input("Enter your name: ")

    async with connect("ws://192.168.1.25:8765") as websocket:
        await websocket.send(name)  

        async def receive_messages():
            while True:
                message = await websocket.recv()
                print(f"\n{message}")

        async def send_messages():
            with patch_stdout():
                while True:
                    message = await session.prompt_async("You: ")
                    if message.lower() in {"exit", "quit"}:
                        await websocket.close()
                        print("Disconnected.")
                        break
                    
                    elif message.strip():
                        print(message)
                        await websocket.send(message)
                    
                    else:
                        print('can not send empty message')
        await asyncio.gather(receive_messages(), send_messages())

if __name__ == "__main__":
    asyncio.run(chat())
