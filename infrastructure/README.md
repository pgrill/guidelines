# Infrastructure

Define a correct infrastructure for each project is important to assure
reliability, good performance and scalability in the applicable. Choose
a wrong infrastructure can bring problems in a production environment.

Sophilabs recommends host your application in Amazon infrastructure and
use containerization.

## Amazon Web Services

[Amazon Web Services](https://aws.amazon.com/) provides a set of
scalable and reliable services that help you to host and monitor your
web applications. Amazon provides solutions to:

- Compute
  - [Amazon EC2](https://aws.amazon.com/)
  - [Amazon Lambda](https://aws.amazon.com/lambda/?hp=tile&so-exp=below)
- Storage
  - [Amazon S3](https://aws.amazon.com/s3/?hp=tile&so-exp=below)
- Database
  - [Amazon RDS](https://aws.amazon.com/rds/?hp=tile&so-exp=below)
  - [Amazon DynamoDB](https://aws.amazon.com/dynamodb/?hp=tile&so-exp=below)
  - [Amazon Aurora](https://aws.amazon.com/rds/aurora/?hp=tile&so-exp=below)
- Cache
  - [Amazon ElasticCache](https://aws.amazon.com/elasticache/?hp=tile&so-exp=below)
- Load Balancing
  - [Amazon Load Balancers](https://aws.amazon.com/elasticloadbalancing/?hp=tile&so-exp=below)
- Monitoring
  - [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/?hp=tile&so-exp=below)

## Containerization

[Containerization](https://en.wikipedia.org/wiki/Operating-system-level_virtualization)
is important to isolate your web application server and database. We
recommend use [Docker](https://www.docker.com/) to define the containers
that your application needs.

For example, a simple web application can use 3 containers.

![image](./containers.png)

- A Frontend Server, which hosts a javascript application and makes
  calls to a Backend Server to do any operation with the system.
- A Backend Server, which exposes an API for operating with the
  system. It can contain the Admin Site to approve users.
- A Database Server to store persistent data, using PostgreSQL or another database engine of your
  choice.

For big systems, maybe you require Containers Orchestration. In these cases, we recommend uses
[Docker Swarm](https://docs.docker.com/engine/swarm/) or [Kubernetes](https://kubernetes.io/).

## Domain Names

We suggest using [Domize](https://domize.com/) to see what's available.
Use [DNSimple](https://dnsimple.com/) to buy and maintain domain names
if a client hasn't registered a domain name yet.

## SSL Certificates

Buy a wildcard certificate from
[DNSimple](https://dnsimple.com/ssl-certificates). The wildcard (\*)
lets you use the same certificate on www., staging., api., and any other
future subdomains. SSL and DNS are tightly coupled. If we're doing any
work with SSL, we need to make sure we have access to make DNS changes,
such as adding a CNAME record. When working with a client that has a DNS
department, schedule time during off-peak hours in order to pair program
with their DNS personnel to ensure smooth sailing. We can accidentally
take down a site that is all SSL if this work isn't done methodically.