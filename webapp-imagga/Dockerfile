# Usa una imagen base de Python ligera
FROM python:3.8-slim

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias necesarias
RUN pip install flask requests

# Expone el puerto 5000 (usado por Flask)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]