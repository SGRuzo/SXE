Basándome en el contenido del archivo YAML que proporcionaste, aquí tienes el código equivalente en formato de script Bash:

```bash
#!/bin/bash

# Crear la red de Docker
docker network create prestashop_network

# Ejecutar el contenedor de MySQL
docker run -d \
    --name mysql_db \
    --restart always \
    --network prestashop_network \
    -e MYSQL_ROOT_PASSWORD=admin123 \
    -e MYSQL_DATABASE=prestashop_db \
    -e MYSQL_USER=prestashop_user \
    -e MYSQL_PASSWORD=prestashop_pass \
    mysql:latest

# Ejecutar el contenedor de PrestaShop
docker run -d \
    --name prestashop \
    --restart always \
    --network prestashop_network \
    --link mysql_db:db \
    -p 8080:80 \
    -e DB_SERVER=db \
    -e DB_NAME=prestashop_db \
    -e DB_USER=prestashop_user \
    -e DB_PASSWD=prestashop_pass \
    prestashop/prestashop:latest

# Ejecutar el contenedor de phpMyAdmin
docker run -d \
    --name phpmyadmin \
    --restart always \
    --network prestashop_network \
    --link mysql_db:db \
    -p 8081:80 \
    -e PMA_HOST=db \
    -e PMA_USER=root \
    -e PMA_PASSWORD=admin123 \
    phpmyadmin/phpmyadmin:latest

echo "Todos los contenedores están en ejecución:"
echo "- MySQL en el contenedor: mysql_db"
echo "- PrestaShop accesible en: http://localhost:8080"
echo "- phpMyAdmin accesible en: http://localhost:8081"
```

**Notas importantes sobre el script:**

1. **Corrección del nombre de imagen**: En tu YAML original había `server:mysql:latest` que he corregido a `mysql:latest`

2. **Dependencias**: He añadido `--link mysql_db:db` para establecer la conectividad entre contenedores, ya que PrestaShop y phpMyAdmin dependen de MySQL

3. **Red**: Todos los contenedores están conectados a la misma red `prestashop_network`

4. **Puertos expuestos**:
    - PrestaShop: puerto 8080 → 80
    - phpMyAdmin: puerto 8081 → 80

5. **Variables de entorno**: Se mantienen todas las credenciales y configuraciones del YAML original

**Para usar el script:**
1. Guárdalo como `deploy.sh`
2. Dale permisos de ejecución: `chmod +x deploy.sh`
3. Ejecútalo: `./deploy.sh`

Este script replicará exactamente la misma configuración que tienes en tu archivo Docker Compose.