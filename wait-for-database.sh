#!/bin/sh

set -e

until mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -h"$MYSQL_HOST" -e "show databases;" > /dev/null 2>&1; do
  >&2 echo "MariaDB is unavailable - sleeping"
  sleep 1
done

>&2 echo "MariaDB is up - executing migrations"

python3 manage.py makemigrations
python3 manage.py migrate

>&2 echo "Now, executing command: $@"

exec "$@"