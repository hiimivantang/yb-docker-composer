# yb-docker-composer


yb-docker-composer generates docker-compose.yml dynamically based on your inputs. If no inputs are supplied when running yb-docker-composer, a docker-compose.yml for a YugabyteDB cluster with RF of 3 will be generated. 

```
usage: yb-docker-composer.py [-h] [--tag TAG] [--rf RF]
                             [--placement-info PLACEMENT_INFO]
                             [--master-flags MASTER_FLAGS]
                             [--tserver-flags TSERVER_FLAGS] [--no-prometheus]
                             [--prometheus] [--no-ysql] [--ysql] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --tag TAG             yugabytedb/yugabyte Docker image tag.
  --rf RF               Replication factor
  --placement-info PLACEMENT_INFO
                        Specify the placement info in the following format:
                        cloud.region.zone. Can be comma separated in case you
                        want to pass more than one value.
  --master-flags MASTER_FLAGS
                        Specify extra master flags as a set of key-value
                        pairs.
  --tserver-flags TSERVER_FLAGS
                        Specify extra tserver flags as a set of key-value
                        pairs.
  --no-prometheus       Exclude Prometheus and Grafana (Default)
  --prometheus          Include Prometheus and Grafana
  --no-ysql             Disable Postgres compatible YSQL API
  --ysql                Enable Postgres compatible YSQL API (Default)
  -o OUTPUT, --output OUTPUT
                        Path to output docker-compose yaml file
```


With --prometheus flag, Yugabyte Grafana dashboard comes imported out-of-the box. Log in Grafana (localhost:3000) with username `admin` and password `admin`.
<img width="1792" alt="image" src="https://github.com/hiimivantang/yb-docker-composer/assets/4137197/481d6f01-feeb-42f7-8c0b-ed17dadaa8f0">




