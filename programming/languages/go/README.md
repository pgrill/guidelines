# Go Guidelines

## Learning resources

* [Pluralsight](https://www.pluralsight.com/search?q=golang&categories=all)
* [Go lang tutorial](https://golangbot.com/page/2/)
* [https://github.com/golang/go/wiki/Learn](https://github.com/golang/go/wiki/Learn)

## Required development tools

* [goimports](https://godoc.org/golang.org/x/tools/cmd/goimports)
* [golint](https://github.com/golang/lint)
* [gometalinter](https://github.com/alecthomas/gometalinter) which includes
   previous tools and run them asynchronously
* [gofmt](https://golang.org/cmd/gofmt/) with the ``-s`` option to simplify code

Integrate those tools with your own editor.

## Coding Style

### Types

Types should be explicit as much as possible:

* Avoid `interface{}` type.
* Don't be shy and/or skinflint about interface.
* Visitor pattern is your best-friend if you can't use an interface, in order
  to avoid `interface{}` type.

Use generic litterals _(`int`, `float`, etc...)_ **unless you are defining a
 model**, which should follow these conventions:

* Use `int64` type for primary, foreign key and counter.
* Use `Enumerated` type for enumeration.

```go
// Foobar is ...
type Foobar struct {
    ID        int64 `db:"id"`
    UserID    int64 `db:"user_id"`
    AccountID int64 `db:"account_id"`
    HitCount  int64 `db:"hit_count"`
    MissCount int64 `db:"miss_count"`
    Status    Enumerated `db:"status"`
    Type      Enumerated `db:"type"`
}
```

### Naming convention

```go
type Category struct{}
type Media struct{}

// slices
mediaList := []Media{}
categories := []Category{}

// maps
categoriesByID := map[int][]Category{}
mediaListByID := map[int][]Media{}
categoryByID := map[int]Category{}
```

### Context

``context.Context`` should be immutable, don't rely on ``context.Background()`` only to initialize it.

If your context is global don't store too much things in it, keep it simple:

* connection pool (redis, postgresql, rabbitmq, etc.)
* configuration

For the request context include all keys from the application context and add it request information:

* user
* resource for the dedicated endpoint
* user lang

### Error handling

If your method can fail, you need to propagate the error to the root level.

You need to [wrap](https://github.com/pkg/errors) the error and add context.

Always set a recover behavior.

panic/recover is meant for exceptions not common errors.

Always check for errors.

```go
// bad
foo()
val, _ := foo()

// good
_, err := foo()
val, err := foo()
```

Group your logic when checking an error.

```go
// bad
result, err := thisMethodWillFail()

if err != nil {
  return err
}

// bad
if err := thisMethodWillFail(); err != nil {
    return err
}

// good
result, err := thisMethodWillFail()
if err != nil {
  return err
}
```

## Project architecture

This is an initial draft:

```bash
/application
    /commands
/configuration
    configuration.go
/constants
    constants.go
/events
    users.go
/gimme
    store.go
/failures
    errors.go
    handlers.go
/managers
    users.go
    users_test.go
/models
    user.go
        user_test.go
/payments
    /backends
/store
        users.go
        users_queries.go
/rpc
    /validators
    user.go
    /payloads
    user.go
    /resources
    user.go
/tasks
    users.go
/web
    /authentication
    facebook.go
    ulule.go
    /handlers
    permissions.go
    resources.go
    users.go
    /middleware
    authentication.go
    router.go
    server.go
/worker
    /handlers
    users.go
    worker.go
```

## References

* [Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments)
