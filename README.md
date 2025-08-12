## 📘 README.md
```markdown
# 📐 Math Service API

Microserviciu Python scris cu **FastAPI** ce oferă operații matematice de bază:
- Putere (`a^b`)
- Fibonacci (`n`-lea număr)
- Factorial (`n!`)

Operațiile sunt salvate în:
- 🔸 Bază de date SQLite (`operations.db`)
- 🔸 Fișier CSV (`stream_log.csv`) — simulare mesaj streaming
- 🔸 Fișier log (`app.log`) — pentru tracking și debugging

---

## 🚀 Cum rulezi local (fără Docker)

### 1. Creează un mediu virtual:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Instalează dependențele:
```bash
pip install -r requirements.txt
```

### 3. Rulează aplicația:
```bash
uvicorn main:app --reload
```

### 4. Accesează Swagger UI:
- [http://localhost:8000/docs](http://localhost:8000/docs)

### 5. Autentificare:
- Click pe butonul **Authorize** în Swagger UI
- Introdu în câmpul Header:
```
X-API-Key: secret123
```

---

## 🐳 Cum rulezi cu Docker

### 1. Build imaginea:
```bash
docker build -t math-api .
```

### 2. Rulează containerul:
```bash
docker run -p 8000:8000 math-api
```

### 3. Accesează interfața API:
- [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📬 Endpointuri disponibile

| Metodă | Endpoint      | Descriere                        |
|--------|---------------|----------------------------------|
| POST   | /pow          | `a^b`                            |
| POST   | /fibonacci    | n-lea număr din șirul Fibonacci |
| POST   | /factorial    | Factorialul unui număr          |
| GET    | /history      | Istoric operații efectuate       |

---

## 📦 Structura proiectului
```
math_service/
├── main.py              # aplicația FastAPI
├── api/routes.py        # endpointuri REST
├── core/calculator.py   # funcții matematice + cache
├── models/schemas.py    # validare input/output
├── db/database.py       # conexiune SQLite
├── services/
│   ├── recorder.py      # salvare operații + CSV
│   ├── logger.py        # sistem logging
├── tests/test_api.py    # testare automatizată
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🔒 Funcționalități avansate

- ✅ `@lru_cache` pentru `fibonacci` și `factorial`
- ✅ Logare în consolă + `app.log`
- ✅ Simulare trimitere mesaje (CSV + log `[STREAMING]`)
- ✅ Monitorizare: log timpi răspuns + status code
- ✅ Autentificare cu header `X-API-Key`
- ✅ Testare automată (`pytest` + `httpx`)

---

## 🧪 Testare automată

### 1. Instalează `pytest` dacă nu este deja:
```bash
pip install pytest httpx
```

### 2. Rulează testele:
```bash
pytest
```

### 3. Verifică rezultatul:
```
===================== test session starts =====================
tests/test_api.py ....                                [100%]
```

---

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

---

## 🧑‍💻 Creat cu ❤️ pentru evaluare Python Microservices
```
