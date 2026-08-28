# Cria o ambiente virtual e instala as dependências do pyproject.toml
poetry install

# Ativa o ambiente virtual
poetry shell

# Configurar .env
cp .env.example .env

# Rodar as migrações até a versão mais recente
poetry run alembic upgrade head

#rodar docs do fastapi
cd /app
poetry run fastapi dev main.py
