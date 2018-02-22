Infrastructure
--------------

Define a correct infrastructure for each project is important to assure
reliability, good performance and scalability in the applicable. Choose a wrong
infrastructure can bring problems in a production environment.

Sophilabs recommends host your application in Amazon infrastructure and use
containerization.


Amazon Web Services
===================

`Amazon Web Services <https://aws.amazon.com/>`_ provides a set of scalable and reliable services that help you to host and monitor your web applications.
Amazon provides solutions to:

- Compute
	- `Amazon EC2 <https://aws.amazon.com/>`_
	- `Amazon Lambda <https://aws.amazon.com/lambda/?hp=tile&so-exp=below>`_
- Storage
	- `Amazon S3 <https://aws.amazon.com/s3/?hp=tile&so-exp=below>`_
- Database
	- `Amazon RDS <https://aws.amazon.com/rds/?hp=tile&so-exp=below>`_
	- `Amazon DynamoDB <https://aws.amazon.com/dynamodb/?hp=tile&so-exp=below>`_
	- `Amazon Aurora <https://aws.amazon.com/rds/aurora/?hp=tile&so-exp=below>`_
- Cache
	- `Amazon ElasticCache <https://aws.amazon.com/elasticache/?hp=tile&so-exp=below>`_
- Load Balancing
	- `Amazon Load Balancers <https://aws.amazon.com/elasticloadbalancing/?hp=tile&so-exp=below>`_
- Monitoring
	- `Amazon CloudWatch <https://aws.amazon.com/cloudwatch/?hp=tile&so-exp=below>`_

Containerization
================

`Containerization
<https://en.wikipedia.org/wiki/Operating-system-level_virtualization>`_ is
important to isolate your web application server and database.
We recommend use `Docker <https://www.docker.com/>`_ to define the containers that
your application needs.

For example, a simple web application can use 3 containers.

.. image:: ./containers.png

- A Frontend Server, which hosts a javascript application and makes calls to a
  Backend Server to do any operation with the system.
- A Backend Server, which exposes an API for operating with the system. It can
  contain the Admin Site to approve users.
- A Database Server to store persistent data,
  using PostgreSQL or another database engine of your choice.

For big systems, maybe you require Containers Orchestration. In these cases, we
recommend uses `Docker Swarm <https://docs.docker.com/engine/swarm/>`_ or
`Kubernetes <https://kubernetes.io/>`_.
