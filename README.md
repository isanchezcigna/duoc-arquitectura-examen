commandos para configurar:

$ python3 -m venv myvenv
$ source myvenv/bin/activate


Ambiente desarrollo local:
- Crear ambiente virtual:
    python.exe -m virtualenv venv
- Activar el ambiente virtual, buscando el script correspondiente según consola: 
    \venv\Scripts\
    ./venv/Scripts/Activate.ps1
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

- Borrar BD
    python manage.py sqlflush
    borrar archivos: migrations/* a excepción de init py y 0001_initial

Si da error porque tabla existe:
    python manage.py migrate --fake




CONECTAR A HEROKU:

1) npm i -g heroku
2) heroku login
3) heroku plugins:install heroku-connect-plugin
4) heroku git:remote -a nombreapp