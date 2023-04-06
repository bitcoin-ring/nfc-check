import pytest
from blacksheep.testing import TestClient
import nfc_check as nc


@pytest.mark.asyncio
async def test_home():
    await nc.app.start()
    client = TestClient(nc.app)
    response = await client.get("/")
    assert response.status == 200
    text = await response.text()
    assert nc.conf.app_name in text


@pytest.mark.asyncio
async def test_logo():
    await nc.app.start()
    client = TestClient(nc.app)
    response = await client.get("/images/bolt-ring-logo.png")
    assert response.status == 200
    assert response.content_type() == b"image/png"
