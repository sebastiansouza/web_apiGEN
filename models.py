from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    foto = Column(String)

    # Relacionamento com as postagens (sem carregamento automático)
    postagens = relationship("Postagem", back_populates="autor", lazy='select')

class Postagem(Base):
    __tablename__ = 'postagem'

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    texto = Column(String)
    data = Column(DateTime)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    tema_id = Column(Integer, ForeignKey('tema.id'))

    # Relacionamento com o autor da postagem
    autor = relationship("User", back_populates="postagens")

class Tema(Base):
    __tablename__ = 'tema'

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)

    # Relacionamento com as postagens (sem carregamento automático)
    postagens = relationship("Postagem", back_populates="tema", lazy='select')
