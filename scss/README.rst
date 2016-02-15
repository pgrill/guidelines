SASS
====

Table of Contents
-----------------

1.

   -

2.

   -

3.

   -

4.

   -

Rules
-----

-  Don't use ``#ids``

-  Name classes with dashes and have an space between the name and the
   bracket.

   .. code:: scss

       .class-with-dahses {
       //styles
       }

-  Order

\`\`\`sass .class-with-dahses { // Variable definition $foo: #636363;
$bar: 3.3em;

::

    // Includes and extends
    @extend .foo;
    @include bar(10%);

    // Regular properties [a-z]
    background-color: $foo;
    display: block;
    height: $bar;
    width: $bar;
    z-index: 6;

    // media queries
    @media #{$mobile}{
    }
    @media #{$tablet}{
    }

    // pseudo classes
    &:hover {
    }
    &:first-child {
    }

    // pseudo elements
    &::after {
    }
    &::before {
    }

    // selectors
    & > ... {
    }

} \`\`\`

-**`⬆ back to top <#table-of-contents>`__**

Inspiration
-----------

-  `Css-Tricks <https://css-tricks.com/sass-style-guide/>`__
-  `SCSS Linter <https://github.com/brigade/scss-lint>`__
-  `SCSS Depth <https://smacss.com/book/applicability>`__
-  ` <http://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/>`__

-**`⬆ back to top <#table-of-contents>`__**