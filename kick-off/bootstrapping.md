# Project bootstrapping

## Project directory structure

- A project divided into different git repos is hard to maintain,
  avoid it.

## Docker

### How to organize Docker files

We recommend to use the following folder structure to organize your docker files.

```text
.
├── compose
│   ├── build.sh
│   ├── docker-compose.base.yml
│   ├── docker-compose.dev.yml
│   ├── docker-compose.prod.yml
│   └── up.sh
└── projects
    ├── api
    │   └── Dockerfile
    ├── db
    │   └── Dockerfile
    ├── proxy
    │   └── Dockerfile
    └── frontend
        └── Dockerfile
```

In order to use an environment `docker-compose` file,
you will need to chain them with the `base` one, like this:

```bash
docker-compose -f docker-compose.base.yml -f docker-compose.dev.yml [subcommand] <args>
```

## Commit hooks

We recommend to let [Gilp](https://github.com/sophilabs/gilp) handle that for you.

You can run linters, check commit messages and more with Gilp and Gulp.