Table of Contents
=================

1. `Books`_
2. `Files`_
3. `Templates`_
4. `Signals`_


Books
=====

#. `Django Two Scoops <http://twoscoopspress.org/>`__


Files
=====

.. code:: yaml

    py: lowercase_with_underscores.py
    html: lowercase_with_underscores.html
    javascript: lowercase-with-dashes.js
    images: lowercase-with-dashes.*
    css: lowercase-with-dashes.*
    scss: lowercase-with-dashes.*
    scss (partials): _lowercase-with-dashes.*


Templates
=========

-  Name blocks with lowercase and underscores.

.. code:: html

    {% block lowercase_with_underscores %}
    {% endbblock lowercase_with_underscore %}

-  If the block/endblock is inline you should avoid the name on the
   endblock.

-  In endblocks, add the name of the block they close.

.. code:: html

    {% block foo_bar %}
        ...
    {% endblock foo_bar %}

-  Indent everything within template tags.

.. code:: html

    {% block foo_bar %}
        <html-tag></html-tag>
        {% if foo %}
            <html-tag></html-tag>
        {% else %}
            <html-tag></html-tag>
        {% endif %}
    {% endblock foo_bar %}


Signals
=======

.. code:: bash

    app/signals/__init__.py # Define new signals
    app/signals/handlers.py # Define handlers

.. code:: python

    from django.apps import AppConfig as BaseAppConfig


    class AppConfig(BaseAppConfig):

        ...

        def ready(self):


Tests
=====

If you want to see how we do tests, please click here_.

.. _here: https://github.com/sophilabs/guidelines/tree/master/python#tdd-unit-tests
