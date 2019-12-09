#!/bin/bash

if ["$DATABASE_SERVER" = "postgres"]
then
    echo "Wating for postgres...."
    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 2
    done
    echo "Postgresql started"
fi

if [ "$(PGPASSWORD=django_docker  psql -U django_docker -h db -tAc "SELECT 1 FROM pg_database WHERE datname='$SQL_DATABASE'" )" = '1' ]; then
    echo "Database already exists... migration will starting soon"
else
    echo "Database does not exist and creating database and permission"
    PGPASSWORD=$SQL_PASSWORD psql -U $SQL_USER -h $SQL_HOST -p $SQL_PORT  -c  "CREATE USER $SQL_USER;"
    PGPASSWORD=$SQL_PASSWORD psql -U $SQL_USER -h $SQL_HOST -p $SQL_PORT  -c  "CREATE DATABASE $SQL_DATABASE;"
    PGPASSWORD=$SQL_PASSWORD psql -U $SQL_USER -h $SQL_HOST -p $SQL_PORT  -c  "GRANT ALL PRIVILEGES ON DATABASE $SQL_DATABASE TO $SQL_USER;"
fi


echo "Flush the manage.py command it any"

while ! python manage.py flush --no-input 2>&1; do
    echo "Flusing django manage command"
    sleep 3
done

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python manage.py migrate  2>&1; do
    echo "Migration is in progress status"
    sleep 3
done

echo "Django docker is fully configured successfully."

exec "$@"

