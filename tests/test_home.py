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


TEST_UID = "5215fbdd756359"
ENC_UID = "d91dca601be6e377d585277bc1022b8040b79393d07747"


@pytest.mark.asyncio
async def test_check():
    await nc.app.start()
    client = TestClient(nc.app)
    response = await client.get(f"/{ENC_UID}")
    assert response.status == 200
    uid = nc.normalize_uid(TEST_UID)
    assert uid in await response.text()
