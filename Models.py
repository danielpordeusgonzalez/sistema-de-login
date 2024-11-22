from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "sistema_de_login"
PORT = "3306"

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CONN, echo=True) 
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base() ##faz toda a conexão

# class Cadastro:
#     def __init__(self, nome, email, senha):
#         self.nome = nome
#         self.email = email
#         self.senha = senha

# class Cadastro(Base): 
#     __tablename__ = "cadastro" 
#     id = Column(Integer, primary_key=True) 
#     nome = Column(String(50))
#     email = Column(String(40))
#     senha = Column(String(20))


# class Login:
#     def __init__(self, email, senha):
#         self.email = email
#         self.senha = senha
        
# class Login(Base): 
#     __tablename__ = "login" 
#     id = Column(Integer, primary_key=True) 
#     email = Column(String(40))
#     senha = Column(String(20))

class Pessoa(Base):
    __tablename__ = "pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(200))
    senha = Column(String(100))
    
    
Base.metadata.create_all(engine)