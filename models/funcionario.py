from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = 'funcionario'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cargo = Column(String)
    setor = Column(String)
    salario = Column(Float)

    def __repr__(self):
        return f"<Funcionario(nome='{self.nome}', cargo='{self.cargo}')>"