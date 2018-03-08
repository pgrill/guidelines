# Software design

![Crab on front of different shells](https://d2wlcd8my7k9h4.cloudfront.net/static/figures/product-design.jpg)

## Introduction

The main purpose Sofware of design is to fill in the details which have been glossed over in the
architectural design. The intention is that the design should be detailed enough to provide a good
guide for actual coding, including details of any particular algorithms to be used.

## Principles

* The design process should not suffer from "tunnel vision." A good designershould consider
  alternative approaches, judging each based on the requirements of the problem, the resources
  available to do the job.
* The design should be traceable to the analysis model. Because a single element of the design model
  can often be traced back to multiple requirements, it is necessary to have a means for tracking
  how requirements have been satisfied by the design model.
* The design should not reinvent the wheel. Systems are  constructed using a set of design patterns,
  many of which have likely been encountered before. These patterns should always be chosen as an
  alternative to reinvention. Time is short and resources are limited; design time should be
  invested in representing (truly new) ideas by integrating patterns that already exist (when
  applicable).
* The design should "minimize the intellectual distance" between the software and the problem as it
  exists in the real world. That is, the structure of the software design should, whenever possible,
  mimic the structure of the problem domain.
* The design should exhibit uniformity and integration. A design is uniform if it appears fully
  coherent. In order to achieve this outcome, rules of style and format should be defined for a
  design team before design work begins. A design is integrated if care is taken in defining
  interfaces between design components.
* The design should be structured to accommodate change. The design concepts discussed in the next
  section enable a design to achieve this principle.
* The design should be structured to degrade gently, even when aberrant data, events, or operating
  conditions are encountered. Well- designed software should never "bomb"; it should be designed to
  accommodate unusual circumstances, and if it must terminate processing, it should do so in a
  graceful manner.
* Design is not coding, coding is not design. Even when detailed procedural designs are created for
  program components, the level of abstraction of the design model is higher than the source code.
  The only design decisions made at the coding level should address the small implementation details
  that enable the procedural design to be coded.
* The design should be assessed for quality as it is being created, not after the fact. A variety of
  design concepts and design measures are available to assist the designer in assessing quality
  throughout the development process.
* The design should be reviewed to minimize conceptual (semantic) errors. There is sometimes a
  tendency to focus on minutiae when the design is reviewed, missing the forest for the trees. A
  design team should ensure that major conceptual elements of the design (omissions, ambiguity,
  inconsistency) have been addressed before worrying about the syntax of the design model.

### Tools

* It's important to create an initial design for the Models following a
  [Domain Model](https://www.uml-diagrams.org/examples/hospital-domain-diagram.html)
  diagram or a
  [Entity Relationship](https://www.smartdraw.com/entity-relationship-diagram/)
  diagram.
* We use [Gliffy](https://www.gliffy.com/) for making design documents.
* We beleive those diagrams can be hard to maintain as code progresses so
  we chose to use them initially, and mantain the minimum amount possible of
  documentation.

### Aspects in software design

There are many aspects to consider in the design of a piece of software. The
importance of each consideration should reflect the goals and expectations that
the software is being created to meet. Some of these aspects are:

* Compatibility - The software is able to operate with other products that are
  designed for interoperability with another product.
* Extensibility - New capabilities can be added to the software without major
  changes to the underlying architecture.
* Modularity - the resulting software comprises well defined, independent
  components which leads to better maintainability. The components could be then
  implemented and tested in isolation before being integrated to form a desired
  software system.
* Fault-tolerance - The software is resistant to and able to recover from
  component failure.
* Maintainability - A measure of how easily bug fixes or functiona
  modifications can be accomplished.
* Reliability - The software is able to perform a required function under stated
  conditions for a specified period of time.
* Reusability - The ability to use some or all of the aspects of the preexisting
  software in other projects with little to no modification.
* Robustness - The software is able to operate under stress or tolerate
  unpredictable or invalid input.
* Security - The software is able to withstand and resist hostile acts and
  influences.
* Usability - The software user interface must be usable for its target
  user/audience.
* Performance - The software performs its tasks within a time-frame that is
 acceptable for the user, and does not require too much memory.
* Portability - The software should be usable across a number of different
  conditions and environments.
* Scalability - The software adapts well to increasing data or number of users.

## References

* ["Do one thing and do it well"
  Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)
* [You aren't gonna need it](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)
* [SOLID](https://en.wikipedia.org/wiki/SOLID_(object-oriented_design))
* [GRASP](https://en.wikipedia.org/wiki/GRASP_(object-oriented_design))
* [Software Design](https://en.wikipedia.org/wiki/Software_design)