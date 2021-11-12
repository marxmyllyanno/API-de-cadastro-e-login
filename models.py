import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.schema import Column


CONN = "postgresql://postgres:1234@localhost:5432/projetofastapi"

engine = create_engine(CONN)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))

class Tokens(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('pessoa.id'))
    token = Column(String(100))
    data = Column(DateTime, default=datetime.datetime.utcnow())

Base.metadata.create_all(engine)
