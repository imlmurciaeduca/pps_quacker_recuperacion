<center><img src="./static/images/quacker.webp" width = 30%></img>
</center>

# Quacker (anteriormente conocida como Y)
La mejor red social para compartir tus ideas y contactar con grandes marcas y personas de importancia a nivel global. Sin un algoritmo que controle lo que ves.

Actualmente sin mantenimiento debido al éxito de la competencia. Si quieres hacer un mantenimiento por tu cuenta, haz un __fork__ del proyecto y sigue las pautas del fichero TODO.md en tu propio repositorio:
  - [TODO.md](TODO.md)

## Instrucciones de uso
Aplicación desarrollada en Python (v3.11) con Flask y Mongo como dependencias principales. Levanta primero un servidor de Mongo en local.

    docker run -p 27017:27017 -d mongo
Luego ejecuta la aplicación con

    python app.py

Desplegará un servidor web en [http://127.0.0.1:5000](http://127.0.0.1:5000)

En el index se mostrará una tabla con los quacks de todos los usuarios, pero cuenta con una API que puedes utilizar para integrarla con tu propia aplicación o para desarrollar tu propio frontend.

### API REST
No cuenta con funcionalidad CRUD completa. Se exponen los siguientes endpoints (acompaño explicación y ejemplos):
  - __\[POST\] /signup__ (registrar nuevo usuario). Espera un JSON con la siguiente estructura:
  
        {
            "username": "",
            "password": ""
        }
    El servidor responderá con código 200 si todo va bien, o con código 400 si hay algún conflicto.

      - Ejemplo de uso:

            curl --request POST -i \
            --url http://localhost:5000/signup \
            --header 'Content-Type: application/json' \
            --data '{
                "username": "Eel_On_Musk",
                "password": "1234"
            }'
  - __\[POST\] /login__ (login de usuario). Espera un JSON con la siguiente estructura:
  
        {
            "username": "",
            "password": ""
        }
    El servidor responderá con código 200 y un __\<user_token\>__ que deberá usarse para completar las peticiones de __quack__ y __requack__. Si hay algún conflicto, responderá con código 400.
      - Ejemplo de uso:

            curl --request POST -i \
            --url http://localhost:5000/login \
            --header 'Content-Type: application/json' \
            --data '{
                "username": "Eel_On_Musk",
                "password": "1234"
            }'
      - Ejemplo de respuesta:

            {"token":"f44e9a89-fd46-43b6-af5d-d7180d79f8f0"}
  - __\[POST\] /\<user_token\>/quack__ (enviar un quack): sustituye __\<user_token\>__ por la respuesta del servidor tras hacer un login satisfactorio. Espera un JSON con la siguiente estructura:

        {
            "quack": ""
        }
    El servidor responderá con código 200 y un __\<quack_id\>__ que puede usarse para completar la petición de __requack__. Si hay algún conflicto, responderá con código 400.
      - Ejemplo de uso:

            curl --request POST -i \
            --url http://localhost:5000/f44e9a89-fd46-43b6-af5d-d7180d79f8f0/quack \
            --header 'Content-Type: application/json' \
            --data '{
                "quack": "The world is quiet here"
            }'
      - Ejemplo de respuesta:

            {"quack_id":"f1311be5-3f6b-4917-8f9b-170fdab0f0a8"}
  - __\[POST\] /\<user_token\>/requack__ (realizar un requack): sustituye __\<user_token\>__ por la respuesta del servidor tras hacer un login satisfactorio. Espera un JSON con la siguiente estructura:

        {
            "quack_id": "{quack_id}"
        }
    Sustituye __{quack_id}__ por la respuesta del servidor tras realizar un quack, o bien los IDs obtenidos de los quacks al llamar a  __\[GET\] /\<username\>__ o  __\[GET\] /\<username\>/all__. El servidor responderá con código 200 si todo va bien, o bien con código 400 si hubiera un conflicto.
      - Ejemplo de uso:

            curl --request POST -i \
            --url http://localhost:5000/f44e9a89-fd46-43b6-af5d-d7180d79f8f0/requack \
            --header 'Content-Type: application/json' \
            --data '{
                "quack_id": "7c2ab360-7395-4537-af40-2a19d5a7b622"
            }'
  - __\[GET\] /\<username\>__ (obtener los quacks de un usuario)
      - Ejemplo de uso:

            curl --request GET \
            --url http://localhost:5000/Eel_On_Musk/
  - __\[GET\] /\<username\>/all__ (obtener los quacks y requacks de un usuario)
      - Ejemplo de uso:

            curl --request GET \
            --url http://localhost:5000/Eel_On_Musk/all