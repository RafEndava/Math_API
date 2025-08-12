## 📘 README.md
# 📐 Math Service API

Microserviciu Python scris cu **FastAPI** ce oferă operații matematice de bază:
- Putere (`a^b`)
- Fibonacci (`n`-lea număr)
- Factorial (`n!`)

Operațiile sunt salvate în:
- 🔸 Bază de date SQLite (`operations.db`)
- 🔸 Fișier CSV (`stream_log.csv`) — simulare mesaj streaming
- 🔸 Fișier log (`app.log`) — pentru tracking și debugging


## 🚀 Cum rulezi local (fără Docker)

### 1. Creează un mediu virtual:
python -m venv .venv
.venv\Scripts\activate


### 2. Instalează dependențele:
pip install -r requirements.txt


### 3. Rulează aplicația:
uvicorn main:app --reload


### 4. Accesează Swagger UI:
- [http://localhost:8000/docs](http://localhost:8000/docs)

### 5. Autentificare:
- Click pe butonul **Authorize** în Swagger UI
- Introdu în câmpul Header:

X-API-Key: secret123


## 🐳 Cum rulezi cu Docker

### 1. Build imaginea:

docker build -t math-api .


### 2. Rulează containerul:

docker run -p 8000:8000 math-api


### 3. Accesează interfața API:
- [http://localhost:8000/docs](http://localhost:8000/docs)


## 📬 Endpointuri disponibile

| Metodă | Endpoint      | Descriere                        |
|--------|---------------|----------------------------------|
| POST   | /pow          | `a^b`                            |
| POST   | /fibonacci    | n-lea număr din șirul Fibonacci |
| POST   | /factorial    | Factorialul unui număr          |
| GET    | /history      | Istoric operații efectuate       |


## 🧪 Testare automată

### 1. Instalează `pytest` dacă nu este deja:
pip install pytest httpx


### 2. Rulează testele:

pytest


### 3. Verifică rezultatul:

tests/test_api.py ....                               


## ✅ Exemple cereri API

### POST `/pow`
```json
{
  "a": 2,
  "b": 8
}
```

### POST `/fibonacci`
```json
{
  "a": 10
}
```

### POST `/factorial`
```json
{
  "a": 5
}
```

### GET `/history`
- returnează listă cu toate operațiile anterioare

