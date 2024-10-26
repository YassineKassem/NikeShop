# backend/tests/test_main.py
import pytest
from httpx import AsyncClient
from app.main import app
from app.models.produit_model import Produit

@pytest.mark.asyncio
async def test_create_produit():
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
    assert response.json() == {"message": "Produit créé avec succès"}

@pytest.mark.asyncio
async def test_get_produits():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/produits/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_produit_by_id():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        produit_id = 1  # Example ID, replace with a valid one if needed
        response = await ac.get(f"/produits/{produit_id}")
    assert response.status_code == 200 or response.status_code == 404

@pytest.mark.asyncio
async def test_update_produit():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        produit_id = 1  # Example ID, replace with a valid one if needed
        updated_data = {
            "nom": "Produit Mis à jour",
            "reference": "REF124",
            "description": "Description mise à jour",
            "image": "http://example.com/image-updated.png",
            "stock": 20
        }
        response = await ac.put(f"/produits/{produit_id}", json=updated_data)
    assert response.status_code == 200 or response.status_code == 404

@pytest.mark.asyncio
async def test_delete_produit():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        produit_id = 1  # Example ID, replace with a valid one if needed
        response = await ac.delete(f"/produits/{produit_id}")
    assert response.status_code == 200 or response.status_code == 404
