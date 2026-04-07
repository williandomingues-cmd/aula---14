# configurar alembic

# inicializar o alibic 

# no terminal:
# alembic init alembic
# ou
# python -m alembic init alembic p
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
# from models import base

# depois, encotre a linha:
# target_metadata = none
# e alterar para:
# target_metadata = base.metadata