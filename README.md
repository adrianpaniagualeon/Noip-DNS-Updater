## NOW DNS UPDATER

## ¿Qué hace este script?
Este script permite la actualización de la IP pública de la maquina que lo ejecuta en los servidores DNS de Noip. Para evitar sobrecargar la API de Noip, se ejecuta cada 5 minutos hasta que el usuario decida parar el servicio.

## ¿Cómo puedo colaborar?
Existen dos formas de colaborar:
- Añadiendo nuevas funcionalidades al bot mediante _pull-request_. 
- Aportación económica: Puedes aportar tu granito de arena por [Paypal](https://paypal.me/panleoad)
- Invitarme a un café: Me puedes invitar a un café a través de [Ko-Fi](https://ko-fi.com/adrianpaniagualeon)

## ¿Necesita alguna librería externa?
Si, este script necesita la librería [Requests](https://requests.readthedocs.io/en/master/). Puedes instalarla con el siguiente comando "pip install requests".

## ¿Qué datos necesito para autenticarme?
|DATO|INFORMACIÓN|
|-|-|
|EMAIL|CORREO ELECTRÓNICO UTILIZADO PARA REGISTRARTE EN NOIP|
|PASSWORD|CONTRASEÑA DE TU CUENTA NOIP|
|HOST|DOMINIO QUE QUEREMOS ACTUALIZAR|

Tienes que modificar el archivo ddns.py con tus datos para que el script funcione. Es muy importante no introducir espacios para que todo funcione correctamente.

## Me da un error al intentar ejecutarlo

|Estado|Descripción|
|-|-|
|good {IP_ADDRESS}| La IP se ha actualizado correctamente |
|nochg {IP_ADDRESS}| La IP es la misma y no se ha actualizado|
|nohost|El dominio introducido no existe o no pertenece a tu cuenta|	
|badauth|Email o contraseña incorrecta|
|badagent|NowIP ha bloqueado esta aplicación. Busca en el código `Adrian Paniagua DNS UPDATER maintainer-github@adrianpaniagua.es` y cambialo por lo que tu quieras|
|abuse| Tu cuenta de NOIP ha sido bloqueada|
|911| Error en NOIP. Espera hasta que el servicio se restablezca|
