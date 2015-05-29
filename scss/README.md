# SASS

## Table of Contents
1. -
1. -
1. -
1. -


## Rules

- Don't use #ids

- Order
```sass
.class-with-dahses {
    @extends ...
    @include ...

    // regular styles [a-z]

    // pseudo classes
    &:hover {
    }
    &:first-child {
    }

    // pseudo elements
    &::after {
    }

    // selectors
    & > ... {
    }

}
```

**[⬆ back to top](#table-of-contents)**

## Inspiration
- [Css-Tricks](https://css-tricks.com/sass-style-guide/)

**[⬆ back to top](#table-of-contents)**
