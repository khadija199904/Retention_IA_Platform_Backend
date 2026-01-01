import os 
from dotenv import load_dotenv

load_dotenv()
# utulise pour vercel
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    USER=os.getenv("POSTGRES_USER")
    PASSWORD=os.getenv("POSTGRES_PASSWORD","secret")
    HOST=os.getenv("POSTGRES_HOST", "db")
    PORT=os.getenv("POSTGRES_PORT")
    DB=os.getenv("POSTGRES_DB")

    
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

# Correction pour SQLAlchemy (cas où Supabase ou Vercel utilise postgres://)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)




 # Configuration de JWT
SECRET_KEY = os.getenv("SECRET_KEY")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")