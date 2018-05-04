# Testing

![A cubelike figure with poligonal holes and two smaller objects that fit on those holes](https://d2wlcd8my7k9h4.cloudfront.net/static/figures/testing.jpg)

Testing is very important. Not only to prevent and debug annoying
bugs but it also helps project newcomers to better understand the
expected functionality of your functions and classes.

## Resources

* We recommend taking a look at this [page](https://mfranc.com/unit-testing/tdd-unit-testing-big-list-of-learning-resources-from-basics-to-advanced-topics/),
  which contains several resources for unit testing, from basic to advanced.
* [Awesome Testing](https://github.com/TheJambo/awesome-testing) has a list of
  a good number of testing resources and books.
* [Awesome-test-automation](https://github.com/atinfo/awesome-test-automation):
  A curated list of awesome test automation frameworks, tools, libraries, and
  software for different programming languages.

## Unit testing

Unit testing is a software testing method by which individual units of source code, sets of one or more
computer program modules together with associated control data, usage procedures, and operating procedures,
are tested to determine whether they are fit for use.

We strongly recommend the use of unit tests in the software we build. If you want to learn how to implement
useful unit tests we suggest take a look at this [guidelines](http://geosoft.no/development/unittesting.html)

## Specific language guidelines

If you want to obtain more specific information on how to implement tests in a specific language refer
to the [language specific testing guidelines].

## Integration testing

Integration Testings is a level of software testing where individual units are combined and tested as
a group. The purpose of this level of testing is to expose faults in the interaction between integrated
units. Test drivers and test stubs are used to assist in Integration Testing.

We usually use [Selenium](http://www.seleniumhq.org/) to perform automatic Integration and Acceptance
Testing in our web applications.

If you want learn more about intrgration tests, for example tips and approachs, we suggest take a look
at [Software Testing Fundamentals](http://softwaretestingfundamentals.com/integration-testing/).

## Acceptance Testing

Acceptance testing is a term used in agile software development
methodologies, particularly extreme programming, referring to the
functional testing of a user story by the software development
team during the implementation phase.

The customer specifies scenarios to test when a user story has
been correctly implemented. A story can have one or many
acceptance tests, whatever it takes to ensure the functionality
works. Acceptance tests are black-box system tests. Each
acceptance test represents some expected result from the system.

Some guidelines on Acceptance Testing and functional testing can be found in
[guide](http://www.softwaretestinghelp.com/practical-software-testing-tips-to-test-any-application/)

## Load and Performance Testing

Load tests are important to measure the performance of your application. You can emulate scenarios
with many users accessing the application at the same time and evaluate if the application responds
according.

Another approach is test specific endpoints and detects if the performance decrease with some changes.

A common tool to implement this kind of tests is [Apache's JMeter](https://jmeter.apache.org/). If you
want to learn how to implement test with Jmeter take a look at this [tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-apache-jmeter-to-perform-load-testing-on-a-web-server).

[language specific testing guidelines]: languages/README.md
