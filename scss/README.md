# SASS

## Table of Contents
1. -
1. -
1. -
1. -


## Rules

- Don't use `#ids`

- Name classes with dashes and have an space between the name and the bracket.

    ```scss
.class-with-dahses {
    //styles
}
    ```

- Order

```sass
.class-with-dahses {
    // Variable definition
    $foo: #636363;
    $bar: 3.3em;

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
}
    ```

**[⬆ back to top](#table-of-contents)**

## Inspiration
- [Css-Tricks](https://css-tricks.com/sass-style-guide/)
- [SCSS Linter](https://github.com/brigade/scss-lint)
- [SCSS Depth](https://smacss.com/book/applicability)
- [](http://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/)

**[⬆ back to top](#table-of-contents)**
