import os
from databases import Database 
from dotenv import load_dotenv 

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Obtenir l'URL de la base de données depuis la variable d'environnement
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres.uoypxcmqbgbicrowjika:KASSEMntpt33@aws-0-eu-west-3.pooler.supabase.com:6543/postgres")

# Créer une instance de la base de données
database = Database(DATABASE_URL)
