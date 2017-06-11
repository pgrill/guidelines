Django Guidelines
-----------------


Resources
=========

#. `Django Two Scoops <http://twoscoopspress.org/>`__ (book)
#. `Writing your first Django app <https://docs.djangoproject.com/en/stable/intro/tutorial01/>`__
#. `Awesome Django <https://gitlab.com/rosarior/awesome-django>`__
#. `Django packages <https://djangopackages.org/>`__


Training
========

#. `Ticketing system <./training/ticketing-system.rst>`__


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

-  Avoid block names on inline block tags.

-  Multiline blocks should have the block name in start and end tags.

   .. code:: html

        {% block foo_bar %}
            ...
        {% endblock foo_bar %}

-  Indent everything within template tags for readability. Remember django templates are for the developers to read, the rendered result is for browsers.

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
            import myapp.signals.handlers  # noqa


Tests
=====

Visit the `testing page <./test.rst>`__.
