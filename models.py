# models é o arquivo onde fica as classes (tabelas)
# instalar = pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

engine = create_engine("sqlite:///escola.db")

Session = sessionmaker(bind=engine)

#Tabelas Curso e aluno (1:N)
class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False) = Column(Integer, nullable=False)

    alunos = relationship("Aluno", back_populates="cursos")


    def __repr__(self):
        return f"curso = id {self.id} - nome: {self.nome} - carga horaria: {self.cargo_horaria}"
    
class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"Aluno = id: {self.id} - nome: {self.nome} - Email: {self.email}"
    
    curso_id = Column(Integer, ForeignKey("cursos.id"))

    cursos = relationship("curso", back_populates="alunos")

    def __repr__(self):
        return f"Aluno = id: {self.id} - nome: {self.nome} - email: {self.email}"