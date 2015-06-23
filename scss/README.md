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
- [SCSS Linter](https://github.com/brigade/scss-lint)
- [SCSS Depth](https://smacss.com/book/applicability)
- [](http://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/)

**[⬆ back to top](#table-of-contents)**
