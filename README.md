# yb-docker-composer

`docker-compose up -d` to run a 3-node YugabyteDB alongside Prometheus and Grafana.

Yugabyte dashboard comes imported out-of-the box. Log in Grafana (localhost:3000) with username `admin` and password `admin`.
<img width="1792" alt="image" src="https://github.com/hiimivantang/yb-docker-composer/assets/4137197/481d6f01-feeb-42f7-8c0b-ed17dadaa8f0">




TODO:

- Python-based CLI for generating docker-compose files
- Supports `YB-Master`, `YB-TServer`, `Prometheus`, and `Grafana`.
- Finalize arguments for script. Tentatively, whatever yb-docker-ctl accepts today:
    * --rf
    * --placement_info 
    * --master_flags
    * --tserver_flags
    * --num_shards_per_tserver
    * --tag
- In addition to yb-dockerctl arguments, support: 
    * --ysql
    * --ycql
    * --prometheus
    * 



ROADMAP:

- kafka brokers and connect workers






RESOURCES:
-  


