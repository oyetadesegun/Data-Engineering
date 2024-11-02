cd airflow_docker
docker-compose up airflow-init
docker-compose up -d

docker exec -it airflow_docker-airflow-webserver-1 bash