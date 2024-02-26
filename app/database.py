from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Substitua localhost pelo host onde seu banco de dados está hospedado
SQLALCHEMY_DATABASE_URL = "postgresql://apigendb:51jLntcxscckr2Fslx3tEeVpXx1i4W3s@dpg-cne9k3n109ks738ug4n0-a.oregon-postgres.render.com/apigen_4ylk"

# Criar uma instância de motor de banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Criar uma sessão de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar uma base para os modelos
Base = declarative_base()

# Método para conectar ao banco de dados
def connect():
    
    Base.metadata.create_all(bind=engine)


# Método para desconectar do banco de dados (opcional)
def disconnect():
    engine.dispose()

def create_tables():
    Base.metadata.create_all(bind=engine)