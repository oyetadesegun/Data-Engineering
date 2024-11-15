create or replace table Table_name
partition by sate(tpep_pickup_datetime)
cluster by verndorID as
select * from taxi_rider;