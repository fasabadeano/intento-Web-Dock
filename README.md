Deber seguir el siguienttipo de comandos en orden cronologico:
python -m venv env : para crear el entorno virtual 
env\Scripts\activate : para activar el entorno virtual
pip install flask requests : para instalar flask
docker build -t imagga-webapp . : para crear la imagen dentro del docker
docker run -p 5000:5000 imagga-webapp : levantar la imagen creada del docker

De igual maner se debe cambiar en el archivo app.py en la parte de IMAGGA_API_KEY
y de igual manera en IMAGGA_API_SECRET, con los codigos optenidos en la pagina de
immaga.com
