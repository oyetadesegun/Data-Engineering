________________________
pip install pgcli psycopg_binary
docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v postgres_db:/var/lib/postgresql/data -p 5432:5432 postgres:13

pgcli -h localhost -u root -p 5432 -d ny_taxi

pip install pgadmin
docker network create pg-network

------------Adding the network--------
 docker run -it \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="root" \
 -e POSTGRES_DB="ny_taxi" \
 -v postgres_db:/var/lib/postgres/data \
 --network=pg-network \
 -p 5432:5432 \
 --name pg-database \
 postgres:13

docker run -it \
 -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
 -e PGADMIN_DEFAULT_PASSWORD="root" \
 -p 8080:80 \
 --network=pg-network \
 --name pgadmin \
 dpage/pgadmin4

 URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"


docker build -t taxi_ingest:v001 .

 docker run --network=pg-network taxi_ingest:v001 --user=root --password=root --host=pg-database --port=5432 --db=ny_taxi --table_name=yellow_taxi_trips --url=${URL}