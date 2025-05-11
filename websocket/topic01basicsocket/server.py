import asyncio
import websockets

async def echo(websocket):
    try:
        async for message in websocket:
            print(f"Mensaje recibido: {message}")
            await websocket.send(f"Echo: {message}")
    except Exception as e:
        print(f"💥 Error en el servidor: {e}")


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("Servidor WebSocket corriendo en ws://localhost:8765")
        await asyncio.Future()  # Mantiene el servidor activo

asyncio.run(main())
