from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class ProductModel(Base):
    __tablename__ = "products" # vai ser o nome da minha tabela
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    categoria = Column(String)
    email_fornecedor = Column(String)
    create_at = Column(DateTime(timezone=True), default=func.now())