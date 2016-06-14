Table of Contents
=================

1. `Books`_
2. `Documentation`_
3. `Coding Style`_


Books
=====

#. `The C++ Programming Language (4th Edition) <http://www.stroustrup.com/4th.html>`__


Documentation
=============

Use `doxygen <http://www.stack.nl/~dimitri/doxygen/>`__ for generating
documentation from annotated source code.


Coding Style
============

Naming Conventions
^^^^^^^^^^^^^^^^^^

#. **Types** must be in ``UpperCamelCase``.

   .. code-block:: c++

       class FileSystem { };
       struct User { };

#. **Variables** must be in ``lowerCamelCase``.

   .. code-block:: c++

       int userCount;
       int balance;

#. **Functions** must be verbs written in ``lowerCamelCase``.

   .. code-block:: c++

       int computeTotal();
       void clear();

#. **Namespaces** must be written in ``lowercase``.

   .. code-block:: c++

       namespace io { };
       namespace math { };
