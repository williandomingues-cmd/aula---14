from models import Session, Curso, Aluno


#criar as funções do crud 
#função criar um curso com sqlalchemy:

def cadastrar_curso():
    with Session() as session:
        try:
            nome = input("Digite o nome do curso: ").capitalize()
            cargo_horaria = input("Digite a carga hóraria do curso: ")
            curso = Curso(nome=nome, cargo_horaria=cargo_horaria)
            session.add(curso)
            session.commit()
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro}")

cadastrar_curso()

#função criar um aluno com sqlalchemy:
