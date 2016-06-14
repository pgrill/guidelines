Table of Contents
=================

1. `Principles`_
#. `Rule Formatting`_
#. `File Structure`_
#. `Inspiration & Sources`_

Principles
==========

* Don't use ``#ids`` in rule selectors.
* Use one line per rule selector.
* Use lowercase with dashes for class name and add an space between
  the name and the bracket.
* Use 2 speaces for indentation.
* Use lowercase with dashes for filenames.


Rule Formatting
===============

.. code:: scss

    .rule-formatting {
        // 1. Extends
        @extend %foo;

        // 2. Includes
        @include bar(foo);

        // 3. Properties order by name
        display: block;
        z-index: 10;
        ...

        // 4. Media queries
        @media #{$mobile} {
            ...
        }

        @media #{$tablet} {
            ...
        }

        // 5. Pseudo classes
        &:hover {
            ...
        }

        &:first-child {
            ...
        }

        // 6. Pseudo elements
        &::after {
            ...
        }

        &::before {
            ...
        }

        // 7. Selectors
        & > ... {
            ...
        }

        & ... {
            ...
        }
    }


File Structure
==============

.. code:: text

    ├── base
    │   ├── modules
    │   │   └── _all.scss
    │   ├── partials
    │   │   └── _....scss
    │   ├── vendor
    │   │   └── _....scss
    │   ├── _base.scss
    │   └── _page.scss
    ├── desktop
    │   ├── modules
    │   │   └── _all.scss
    │   ├── partials
    │   │   └── _....scss
    │   ├── vendor
    │   │   └── _....scss
    │   ├── base.scss
    │   └── page.scss
    ...

Modules, partials, and vendor
-----------------------------

As you can see this divides the project into three basic types of files: 
Modules, partials, and vendored stylesheets.

* The modules directory is reserved for Sass code that doesn't cause Sass to 
  actually output CSS. Things like mixin declarations, functions, and variables.
* The partials directory is where the meat of my CSS is constructed.
* The vendor directory is for third-party CSS. This is handy when using 
  prepackaged components developed by other people (or for your own components that are maintained in another project). jQuery UI and a color picker are examples of CSS that you might want to place in the vendor directory. As a general rule I make it a point not to modify files in my vendor directory. If I need to make modifications I add those after the vendored files are included in my primary stylesheet. This should make it easy for me to update my third-party stylesheets to more current versions in the future.



Inspiration & Sources
=====================

* `How to structure a sass project <http://thesassway.com/beginner/how-to-structure-a-sass-project>`__
* `Css-Tricks <https://css-tricks.com/sass-style-guide/>`__
* `SCSS Linter <https://github.com/brigade/scss-lint>`__
* `SCSS Depth <https://smacss.com/book/applicability>`__
* `Mindbemding getting your head round-bem syntax <http://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/>`__
