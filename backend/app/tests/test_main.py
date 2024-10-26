import pytest
from httpx import AsyncClient
from app.main import app
from unittest.mock import AsyncMock

# Test for creating a product
@pytest.mark.asyncio
async def test_create_produit(mocker):
    # Mock the creer_produit function to simulate DB operation without Supabase
    mocker.patch("app.services.produit_service.creer_produit", new=AsyncMock(return_value=None))
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

# Test for retrieving products
@pytest.mark.asyncio
async def test_get_produits(mocker):
    # Mock obtenir_produits to simulate DB retrieval
    mocker.patch("app.services.produit_service.obtenir_produits", new=AsyncMock(return_value=[]))
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/produits/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test for retrieving a product by ID
@pytest.mark.asyncio
async def test_get_produit_by_id(mocker):
    # Mock obtenir_produit_par_id to return a test product or None
    mocker.patch("app.services.produit_service.obtenir_produit_par_id", new=AsyncMock(return_value=None))
    async with AsyncClient(app=app, base_url="http://test") as ac:
        produit_id = 1  # Example ID
        response = await ac.get(f"/produits/{produit_id}")
    assert response.status_code == 200 or response.status_code == 404

# Test for updating a product
@pytest.mark.asyncio
async def test_update_produit(mocker):
    # Mock mettre_a_jour_produit to simulate updating a product
    mocker.patch("app.services.produit_service.mettre_a_jour_produit", new=AsyncMock(return_value=None))
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
    assert response.status_code == 200 or response.status_code == 404

# Test for deleting a product
@pytest.mark.asyncio
async def test_delete_produit(mocker):
    # Mock supprimer_produit to simulate deleting a product
    mocker.patch("app.services.produit_service.supprimer_produit", new=AsyncMock(return_value=None))
    async with AsyncClient(app=app, base_url="http://test") as ac:
        produit_id = 1
        response = await ac.delete(f"/produits/{produit_id}")
    assert response.status_code == 200 or response.status_code == 404
