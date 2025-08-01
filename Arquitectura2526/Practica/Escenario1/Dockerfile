FROM python:3.9-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y gcc curl && apt-get clean

# Instalar Ray versión estable
#RUN pip install --no-cache-dir ray[default]==2.10.0
RUN pip install --no-cache-dir ray[default]==2.47.1

CMD ["bash", "-c", "ray start --head --dashboard-host 0.0.0.0 --include-dashboard true --block"]

