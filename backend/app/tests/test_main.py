# backend/tests/test_main.py

import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_hybridaction():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/hybridaction/zybTrackerStatisticsAction")
    assert response.status_code == 200
    assert response.json() == {"message": "Cette route est gérée maintenant."}
