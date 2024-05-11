from fastapi import FastAPI
import socketio

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = FastAPI()
app.mount("/", socketio.ASGIApp(sio))

@sio.event
async def connect(sid, environ):
    print('connect ', sid)

@sio.event
async def chat_message(sid, data):
    print('message ', data)
    await sio.emit('reply', {'data': f"Message received: {data}"}, room=sid)

@sio.event
async def disconnect(sid):
    print('disconnect ', sid)
