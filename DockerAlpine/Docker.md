# Práctica Docker — Alpine 

# 1) Descargar la imagen alpine sin arrancarla y comprobar que está en tu equipo

![1.DescargaAlpine.png](img%2F1.DescargaAlpine.png)


* `docker pull alpine` descarga la imagen sl equipo local. 
* `docker images` lista las imágenes locales; ahí debe aparecer `alpine` en la columna `REPOSITORY`.

---
# 2) Crear un contenedor sin ponerle nombre. ¿Está arrancado? Obtener el nombre

![2.CrearContenedorSinNombre.png](img%2F2.CrearContenedorSinNombre.png)
Explicación (nivel bajo):

* `docker run -d alpine` crea un contenedor. El comando devolvió un `CONTAINER ID`.
* `docker ps -a` muestra el contenedor 
* el nombre aleatorio es `strange_raman`.

---
