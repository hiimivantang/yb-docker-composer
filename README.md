# yb-docker-composer

## Overview

yb-docker-composer generates docker-compose.yml dynamically based on your inputs. If no inputs are supplied when running yb-docker-composer, a docker-compose.yml for a YugabyteDB cluster with RF of 3 will be generated. 

Getting a YugabyteDB cluster up and running alongside Prometheus+Grafana for monitoring is as easy as:
```
python yb-docker-composer.py --prometheus && docker-compose up -d
```

More options are available:

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


## How does it work?

Jinja templates for `yb-master`, `yb-tserver`, `prometheus`, and `grafana` are used to generate the `docker-compose.yml` file dynamically. Based on the replication factor specified, things like service names, hostnames, container names, and exposed ports are dynamically generated on the fly.

## Why Jinja?

Well, you can easily change layout, content, and formatting of your docker-compose services without modifying the code in `yb-docker-composer.py`. This makes the project so much more extensible. 

In addition, as long as you know a bit of Jinja templating syntax, you can easily add more services e.g. Kafka brokers, Kafka Connect workers, and etc.

## TODO

- [ ] Specify yb-master and yb-tserver flags via CLI
- [ ] sqlpad option
- [ ] Accompanying sample/demo apps
- [ ] Kafka brokers and connect workers



## Resources

- https://github.com/sknop/kafka-docker-composer
- https://github.com/FranckPachot/ybdemo/tree/main/docker/yb-lab
- https://github.com/srinivasa-vasu/yb-loki-alog
