import logging
import pytest
import websockets
import pytest_asyncio
from websockets.protocol import State

@pytest_asyncio.fixture
async def websocket_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        yield websocket

@pytest.mark.asyncio
async def test_websocket_connection(websocket_client):
    assert websocket_client.state is State.OPEN
    if websocket_client.state is open():
        logging.info("Cliente enviando: OK")
        await websocket_client.send("OK")

@pytest.mark.asyncio
async def test_websocket_send_and_receive(websocket_client):
    message = "HELLO, WEBSOCKET!"
    await websocket_client.send(message)
    response = await websocket_client.recv()
    logging.info("CLIENTE RECEBEU: %s ", message)
    assert response == message

@pytest.mark.asyncio
async def test_websocket_close(websocket_client):
    await websocket_client.close()
    assert websocket_client.state is State.CLOSED

    