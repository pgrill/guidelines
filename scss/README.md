# SASS

Don't use #ids

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

## Inspiration
* Css-Tricks: https://css-tricks.com/sass-style-guide/
