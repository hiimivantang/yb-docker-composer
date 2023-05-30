from jinja2 import Environment, FileSystemLoader
import argparse
import os


def generate_hostnames(replication_factor):
    pass

def generate_yb_master_services(args):
    return Environment(loader=FileSystemLoader("templates/services/")).get_template("yb-master-cluster.j2").render(vars(args))

def generate_yb_tserver_services(args):
    return Environment(loader=FileSystemLoader("templates/services/")).get_template("yb-tserver-cluster.j2").render(vars(args))

def generate_prometheus_context():
    pass

def generate_grafana_context():
    pass

# print(template.render(context))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--tag', dest='tag', help='yugabytedb/yugabyte Docker image tag.', default='latest')
    parser.add_argument('--rf', dest='rf', default=3, type=int, help='Replication factor')
    parser.add_argument('--placement-info', dest='placement_info', help='Specify the placement info in the following format: cloud.region.zone. Can be comma separated in case you want to pass more than one value.')

    parser.add_argument('--master-flags', dest='master_flags', help='Specify extra master flags as a set of key-value pairs.')
    parser.add_argument('--tserver-flags', dest='tserver_flags', help='Specify extra tserver flags as a set of key-value pairs.')

    parser.add_argument('--no-prometheus', dest='prometheus', action='store_false', help='Exclude Prometheus and Grafana (Default)', default=False)
    parser.add_argument('--prometheus', action='store_true', help='Include Prometheus and Grafana')

    parser.add_argument('--no-ysql', dest='ysql', action='store_false', help='Disable Postgres compatible YSQL API')
    parser.add_argument('--ysql', action='store_true', help='Enable Postgres compatible YSQL API')

    parser.add_argument('--no-ycql', dest='ycql', action='store_false', help='Disable Cassandra compatible YCQL API')
    parser.add_argument('--ycql', action='store_true', help='Enable Cassandra compatible YCQL API')

    parser.add_argument('-o', '--output', dest='output', default='test/docker-compose.yaml', help='Path to output docker-compose yaml file')

    args = parser.parse_args()
    print(args)


    #Generate services
    services = []

    services.append(generate_yb_master_services(args))
    services.append(generate_yb_tserver_services(args))

    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("docker_compose.j2")
    
    rendered = template.render(dict(services=services))
    
    with open(args.output, "w") as fh:
        fh.write(rendered)


    #template = environment.get_template("yb-master.j2")
    #print(template.render(context))
