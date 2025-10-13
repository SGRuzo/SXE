# Práctica Docker — Apache httpd

## 1) Descargar la imagen 'httpd' y comprobar que está en tu equipo

![1. Descargarhttpd.png](img/1.%20Descargarhttpd.png)

* `docker pull httpd:2.4` descarga la imagen httpd versión 2.4
* `docker images` lista las imágenes locales; ahí debe aparecer `httpd` con tag `2.4` en la lista.

---

## 2) Crear un contenedor con el nombre 'dam_web1'

![2. CrearContenedor.png](img/2.%20CrearContenedor.png)

* `docker run -dit --name dam_web1 httpd:2.4` crea y ejecuta un contenedor con nombre `dam_web1`.
* `docker ps` comprueba que el contenedor está en ejecución.

---
