# entrar em um virutal env

```
source myenv/bin/activate
```

# criar um usuario

```
python manage.py createsuperuser
```

# banco postgres

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sistema',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
}

```

# banco - sqlite

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

# migrations

```
## 1. Criar migrations (quando você altera os models)
python manage.py makemigrations

## 2. Aplicar migrations (executar no banco)
python manage.py migrate
```

## uso do sqlite

```
# Navegar até a pasta do projeto Django
cd /caminho/do/seu/projeto

# Abrir o banco SQLite
sqlite3 db.sqlite3

-- Ver todas as tabelas
.tables

-- Ver estrutura de uma tabela
.schema nome_da_tabela

-- Fazer consultas SQL normais
SELECT * FROM auth_user;
SELECT * FROM seu_app_veiculo;

-- Sair
.quit

```

# insert de veiculo

```
INSERT INTO veiculo_veiculo  (marca, modelo, ano, cor, combustivel) VALUES
(1, 'Civic', 2020, 1, 1),
(1, 'City', 2021, 2, 1),
(1, 'HR-V', 2019, 3, 1),
(2, 'Corolla', 2022, 1, 1),
(2, 'Etios', 2018, 4, 1),
(2, 'Hilux', 2021, 5, 2),
(3, 'Onix', 2020, 2, 1);
```

# baixar postgres

```
sudo apt update && sudo apt install postgresql postgresql-contrib

sudo service postgresql start

sudo -u postgres psql

CREATE DATABASE sistema;
CREATE USER postgres WITH PASSWORD 'postgres';
ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE sistema TO postgres;

pip install psycopg2-binary

```
