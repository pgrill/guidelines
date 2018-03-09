# Databases

![A stack of disks](https://i.stack.imgur.com/DZc0e.png)

## Introduction

For data that must be saved and stored correctly, we use
[PostgreSQL](https://www.postgresql.org/) (we usually refer to it as
"Postgres"). It's a thirty-year-old open source database that is highly
respected, is well supported by documentation and hosting providers, and
can be used by any developer who knows the SQL standard.

In recent years, a movement called
[NoSQL](https://en.wikipedia.org/wiki/NoSQL) has gained popularity. Best
translated as "not only SQL", tremendous effort has been made to create
different kinds of databases for different use cases, often based on
academic or industry research.

Ours most frequently used NoSQL database are [Redis](https://redis.io/),
which we use for storing transient, high quantity read/write data such
as activity feeds, tags, background jobs, sessions, tokens, and
counters. Another NoSQL database is
[Cassandra](http://cassandra.apache.org/) which we use for storing time
series. Redis and Cassandra are reliable, open-source, and simple. They
offer high performance and reliable predictions of its performance.

When we need to do full-text search on documents, we use
[Solr](http://lucene.apache.org/solr/). Its major features include hit
highlighting, faceted search, real-time indexing, dynamic clustering,
database integration, and rich text documents handling.

## Resources

* [Awesome Databases](https://github.com/dhamaniasad/awesome-databases) contains
  a list of databases, categorized by type and language.
* [W3Schools SQL Tutorial](http://www.w3schools.com/sql/default.asp)
* [Codecademy – "Learn SQL"](https://www.codecademy.com/learn/learn-sql)
* [Khan Academy – "Intro to SQL"](https://www.khanacademy.org/computing/computer-programming/sql)