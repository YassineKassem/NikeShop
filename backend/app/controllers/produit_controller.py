from app.models.produit_model import Produit
from fastapi import APIRouter, HTTPException 
from ..services.produit_service import (
    creer_produit, obtenir_produits, obtenir_produit_par_id,
    mettre_a_jour_produit, supprimer_produit
)

router = APIRouter()

@router.post("/produits/")
async def creer_produit_controller(produit: Produit):
    try:
        # Save product to the database (you can adjust this for your DB)
        await creer_produit(produit.nom, produit.reference, produit.description, produit.image, produit.stock)
        return {"message": "Produit créé avec succès"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/produits/")
async def obtenir_produits_controller():
    produits = await obtenir_produits()
    return produits

@router.get("/produits/{produit_id}")
async def obtenir_produit_par_id_controller(produit_id: int):
    produit = await obtenir_produit_par_id(produit_id)
    if produit is None:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return produit

@router.put("/produits/{produit_id}")
async def mettre_a_jour_produit_controller(produit_id: int, nom: str, reference: str, description: str, image: str, stock: int):
    await mettre_a_jour_produit(produit_id, nom, reference, description, image, stock)
    return {"message": "Produit mis à jour avec succès"}

@router.delete("/produits/{produit_id}")
async def supprimer_produit_controller(produit_id: int):
    await supprimer_produit(produit_id)
    return {"message": "Produit supprimé avec succès"}
