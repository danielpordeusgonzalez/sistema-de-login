from Models import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib


def RetornaSession(): ##coloca a connection com o banco de dados em uma classe
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "sistema_de_login"
    PORT = "3306"
    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True) ##a engine cria todas as funções que podem ser utilizada tipo o add
    Session = sessionmaker(bind=engine) ##tem que pesquisar mas acho que faz a conexão com a engine
    return Session()

session = RetornaSession()

class ControllerCadastro():
    
    @classmethod
    def hash_senha(cls, senha):
        # Gerar o hash da senha usando SHA-256
        hash_obj = hashlib.sha256(senha.encode('utf-8'))
        return hash_obj.hexdigest()  # Retorna a senha codificada como uma string hexadecimal
    
    @classmethod
    def verificacao_cadastro(cls, nome, email, senha):
        if len(nome) == 0 or len(nome) < 3:
            raise ValueError("Campo vazio ou menor que 3 caracteres, insira um valor válido")
        if len(email) == 0:
            raise ValueError("Campo vazio, insira um valor válido")
        if len(senha) == 0 or len(senha) < 8:
            raise ValueError("Campo vazio ou menor que 8 caracteres, insira um valor válido")
        
        email_existente = session.query(Pessoa).filter_by(email = email).first()
        if email_existente:
            raise ValueError("E-mail já cadastrado. Insira um e-mail diferente.")
        
        return True
    
    @classmethod
    def cadastro(cls, nome, email, senha):
        
        try:
            cls.verificacao_cadastro(nome, email, senha)

            #senha codificada
            senha_codificada = cls.hash_senha(senha)
            
            novo_usuario = Pessoa(nome=nome, email=email, senha=senha_codificada)
            session.add(novo_usuario)
            
            session.commit()
            print("usuario cadastrado com sucesso")
          
        except Exception as e:
            session.rollback() 
            print(f"Erro ao cadastrar usuário: {e}")
        

    
# try: ##uma forma de cadastrar e capturar seus erros
#     ControllerCadastro.cadastro(nome="daniel", email="daniel@daniel.com", senha="danieldaniel")
# except ValueError as e:
#     print(f"Erro na validação: {e}")


class ControllerLogin():
    @classmethod
    def verificacao_login(cls, email, senha):
        usuario = session.query(Pessoa).filter_by(email=email).first()
        if not usuario:
            raise ValueError("E-mail não encontrado. Digite um e-mail válido.")
            
        senha_codificada = ControllerCadastro.hash_senha(senha)
        if usuario.senha != senha_codificada:
            raise ValueError("Senha incorreta. Tente novamente.")
            
        return usuario
    
    @classmethod
    def login(cls, email, senha):
        try:
            usuario = cls.verificacao_login(email, senha)
            print(f"Bem-vindo, {usuario.nome}! Login efetuado com sucesso.")
            return usuario
            
        except ValueError as e:
            print(f"Erro no login: {e}")
            return None
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None

