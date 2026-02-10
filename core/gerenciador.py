from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.funcionario import Funcionario, Base

engine = create_engine('sqlite:///data/empresa.db')
Session = sessionmaker(bind=engine)

def inicializar_banco():
    Base.metadata.create_all(engine)

def salvar_funcionario(nome, cargo, setor, salario):
    session = Session()
    try:
        novo_func = Funcionario(nome=nome, cargo=cargo, setor=setor, salario=salario)
        session.add(novo_func)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e # repassa o erro para o main tratar
    finally:
        session.close()

def listar_funcionario():
    session = Session()
    lista = session.query(Funcionario).all()
    session.close()
    return lista

def buscar_funcionario_nome(nome_busca):
    session = Session()
    # Busca aproximada usando Like
    resultado = session.query(Funcionario).filter(Funcionario.nome.contains(nome_busca))
    session.close()
    return resultado
