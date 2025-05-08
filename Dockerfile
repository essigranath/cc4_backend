# Käytä Python 3.12 slim -pohjaa
FROM python:3.12-slim

# Määrittele ympäristömuuttujat
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Luo työhakemisto konttiin
WORKDIR /app

# Kopioi vaadittavat tiedostot konttiin
COPY requirements.txt .

# Asenna riippuvuudet
RUN pip install --upgrade pip && pip install -r requirements.txt

# Kopioi koko projektin sisältö konttiin
COPY . .

# Määrittele portti, jota palvelin käyttää
EXPOSE 8000

# Määrittele oletuskäynnistyskomento
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]