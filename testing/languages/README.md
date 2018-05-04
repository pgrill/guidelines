# Testing guidelines by language

## Python

* A testing unit should focus on one tiny bit of functionality and prove it
  correct.
* Each test unit must be fully independent.
* Use `setUp()` and `tearDown()` methods to set up each test and clear any data.
* Files are named according to the following patterns
  * `test*.py`
  * `*test.py`
* Classes are prefixed with Test (without an `__init__` method) like `TestFoo`
* Functions are prefixed with test like `test_foo`
* Use [FactoryBoy] in favour of Fixtures to set up testing data
* User [Coverage.py](https://coverage.readthedocs.io/) to measure test code
  coverage
* Use the [mock](http://www.voidspace.org.uk/python/mock) library to isolate
  side effects from external code.
* Use the `patch` decorators to apply mocks clearly

## React

* Use [Jest](https://facebook.github.io/jest/) along with
  [enzyme](https://github.com/airbnb/enzyme) library in order to
  make efficient reducer and component tests.
* Each test should live in each component directory and should have the name of
  the component plus `.test.js`.
* We use the `expect` module from [chai](http://chaijs.com/) in order to compare
  values.
* We use [shallow rendering](http://airbnb.io/enzyme/docs/api/shallow.html)
  in order to test React components in an efficient way.

## Angular

* We suggest use the following libraries:
  * [Jasmine](https://jasmine.github.io/):
   Useful development framework for testing JavaScript code.
  * [Sinon](http://sinonjs.org/):
    Standalone test spies, stubs and mocks for JavaScript.
* Each test should live in each component directory and should have the name of
  the component plus `.test.js`.
* We use the `expect` module from [chai](http://chaijs.com/) in order to compare
  values.

[shallow rendering]:  http://airbnb.io/enzyme/docs/api/shallow.html
[FactoryBoy]: http://factoryboy.readthedocs.io/en/latest/orms.html