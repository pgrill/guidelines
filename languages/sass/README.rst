SASS Guidelines
---------------

Ruleset
=======

* Use single quotes.
* Each selector on a new line.
* Don't use ``#ids`` in selectors.
* The opening brace (``{``) spaced from the last selector by a single space.
* Each declaration on its own new line.
* A space after the colon (``:``).
* Trailing semi-colon (``;``) at the end of all declarations.
* The closing brace (``}``) on its own new line.
* A new line after the closing brace ``}``.
* Use 2 speaces for indentation.
* Force ``@charset 'utf-8';`` in the main stylesheet.
* Sort properties by name.
* Write comments.
* Comment the code using `SassSoc <http://sassdoc.com/>`__.
* Use multiple lines comments ``/* ... */``` if you want to preserve the comments.
* Extend from `%placeholders <http://blog.teamtreehouse.com/extending-placeholder-selectors-with-sass/>`__, never from a class.
* Don't abuse extend a placeholder in order to avoid side effects.
* Lines as possible, shorter than 80 characters. You can split them into several lines when necessary.
* Use colors expressed in HSL when possible, then RGB, then hexadecimal.
* Use media queries inside the selector.
* Use pseudo-elements ``::after`` and ``::before`` if you don't need link a action.
* Generate source map just for develop propose.
* Use the flag ``!default`` in public libraries to safely override.
* Don't use the flag ``!global`` for root declarations.

Naming
======

* Filenames: Use lowercase with dashes.
* Classes: Use `BEM <http://getbem.com/naming/>`__.
* Functions: All lowercase with dashes. ``@function my-function() { ...``
* Mixins: All lowercase with dashes. ``@mixin my-mixin() { ...``
* Variables: All lowercase with dashes. ``$my-variable = 50;``
* Constants: All-caps snakerized. ``$POSITIONS = (top, right, bottom, left)``
* Namespace: Prefix variables, mixins, functions, etc. by an abbreviation of the project.


Declarations
============

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


Architecture
============

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As you can see this divides the project into three basic types of files:
Modules, partials, and vendored stylesheets.

* The modules directory is reserved for Sass code that doesn't cause Sass to
  actually output CSS. Things like mixin declarations, functions, and variables.
* The partials directory is where the meat of my CSS is constructed.
* The vendor directory is for third-party CSS. This is handy when using
  prepackaged components developed by other people (or for your own components that are maintained in another project). jQuery UI and a color picker are examples of CSS that you might want to place in the vendor directory. As a general rule I make it a point not to modify files in my vendor directory. If I need to make modifications I add those after the vendored files are included in my primary stylesheet. This should make it easy for me to update my third-party stylesheets to more current versions in the future.



Inspiration & Sources
=====================

* `Sass Guidelines <https://sass-guidelin.es>`__
* `How to structure a sass project <http://thesassway.com/beginner/how-to-structure-a-sass-project>`__
* `Css-Tricks <https://css-tricks.com/sass-style-guide/>`__
* `SCSS Linter <https://github.com/brigade/scss-lint>`__
* `SCSS Depth <https://smacss.com/book/applicability>`__
* `Mindbemding getting your head round-bem syntax <http://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/>`__
