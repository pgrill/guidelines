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

File Names
^^^^^^^^^^

#. **Headers**

   Header files should be named with ``snake_case`` and use the ``.hpp``
   extension for C++ headers, and ``.h`` for plain C headers.

   - ``file_system.hpp``
   - ``array_view.hpp``
   - ``unused.hpp``

Naming Conventions
^^^^^^^^^^^^^^^^^^

#. **Types** must be in ``UpperCamelCase``.

    .. code-block:: c++

        class FileSystem { };
        struct User { };

#. **Variables** must be in ``snake_case``.

    .. code-block:: c++

        int user_count;
        int balance;

    Member variables must have a ``m_`` prefix.

    .. code-block:: c++

        char* m_buffer;

#. **Functions** must be verbs written in ``snake_case``.

   .. code-block:: c++

       int compute_total();
       void clear();

#. **Namespaces** must be written in ``lowercase``.

   .. code-block:: c++

       namespace io { };
       namespace math { };

Syntax
^^^^^^

#. **Braces**

   Each brace occupies its own line:

   .. code-block:: c++

       if (condition)
       {
           x++;
       }

       for (const auto& variable : iterable)
       {
           x++;
       }

       while (condition)
       {
           x++;
       }

       switch (something)
       {
       case Something:
           break;
       }

       void do_something()
       {
           x++;
       }

       class Class
       {
       public:
           int m_x;
       };

       // Extra braces inside a function also follow this convention
       void do_something()
       {
           {
               // Another Scope
               int x;
               x++;
           }
       }


   Namespaces are an exception to the above:

   .. code-block:: c++

       namespace sophi {

       // Stuff inside the namespace block has the same indentation as
       // the block itself;
       x++;

       } /* sophi */


   The final ``/* sophi */`` comment is mandatory.
