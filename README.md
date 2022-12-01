commandos para configurar:

$ python3 -m venv myvenv
$ source myvenv/bin/activate


Ambiente desarrollo local:
- Crear ambiente virtual:
    python.exe -m virtualenv venv
- Activar el ambiente virtual, buscando el script correspondiente según consola: 
    \venv\Scripts\
- Correr el comando:
    pip install -r requirements.txt
- Iniciar tipeando: 
    python.exe .\manage.py runserver


De agregar otras librerias, debes refrescar el archivo requeriments.txt:
    pip freeze > requirements.txt



PASO A PASO:

- Subir modelo a BD:
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser