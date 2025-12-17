from sqlalchemy import Column,Integer,String ,DateTime,func
from sqlalchemy.orm import relationship
from api_app.database import Base


class USERS(Base) :
    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password_hash = Column(String, nullable=False)
    createdat = Column(DateTime,default=func.now())

    # Tous les logs de cet utilisateur
    predictions = relationship("PredictionHistory", back_populates="user")