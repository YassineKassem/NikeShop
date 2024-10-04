from pydantic import BaseModel 
class Produit(BaseModel):
    nom: str
    reference: str
    description: str
    image: str  
    stock: int
