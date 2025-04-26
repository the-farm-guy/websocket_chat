import asyncio
from websockets.asyncio.server import serve
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

clients = {}
session = PromptSession()

async def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                await client.send(message)
                
            except:
                pass

async def handle_client(websocket):
    name = await websocket.recv()
    clients[websocket] = name
    print(f"{name} connected.")
    
    await broadcast(f"{name} has joined the chat!", sender=websocket)

    try:
        async for msg in websocket:
            full_message = f"[{name}]: {msg}"
            print(full_message)
            await broadcast(full_message, sender=websocket)
            
    except:
        pass
    
    finally:
        print(f"{name} disconnected.")
        del clients[websocket]
        await broadcast(f"{name} has left the chat.", sender=websocket)

async def server_input():
    with patch_stdout():
        while True:
            message = await session.prompt_async("Server: ")
            if message.lower() in {"exit", "quit"}:
                break
            
            elif not message.strip():
                print('can not send empty message')
            
            else:
                server_message = f"admin: {message}"
                # print(server_message)
                await broadcast(server_message)

async def main():
    server = await serve(handle_client, "0.0.0.0", 8765)
    print("Server started on 0.0.0.0:8765")
    
    await asyncio.gather(
        server_input(),
        asyncio.Future() 
    )

if __name__ == "__main__":
    asyncio.run(main())