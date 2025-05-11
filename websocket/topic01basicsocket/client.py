import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    print("📡 Conectando al servidor...")
    async with websockets.connect(uri) as websocket:
        print("✅ Conectado, enviando mensaje...")
        await websocket.send("Hola servidor")
        print("📨 Esperando respuesta...")
        respuesta = await websocket.recv()
        print(f"🎉 Respuesta del servidor: {respuesta}")

asyncio.run(hello())
