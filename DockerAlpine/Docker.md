# Práctica Docker — Alpine 

# 1) Descargar la imagen alpine sin arrancarla y comprobar que está en tu equipo

![1.DescargaAlpine.png](img%2F1.DescargaAlpine.png)


* `docker pull alpine` descarga la imagen sl equipo local. 
* `docker images` lista las imágenes locales; ahí debe aparecer `alpine` en la columna `REPOSITORY`.

---
# 2) Crear un contenedor sin ponerle nombre. Obtener el nombre

![2.CrearContenedorSinNombre.png](img%2F2.CrearContenedorSinNombre.png)

* `docker run -d alpine` crea un contenedor. El comando devolvió un `CONTAINER ID`.
* `docker ps -a` muestra el contenedor 
* el nombre aleatorio es `strange_raman`.

---

# 3) Crear un contenedor con nombre dam_alp1.


![3.CrearContenedorConNombre.png](img%2F3.CrearContenedorConNombre.png)

* `--name dam_alp1` de este modo referenciamos el contenedor por su nombre.
* Para acceder al contenedor si está ejecutándose se usa el comando `docker exec -it dam_alp1 sh`
* Si el contenedor está excited primero hay que arrancarlo.



---

# 4) Comprobar qué IP tiene y si puedes hacer ping a google.com
![4.IPyPINaGoogle.png](img%2F4.IPyPINaGoogle.png)


* `ip a` para comprobar la ip.
* `ping google.com` funcinó sin fallos por lo que comprobamos que el host tiene conexión a Internet.



---

# 5) Crear `dam_alp2`. ¿Puedes hacer ping entre contenedores?

1. `docker run -it --name dam_alp2 alpine` crea y ejecuta `dam_alp2`.
2. Desde dentro vemos la IP con `ip a` que resulta ser `172.17.0.2`.
3. A continuación hay que hacer el ping a la IP `172.17.0.3` (en la primera captura me faltaba `-c 4` para limitar, está correcto en la segunda captura)
![5.PinEntreContenedores.png](img%2F5.PinEntreContenedores.png)

![5.1.Pin.png](img%2F5.1.Pin.png)

---

# 6) Sal del terminal, ¿qué ocurrió con el contenedor?


* Con `exit` salimos de la terminal del contenedor.
* Con `docker ps -a` comprobamos el estado de los contenedores.

---

# 7) ¿Cuánta memoria en disco ocupaste?

* Usando `docker system df` comprobamos cuanto espacio en disco ocupa ahora Docker.
