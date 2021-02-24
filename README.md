# BibliotecaEscolarARP

_Biblioteca Escolar del Colegio Tecnico Aldemar Rojas Plazas_

> Construido con Django

![BibliotecaEscolarARP](/static/img/IconBuhoWhite.png)

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

+ [Python3](https://www.python.org/download/releases/3.0/)
+ [Azure Blob Storage](https://azure.microsoft.com/es-es/services/storage/blobs/)
+ [Heroku](https://devcenter.heroku.com/articles/heroku-cli) _opcional_
+ [Postgresql](https://www.postgresql.org/) _Base de datos (opcional)_

```
sudo apt install python3 python3-pip python3-dev postgresql
```

### Instalacion de dependnecias 🔧

_es recomendable crear un entorno virtual para evitar errores de instalacion o conglictos entre dependencias_

```
$ pip3 install virtualenv
$ virtualenv env
$ source env/bin/activate
```

```
pip3 install -r requirements.txt
```
_se instalaran las siguientes dependencias_

+ [azure-common==1.1.26](https://pypi.org/project/azure-common/)
+ [azure-storage-blob==2.1.0](https://azure.microsoft.com/es-es/services/storage/blobs/)
+ [azure-storage-common==2.1.0](https://pypi.org/project/azure-storage-common/)
+ [asgiref==3.3.1](https://pypi.org/project/asgiref/)
+ [bleach==3.3.0](https://pypi.org/project/bleach/)
+ [dj-database-url==0.5.0](https://pypi.org/project/dj-database-url/)
+ [Django==3.1.6](https://pypi.org/project/Django/)
+ [django-dotenv==1.4.2](https://pypi.org/project/django-dotenv/)
+ [django-markdownify==0.8.2](https://pypi.org/project/django-markdownify/)
+ [django-markdownx==3.0.1](https://pypi.org/project/django-markdownx/)
+ [django-widget-tweaks==1.4.8](https://pypi.org/project/django-widget-tweaks/)
+ [django-storages==1.11.1](https://pypi.org/project/django-storages/)
+ [gunicorn==20.0.4](https://pypi.org/project/gunicorn/)
+ [Markdown==3.3.3](https://pypi.org/project/Markdown/)
+ [packaging==20.9](https://pypi.org/project/packaging/)
+ [Pillow==8.1.0](https://pypi.org/project/Pillow/)
+ [psycopg2==2.8.6](https://pypi.org/project/psycopg2/)
+ [pyparsing==2.4.7](https://pypi.org/project/pyparsing/)
+ [pytz==2021.1](https://pypi.org/project/pytz/)
+ [six==1.15.0](https://pypi.org/project/six/)
+ [sqlparse==0.4.1](https://pypi.org/project/sqlparse/)
+ [webencodings==0.5.1](https://pypi.org/project/webencodings/)
+ [whitenoise==5.2.0](https://pypi.org/project/whitenoise/)

## Configuracion ⚙️
_en la carpeta principal cre un archivo "**.env**" y coloca siguiente_

```
CODE = <CODIGO_PARA_PERMITIR_EL_REGISTRO_DE_USUARIOS_NUEVOS>
SECRET_KEY = <TU_SECRET_KEY>
ENGINE_DB = <TIPO_DE_BASE_DE_DATOS (Opcional en local o pruebas)>
NAME_DB = <NOMBRE_DE_LA_BASE_DE_DATOS (Opcional en local o pruebas)>
USER_DB = <USUARIO_DE_LA_BASE_DE_DATOS (Opcional en local o pruebas)>
PASSWORD_DB = <CONTRASEÑA_DE_LA_BASE_DE_DATOS (Opcional en local o pruebas)>
HOST_DB = <HOST_DE_LA_BASE_DE_DATOS (Opcional en local o pruebas)>
PORT_DB = <PUERTO_DE_LA_BASE_DE_DATOS (Opcional en local o pruebas)>
ACCOUNT_NAME_AZURE = <NOMBRE_DE_AZURE_BLOBS_STORAGE(Opcional en local o pruebas)>
ACCOUNT_KEY_AZURE = <CLAVE_KEY_DE_AZURE_BLOBS_STORAGE(Opcional en local o pruebas)>
```

_para mas informacion sobre la configuracion de la vase de datos [Click aqui](https://docs.djangoproject.com/es/3.1/ref/databases/)_

_para mas informacion acerca Azure Blobs Storage_
+ [Azure Storage Python](https://django-storages.readthedocs.io/en/latest/backends/azure.html)
+ [Azure Storage Service](https://azure.microsoft.com/es-es/services/storage/blobs/)

## Modo Local o Pruebas
_Entra a la carpeta Biblioteca y luego edita el archivo "**settings.py**"_

_Cambia la variable **DEBUG** por **True**_

```
....
DEBUG = True
....
```

_Comenta todo desde la linea **177**_

```
# Azure Storage
#DEFAULT_FILE_STORAGE = 'Biblioteca.custom_azure.AzureMediaStorage'
#STATICFILES_STORAGE = 'Biblioteca.custom_azure.AzureStaticStorage'

#STATIC_LOCATION = "static"
#MEDIA_LOCATION = "media"

#AZURE_ACCOUNT_NAME = os.getenv('ACCOUNT_NAME_AZURE')
#AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
#STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
#MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
```

### Opcional
_Cambia la parte de **DATABASES** por lo siguiente_

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

<!-- ## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
``` -->

## Despliegue 📦

> _**Advertencia**: Si hiciste los pasos de Modo local tienes que que revertir los pasos_

_Para el despliegue puedes usar cualquier servicio en la nube pero en este caso usaremos [Heroku](heroku.com)_

_para mas informacion detallada del despliege puedes ver este sitio_ 
* [Tutorial de Django Parte 11 - Mozilla](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Deployment)

_Instala [Heroku](heroku.com), en linux seria_

```
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
```

_Para crear la app ejecutamos el comando "**create**" en el directorio raíz de nuestro repositorio. Esta operación crea un git remoto ("puntero hacia el repositorio remoto") denominado heroku en nuestro entorno git local._

```
heroku create
```

> _**Nota**: Puedes nombrar el remoto, si lo deseas, especificando un valor después de "create". Si no, obtendrás un nombre aleatorio. Este nombre es el que se utiliza en la URL por defecto._

_Podemos a continuación "empujar" (push) nuestra aplicación hacia el respositorio Heroku como se muestra abajo. Este proceso subirá la aplicación, la empaquetará en un dyno, ejecutará collestatic, y arrancará el sitio._

```
git push heroku master
```

_Si tenemos suerte, la app ya estará "corriendo" en el sitio, pero no estará funcionando correctamente ya que no hemos colocado las tablas que usa nuestra aplicación. Para hacer esto necesitamos utilizar el comando heroku run y arrancar un "[one off dyno](https://devcenter.heroku.com/articles/deploying-python#one-off-dynos)" para realizar una operación de migración. Introduce el siguiente comando en el terminal:_

```
heroku run python manage.py migrate
```

_Vamos a necesitar también poder añadir libros y autores, así que vamos a crear nuestro superusuario de administración, de nuevo utilizando un "**one-off dyno**":_

```
heroku run python manage.py createsuperuser
```

_Una vez llevado a cabo ésto, podremos ver el sitio. Debería funcionar. Para abrir el navegador hacia el nuevo sitio web, usa el comando:_

```
heroku open
```

## Construido con 🛠️

_Tecnologias y Herramientas usadas_

* [Django](https://www.djangoproject.com/) - El framework web usado
* [Materialize css](https://materializecss.com/) - Framework css
* [Azure Blob Storage](https://azure.microsoft.com/es-es/services/storage/blobs/) - Almacenamiento de archivos en la nube
* [Heroku](https://rometools.github.io/rome/) - (PaaS) usado para el despliegue
* [OpenLibra](https://openlibra.com/es/page/public-api) - API publica de libros gratis


## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](CONTRIBUTING.md) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

<!-- ## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki) -->

## Autores ✒️

* **Erik172** - *Programador Backend* - [Erik172](https://github.com/Erik172)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia **MIT** - mira el archivo [LICENSE.md](LICENSE.md) para detalles

<!-- ## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc. -->



---
⌨️ con ❤️ por [@_Erik172](https://twitter.com/_Erik172) 😊
