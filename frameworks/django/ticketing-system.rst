Ticketing System
----------------


Purpose
=======

The purpose of this assignment is to learn to design and develop a complete web app using the Django framework.


Requirements
============

Build a web based ticketing system supporting multiple projects, tagging system, signing in with social networks, and reports generation.

Users sign up/sign in to the system and go to their dashboard.
In the header of the page a filter by project will be always present.

From here the user will be able to navigate to different areas of the app.

Views
=====

These are going to be the main views:

Sign up
^^^^^^^

A form requiring First Name, Last Name, Email and Password.

Sign in
^^^^^^^

A form requiring Email and Password.
User should be able to log in with Google, GitHub or Twitter.

Dashboard
^^^^^^^^^

The dashboard shows two lists: one of them lists the tickets assigned to the user, the other one lists the ones created by the user.

Tickets
^^^^^^^

List of tickets with sorting capabilities.
Filters: Assigned user, Status, Tags, Text

Create/View/Edit ticket
^^^^^^^^^^^^^^^^^^^^^^^

Tickets can be created, edited and closed.
They will have the following properties:

#. Project
#. Type (Bug, Story, Task)
#. Status (Open, In Progress, Closed, Invalid)
#. Summary
#. Description
#. Priority (Low, Medium, High, Urgent)
#. Assignee
#. Tags
#. Estimation (in hours)

Users can add comments to a ticket and they will be shown in the ticket details page.

Record progress
^^^^^^^^^^^^^^^

The assigned user of a ticket is able to log hours on it.
Each ticket has a link “log hours”, when clicking a form requiring number of hours invested and a description is shown.

Reports
^^^^^^^

In this view, the user is able to generate a PDF report per project showing the following information:

- Total Hours estimated per week
- Total Hours invested per week
- Total Hours Invested - estimated per week
- Total Tickets opened per week
- Total Tickets closed per week
- Total Tickets Opened - closed per week

For each user in the project:

- Hours estimated per week
- Hours invested per week
- Hours Invested - estimated per week
- Tickets assigned per week
- Tickets closed per week
- Tickets assigned - closed per week

This report should be generated using a background job. When processing is done in the server, the download link becomes available in the front end.

Admin area
==========

The administrator is responsible for managing projects, users and tags in the backend.

Projects
^^^^^^^^

They have a name, a description and users associated.

Tags
^^^^

They have just a name. They can be created, edited and deleted. If deleted, corresponding issues should be updated accordingly.

Non-Functional requirements
===========================

- Follow our `Python <https://guidelines.sophilabs.io/python/>`__ and `Django <https://guidelines.sophilabs.io/django/>`__ guidelines
- Use Virtualenv or Virtualenvwrapper
- Organize the project according to Django Two Scoops Book
- Use Class Based Views
- Use Mixins
- Minify static files
- Use python social auth
- Use celery for background jobs
- Create unit and functional tests, comply with a minimum of 80% of coverage
- Create at least 1 integration test that executes JavaScript functions
- Use the latest stable version of Python and Django
- Comply with pep8 and Django best practices
- Use Sass
- Use Sass & JS linters. See `here <https://guidelines.sophilabs.io/sass/>`__.
- Use the Django Admin app for administrator tasks

Boilerplate project: https://git.sophilabs.io/sophilabs/sophia/tree/dev.

====================================================  ==========
Feature                                               Max Points
Sign up page                                          5
Sign in page with email & password                    5
Sign in page with social networks                     5
Dashboard page                                        5
Global filter by project                              3
List tickets page                                     4
List tickets Sort                                     4
List tickets Filters                                  5
Create/Edit Ticket                                    10
View Ticket                                           3
Comment Ticket                                        4
Log hours to Ticket                                   5
PDF Report Generator using Celery                     10
Admin Area                                            4
Virtualenv + Django last version + pep8 + Two Scoops  6
Class based views + Mixins                            6
80% coverage + unit/integration/functional tests      10
Sass + JS/Sass linters + minify assets                6
====================================================  ==========


Have fun!
