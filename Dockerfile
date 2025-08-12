# Folosește o imagine de bază cu Python
FROM python:3.11-slim

# Setează directorul de lucru în container
WORKDIR /app

# Copiază fișierele locale în container
COPY . .

# Instalează dependențele din requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Creează baza de date dacă nu există (opțional)
# RUN python -c "from db.database import init_db; init_db()"

# Expune portul aplicației
EXPOSE 8000

# Comanda de start a aplicației
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
