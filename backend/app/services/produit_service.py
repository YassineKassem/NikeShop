from app.config.db import database

async def creer_produit(nom: str, reference: str, description: str, image: str, stock: int):
    query = """
    INSERT INTO produit (nom, reference, description, image, stock)
    VALUES (:nom, :reference, :description, :image, :stock)
    """
    await database.execute(query, values={"nom": nom, "reference": reference, "description": description, "image": image, "stock": stock})

async def obtenir_produits():
    query = "SELECT * FROM produit"
    return await database.fetch_all(query)

async def obtenir_produit_par_id(produit_id: int):
    query = "SELECT * FROM produit WHERE id = :produit_id"
    return await database.fetch_one(query, values={"produit_id": produit_id})
async def mettre_a_jour_produit(produit_id: int, nom: str, reference: str, description: str, image: str, stock: int):
    query = """
    UPDATE produit
    SET nom = :nom, reference = :reference, description = :description, image = :image, stock = :stock
    WHERE id = :produit_id
    """
    await database.execute(query, values={
        "produit_id": produit_id,
        "nom": nom,
        "reference": reference,
        "description": description,
        "image": image,
        "stock": stock
    })
async def supprimer_produit(produit_id: int):
    query = "DELETE FROM produit WHERE id = :produit_id"
    await database.execute(query, values={"produit_id": produit_id})
