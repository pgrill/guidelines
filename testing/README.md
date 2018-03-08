# Testing

![A cubelike figure with poligonal holes and two smaller objects
that fit on those holes](https://d2wlcd8my7k9h4.cloudfront.net/static/figures/testing.jpg)

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

Unit testing is a software testing method
by which individual units of source code, sets of one or more
computer program modules together with associated control data,
usage procedures, and operating procedures, are tested to
determine whether they are fit for use. The following guidelines
are inspired on [this](http://geosoft.no/development/unittesting.html)
page.

* Keep unit tests small and fast. Ideally the entire test suite should be
  executed before every code check in. Keeping the tests fast reduce the
  development turnaround time.
* Unit tests should be fully automated and non-interactive. The test suite is
  normally executed on a regular basis and must be
  fully automated to be useful. If the results require manual
  inspection the tests are not proper unit tests.
* Make unit tests simple to run. Configure the development environment so that
  single tests and test suites can be run by a single command or a one button
  click.
* Measure the tests. Apply coverage analysis to the test runs so that it is
  possible to read the exact execution coverage and investigate which parts of
  the code is executed and not.
* Fix failing tests immediately. Each developer should be responsible for
  making sure a new test runs successfully upon check in, and that all existing
  tests runs successfully upon code check in.
* Keep testing at unit level. Unit testing is about testing classes. There
  should be one test class per ordinary class and the class behaviour should be
  tested in isolation. Avoid the temptation to test an entire work-flow
  using a unit testing framework, as such tests are slow and hard to
  maintain. Work-flow testing may have its place, but it is not unit
  testing and it must be set up and executed independently.
* Keep tests independent. To ensure testing robustness and simplify maintenance
  tests should never rely on other tests nor should they depend on the ordering
  in which tests are executed.
* Keep tests close to the class being tested. If the class to test is `Foo` the
  test class should be called `FooTest` and kept in the same package (directory)
  as `Foo`. Keeping test classes in separate directory trees makes them
  harder to access and maintain.
* Name tests properly. Make sure each test method test one distinct feature of
  the class being tested and name the test methods accordingly. The typical
  naming convention is `test[what]` such as `testSaveAs()`, `testAddListener()`,
  `testDeleteProperty()` etc.
* Test public API. Unit testing can be defined as testing classes through their
  public API. Some testing tools makes it possible to test private
  content of a class, but this should be avoided as it makes the
  test more verbose and much harder to maintain. If there is private
  content that seems to need explicit testing, consider refactoring
  it into public methods in utility classes instead. But do this to
  improve the general design, not to aid testing.
* Think black-box. Act as a 3rd party class consumer, and test if the class
  fulfills its requirements. And try to tear it apart.
* Think white-box. After all, the test programmer also wrote the class being
  tested, and extra effort should be put into testing the most complex logic.
* Test the trivial cases too. It is sometimes recommended that all non-trivial
  cases should be tested and that trivial methods like simple setters and
  getters can be omitted. However, there are several reasons why trivial
  cases should be tested too. The recommendation is therefore to test
  everything. The trivial cases are simple to test after all.
* Focus on execution coverage first. Differentiate between execution coverage
  and actual test coverage. The initial goal of a test should be to ensure high
  execution coverage. This will ensure that the code is actually executed on
  some input parameters. When this is in place, the test coverage should be
  improved. Note that actual test coverage cannot be easily measured (and is
  always close to 0% anyway).
* Cover boundary cases. Make sure the parameter boundary cases are covered. For
  numbers, test negatives, 0, positive, smallest, largest, NaN, infinity,
  etc. For strings test empty string, single character string,
  non-ASCII string, multi-MB strings etc. For collections test empty,
  one, first, last, etc. For dates, test January 1, February 29,
  December 31 etc. The class being tested will suggest the boundary
  cases in each specific case. The point is to make sure as many as
  possible of these are tested properly as these cases are the prime
  candidates for errors.
* Test each feature once. When being in testing mode it is sometimes tempting
  to assert on "everything" in every test. This should be avoided as it makes
  maintenance harder. Test exactly the feature indicated by the name
  of the test method.
* Use explicit asserts. Always prefer `assertEquals(a, b)` to `assertTrue(a ==
  b)` (and likewise) as the former will give more useful information of what
  exactly is wrong if the test fails.
* Provide negative tests. Negative tests intentionally misuse the code and
  verify robustness and appropriate error handling.
* Design code with testing in mind. Writing and maintaining unit tests are
  costly, and minimizing public API and reducing cyclomatic complexity in the
  code are ways to reduce this cost and make high-coverage test code faster to
  write and easier to maintain. Some suggestions:
  * Make class members immutable by establishing state at
    construction time. This reduce the need of setter methods.
  * Restrict the use of excessive inheritance and virtual public
    methods.
  * Avoid unnecessary branching.
  * Keep as little code as possible inside branches.
  * Make heavy use of exceptions and assertions to validate
    arguments in public and private API's respectively.
  * Don't connect to predefined external resources
    Unit tests should be written without explicit knowledge of the
    environment context in which they are executed so that they
    can be run anywhere at anytime. In order to provide required
    resources for a test these resources should instead be made
    available by the test itself.
* Know the cost of testing. Not writing unit tests is costly, but writing unit
  tests is costly too. There is a trade-off between the two, and in terms of
  execution coverage the typical industry standard is at about 80%.
  The typical areas where it is hard to get full execution coverage
  is on error and exception handling dealing with external
  resources.
* Prioritize testing. Unit testing is a typical bottom-up process, and if there
  is not enough resources to test all parts of a system priority should be
  put on the lower levels first.
* Write tests to reproduce bugs. When a bug is reported, write a test to
  reproduce the bug (i.e. a failing test) and use this test as a success
  criteria when fixing the code.
* Know the limitations. Unit tests can never prove the correctness of code. A
  failing test may indicate that the code contains errors, but a succeeding test
  doesn't prove anything at all.

## Specific language guidelnes

Refer to the [language specific testing guidelines] for more
information on how to write tests for specific languages.

## Integration testing

An excerpt from [Software Testing fundamentals](./#)

![Integration testing diagram](http://softwaretestingfundamentals.com/wp-content/uploads/2010/12/integrationtesting.jpg)

Integration Testings is a level of software testing where
individual units are combined and tested as a group. The purpose
of this level of testing is to expose faults in the interaction
between integrated units. Test drivers and test stubs are used to
assist in Integration Testing.

### Tasks

* Integration Test Plan
  * Prepare
  * Review
  * Rework
  * Baseline
* Integration Test Cases/Scripts
  * Prepare
  * Review
  * Rework
  * Baseline
* Integration Test
  * Perform

### When is Integration Testing performed

Integration Testing is the second level of testing performed after
Unit Testing and before System Testing.

### Who performs Integration Testing

Either Developers themselves or independent Testers perform
Integration Testing.

### Approaches

* _Big Bang_ is an approach to Integration Testing where all or
  most of the units are combined together and tested at one go.
  This approach is taken when the testing team receives the entire
  software in a bundle. So what is the difference between Big Bang
  Integration Testing and System Testing? Well, the former tests
  only the interactions between the units while the latter tests
  the entire system.
* _Top Down_ is an approach to Integration Testing where top level
  units are tested first and lower level units are tested step by
  step after that. This approach is taken when top down
  development approach is followed. Test Stubs are needed to
  simulate lower level units which may not be available during the
  initial phases.
* _Bottom Up_ is an approach to Integration Testing where bottom
  level units are tested first and upper level units step by step
  after that. This approach is taken when bottom up development
  approach is followed. Test Drivers are needed to simulate higher
  level units which may not be available during the initial phases.

### Tips

* Ensure that you have a proper Detail Design document where
  interactions between each unit are clearly defined. In fact, you
  will not be able to perform Integration Testing without this
  information.
* Ensure that you have a robust Software Configuration Management
  system in place. Or else, you will have a tough time tracking
  the right version of each unit, especially if the number of
  units to be integrated is huge.
* Make sure that each unit is first unit tested before you start
  Integration Testing.

### Selenium

We usually use [Selenium](http://www.seleniumhq.org/) a web browser
automation to perform Integration and Acceptance Testing

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

Some guidelines on Acceptance Testing and functional testing in general taken
from this [guide](http://www.softwaretestinghelp.com/practical-software-testing-tips-to-test-any-application/)

* Learn to analyze your test results thoroughly. Do not ignore any test result.
  The final test result may be ‘pass’ or ‘fail’, but troubleshooting the root
  cause of ‘fail’ will give you the solution of the problem. Testers will be
  respected if they not only log the bugs but also provide solutions.
* Learn to maximize the test coverage each time you test any application. 100%
  test coverage might not be possible but still, you can always try to reach
  near it.
* In order to ensure maximum test coverage, break your application under test
  (AUT), into smaller functional modules. Write test cases on such individual
  unit modules. Also if possible break these modules into smaller parts.
* While writing test cases, write test cases for intended functionality first
  i.e. for valid conditions according to requirements. Then write test cases
  for invalid conditions. This will cover expected as well unexpected behavior
  of the application under test.
* Think positive. Start testing the application with the intend of finding
  bugs/errors. Don’t think beforehand that there will not be any bugs in the
  application. If you test the application with an intention of finding bugs
  you will definitely succeed to find those subtle bugs also.
* Write your test cases in the requirement analysis and design phase itself.
  This way you can ensure that all the requirements are testable.
* Make your test cases available to the developers prior to coding. Don’t keep
  your test cases with you waiting to get final application release for testing,
  thinking that you can log more bugs. Let the developers analyze your test
  cases thoroughly to develop a quality application. This will also save the
  re-work time.
* If possible identify and group your test cases for regression testing. This
  will ensure quick and effective manual regression testing.
* Applications requiring critical response time should be thoroughly tested for
  performance.
* Go beyond requirement testing. Test the application for what it is not
  supposed to do.
* While doing regression testing use the previous bug graph (Bug graph – number
  of bugs found against time for different modules). This module-wise bug graph
  can be useful to predict the most probable bug part of the application.
* Note down the new terms, concepts you learn while testing. Keep a text file
  open while testing any application. Note down the testing progress and
  observations in it. Use these notepad observations while preparing final test
  release report. This good habit will help you to provide the complete
  unambiguous test report and release details.
* Many times testers or developers make changes in the code base for
  application under test. This is a required step in development or testing
  environment to avoid execution of the live transaction processing like in
  banking projects. Note down all such code changes done for testing purpose
  and at the time of final release make sure you have removed all these changes
  from the final client-side deployment file resources.
* It’s a good practice to involve testers right from the software requirement
  and design phase itself. These way testers can get knowledge of application
  dependability resulting in detailed test coverage. If you are not being asked
  to be a part of this development cycle then you can make a request to your
  lead or manager to involve your testing team in all the decision making
  processes or meetings.
* Increase your conversation with the developers to know more about the
  product. Whenever possible make face-to-face communication for resolving
  disputes quickly and to avoid any misunderstandings. But also when you
  understand the requirement or resolve any dispute – make sure to communicate
  the same over written communication ways like emails. Do not keep anything
  verbal.
* Don’t run out of time to do high priority testing tasks. Prioritize your
  testing work from high to low priority and plan your work accordingly.
  Analyze all associated risks to prioritize your work.
* Write clear, descriptive, unambiguous bug report. Do not only provide the bug
  symptoms but also provide the effect of the bug and all the possible
  solutions.

[language specific testing guidelines]: languages/README.md