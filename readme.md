1. Para Odoo primero crea el docker-compose.yml
2. Lánzalo con docker-compose up -d
3. Este comando `docker exec -it [T18_odoo] odoo scaffold [TuModulo] /mnt/extra-addons`
4. Scaffold para crear la estructura `docker exec -it [T18_odoo] chmod 777 -R /mnt/extra-addons/[TuModulo]`
