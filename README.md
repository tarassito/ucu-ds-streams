***Prerequisite***:
 - docker must be installed
 
**How to run:**  
1. Run kafka cluster: `docker compose -f init-kafka-cluster.yaml up -d` Cluster is created 
with 3 nodes and 1 topic (browser-history).

2. To populate data in Kafka topic and calculate most popular domains run: `docker compose -f run.yaml up`.

3. After job is done - `docker compose -f init-kafka-cluster.yaml -f run.yaml down`

