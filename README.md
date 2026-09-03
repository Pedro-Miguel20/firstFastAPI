## 🚀 Instalação e Execução

### 1. Instalar as dependências

O projeto utiliza **Poetry** para gerenciamento de dependências e ambiente virtual.

```bash
poetry install
```

### 2. Ativar o ambiente virtual

```bash
poetry shell
```

> 💡 Alternativamente, você pode executar comandos diretamente no ambiente virtual usando `poetry run`.

### 3. Configurar as variáveis de ambiente

Crie o arquivo `.env` a partir do exemplo fornecido:

```bash
cp .env.example .env
```

Depois, ajuste as variáveis de ambiente conforme necessário.

### 4. Executar as migrações

Aplique todas as migrações do banco de dados até a versão mais recente:

```bash
poetry run alembic upgrade head
```

### 5. Iniciar o servidor

Entre no diretório da aplicação:

```bash
cd /app
```

Inicie o servidor de desenvolvimento do **FastAPI**:

```bash
poetry run fastapi dev main.py
```

O servidor ficará disponível no endereço indicado pelo FastAPI.

### 📚 Documentação da API

Após iniciar o servidor, a documentação interativa da API pode ser acessada pelo **Swagger UI** em:

```text
/docs
```

E a documentação **ReDoc** em:

```text
/redoc
```

### ⚡ Resumo

Se o ambiente já estiver configurado, o fluxo básico é:

```bash
poetry install
poetry shell
cp .env.example .env
poetry run alembic upgrade head

cd /app
poetry run fastapi dev main.py
```

### Rodar Locust
```bash
cd /app
cd poetry run locust -f tests/locustfile.py
```
Depois basta apertar enter

### Rodar Locust na command line

```bash
poetry run locust -f locustfile.py \
  --host=http://ipserviço:port \
  --headless \
  -u 3000 \ # Numero de cliente virtuais
  -r 5 \ # numero de acesso por segundo de clientes
  --run-time 2m \ # duração do teste
  --csv=locust_report #arquivo de feedback
```
