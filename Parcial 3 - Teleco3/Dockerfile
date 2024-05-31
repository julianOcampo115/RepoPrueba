# Usa una imagen base oficial de Python 3.6
FROM python:3.8

# Expone el puerto en el que correrá la aplicación
EXPOSE 5000

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de la aplicación al directorio de trabajo
COPY . /app/
COPY run.py /app


# Instala las dependencias de Python
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Ejecuta la aplicación
CMD python run.py
