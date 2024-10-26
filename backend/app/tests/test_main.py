import pytest
from httpx import AsyncClient
from app.main import app
from unittest.mock import AsyncMock
import databases

# Mock database instance globally
@pytest.fixture(autouse=True)
def mock_database(monkeypatch):
    # Mock the database connection functions to avoid real DB connection
    mock_db = AsyncMock(spec=databases.Database)
    monkeypatch.setattr("app.services.produit_service.database", mock_db)
    return mock_db

@pytest.mark.asyncio
async def test_create_produit(monkeypatch):
    async def mock_creer_produit(*args, **kwargs):
        return None  # Simulate success

    monkeypatch.setattr("app.services.produit_service.creer_produit", mock_creer_produit)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        produit_data = {
            "nom": "Produit Test",
            "reference": "REF123",
            "description": "Description du produit",
            "image": "http://example.com/image.png",
            "stock": 10
        }
        response = await ac.post("/produits/", json=produit_data)
    assert response.status_code == 200
