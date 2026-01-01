from sqlalchemy import create_engine,text
import os
from sqlalchemy.orm import sessionmaker,declarative_base
from .core.config import USER,PASSWORD,HOST,PORT,DB


DB_URL = os.getenv("DATABASE_URL")

if not DB_URL:
    # On s'assure que PORT n'est pas None pour éviter l'erreur de base 10
    safe_port = PORT if (PORT and str(PORT) != 'None') else "5432"
    DB_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{safe_port}/{DB}"





engine = create_engine (DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




# Test connection 
if __name__ == "__main__":
     
     # obtenir la session
     def get_db():
        db = SessionLocal()
        try:
             yield db
        finally:
          db.close()
     

     print(" Test de connexion à la base de données...")
     print(f"DB: {DB} | User: {USER} | Host: {HOST}:{PORT}")
     try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print(" Connexion réussie à la base de données !")
            print("DB_URL:", DB_URL)


     except Exception as e:
        print(" Échec de la connexion :", e)
     