# Databases

![A stack of disks](https://i.stack.imgur.com/DZc0e.png)

## PostgreSQL

- Introduction

For data that must be saved and stored correctly, we use
[PostgreSQL](https://www.postgresql.org/) (we usually refer to it as
"Postgres"). It's a thirty-year-old open source database that is highly
respected, is well supported by documentation and hosting providers, and
can be used by any developer who knows the SQL standard.

- Installation

A guide to installing Postgres in any environment can be found in [Postgres Installation Tutorial](https://www.postgresql.org/docs/9.3/static/tutorial-install.html).

If you are using [Docker](https://www.docker.com/), you can create your database inside a container using
the [Postgres image](https://docs.docker.com/samples/library/postgres/).

## NoSQL Databases

In recent years, a movement called [NoSQL](https://en.wikipedia.org/wiki/NoSQL) has gained popularity.
Best translated as "not only SQL", tremendous effort has been made to create different kinds of databases
for different use cases, often based on academic or industry research.

Our most frequently used NoSQL database is [Redis](https://redis.io/),
which we use for storing transient, high quantity read/write data such
as activity feeds, tags, background jobs, sessions, tokens, and
counters.

To install Redis you must download the sources and compile it

```bash
wget http://download.redis.io/releases/redis-4.0.8.tar.gz
tar xzf redis-4.0.8.tar.gz
cd redis-4.0.8
make
```

If you are usign Docker, you can use the [Redis image](https://docs.docker.com/samples/library/redis/).

Another NoSQL database is [Cassandra](http://cassandra.apache.org/) which we use for storing time
series. The differents ways of install Casandra are documented [here](http://cassandra.apache.org/download/).

Redis and Cassandra are reliable, open-source, and simple. They offer high performance and reliable
predictions of its performance.

## Solr

When we need to do full-text search on documents, we use
[Solr](http://lucene.apache.org/solr/). Its major features include hit
highlighting, faceted search, real-time indexing, dynamic clustering,
database integration, and rich text documents handling.

## Amazon Relational Database Service (RDS)

For production environments we suggest using [RDS](https://aws.amazon.com/rds/). RDS makes it easy to
set up, operate, and scale a relational database in the cloud.

Some of the features that RDS provides that are helpful for us are:

- Easy to Administer
- Highly Scalable
- Fast
- Secure
- Replication

RDS is compatible with the following databases engines:

- [Aurora](https://aws.amazon.com/rds/aurora/)
- [Postgres](https://aws.amazon.com/rds/postgresql/)
- [MySQL](https://aws.amazon.com/rds/mysql/)
- [MariaDB](https://aws.amazon.com/rds/mariadb/)
- [Oracle](https://aws.amazon.com/rds/oracle/)
- [SQL Server](https://aws.amazon.com/rds/sqlserver/)

## Resources

- [Awesome Databases](https://github.com/dhamaniasad/awesome-databases) contains
  a list of databases, categorized by type and language.
- [W3Schools SQL Tutorial](http://www.w3schools.com/sql/default.asp)
- [Codecademy – "Learn SQL"](https://www.codecademy.com/learn/learn-sql)
- [Khan Academy – "Intro to SQL"](https://www.khanacademy.org/computing/computer-programming/sql)