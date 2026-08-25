from database import engine
    

def test_connection():
    try:
        # Tenta abrir uma conexão rápida com o banco
        with engine.connect() as connection:
            print("Successfully connected to the pgAdmin PostgreSQL database!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

if __name__ == "__main__":
    test_connection()