from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.ws_manager import ConnectionManager

router = APIRouter()

# Create an instance of the connection manager
manager = ConnectionManager()

@router.websocket("/ws/fraud")
async def fraud_websocket(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Here, we just keep the connection open. You could also process incoming messages if needed.
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
