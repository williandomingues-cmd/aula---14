# configurar alembic

# inicializar o alebic 

# no terminal:
# alembic init alembic
# ou
# python -m alembic init alembic 
# Configurar a conexão com db
# -------------------------------------------------------
# Abra o arquivo: alembic.ini
# Procure pela linha:
# sqlalchemy.url = driver://user:pass@localhost/dbname

# Altere para a conexão com o seu banco
# sqlalchemy.url = sqlite:///escola.db


# Conectando o alembic ao sqlalchemy
# -------------------------------------------------------
# abra o arquivo: alembic/env.py
# importe o base do seu projeto. exemplo:
# from models import Base

# depois, encotre a linha:
# target_metadata = none
# e alterar para:
# target_metadata = Base.metadata

# criando a migração 
# -------------------------------------------------------
# no terminal:
# python -m alembic revision --autogenerate -m "criando tabelas"
# e depois aplica a migração no banco
# no terminal:
# python -m alembic upgrade head

# As tabelas foram criadas no banco de dados 