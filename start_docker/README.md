cd start_docker
docker-compose up airflow-init
;
docker-compose up -d
;
docker exec -it start_docker-airflow-webserver-1 bash

cd airflow_docker;

docker exec -it start_docker-airflow-webserver-1 bash
