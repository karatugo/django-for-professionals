> Python3 not found:

docker-compose exec web pipenv --python /usr/local/bin/python3 install psycopg2-binary==2.8.3

> Could not translate host name “db” to address using Postgres, Docker Compose and Psycopg2

if you add this to your db container in your docker-compose.yml it should resolve the issue


    environment:
      - "POSTGRES_HOST_AUTH_METHOD=trust"

https://stackoverflow.com/questions/51750715/could-not-translate-host-name-db-to-address-using-postgres-docker-compose-and