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

@pytest.mark.asyncio
async def test_get_produits(monkeypatch):
    async def mock_obtenir_produits(*args, **kwargs):
        return []  # Simulate an empty list response

    monkeypatch.setattr("app.services.produit_service.obtenir_produits", mock_obtenir_produits)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/produits/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Check if the response is a list

@pytest.mark.asyncio
async def test_get_produit_by_id(monkeypatch):
    async def mock_obtenir_produit_par_id(*args, **kwargs):
        return {"nom": "Produit Test", "reference": "REF123"}  # Simulate a product response

    monkeypatch.setattr("app.services.produit_service.obtenir_produit_par_id", mock_obtenir_produit_par_id)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        produit_id = 1
        response = await ac.get(f"/produits/{produit_id}")
    assert response.status_code == 200
    assert response.json() == {"nom": "Produit Test", "reference": "REF123"}

@pytest.mark.asyncio
async def test_update_produit(monkeypatch):
    async def mock_mettre_a_jour_produit(*args, **kwargs):
        return None  # Simulate success

    monkeypatch.setattr("app.services.produit_service.mettre_a_jour_produit", mock_mettre_a_jour_produit)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        produit_id = 1
        updated_data = {
            "nom": "Produit Mis à jour",
            "reference": "REF124",
            "description": "Description mise à jour",
            "image": "http://example.com/image-updated.png",
            "stock": 20
        }
        response = await ac.put(f"/produits/{produit_id}", json=updated_data)
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_delete_produit(monkeypatch):
    async def mock_supprimer_produit(*args, **kwargs):
        return None  # Simulate success

    monkeypatch.setattr("app.services.produit_service.supprimer_produit", mock_supprimer_produit)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        produit_id = 1
        response = await ac.delete(f"/produits/{produit_id}")
    assert response.status_code == 200
