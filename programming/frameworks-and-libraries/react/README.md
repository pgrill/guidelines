# React guidelines

TDB: Write React introduction

## Resources

1. [Tutorial](https://reactjs.org/tutorial/tutorial.html)
2. [Udemy's "Modern React with Redux"](https://www.udemy.com/react-redux/)
3. Check the monthly Beginner's Thread at [/r/reactjs](https://www.reddit.com/r/reactjs/)

## Project structure

Our usual structure is built around the Flux pattern, so we have
specific folders for our actions, components, reducers and stores. Redux
is the Flux implementation we normally use, so our `stores`{.sourceCode}
directory is called `store`{.sourceCode} instead.

```text
project
├── config
│   ├── env.js
│   ├── jest
│   │   ├── cssTransform.js
│   │   └── fileTransform.js
│   ├── paths.js
│   ├── polyfills.js
│   ├── webpack.config.dev.js
│   ├── webpack.config.prod.js
│   └── webpackDevServer.config.js
├── public
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
├── scripts
│   ├── build.js
│   ├── start.js
│   └── test.js
├── src
│   ├── actions
│   │    └── example.js
│   ├── components
│   │   └── SomeComponent
│   │       ├── SomeComponent.css
│   │       ├── SomeComponent.js
│   │       └── SomeComponent.test.js
│   ├── containers
│   │   └── SomeContainer
│   │       ├── SomeContainer.css
│   │       └── SomeContainer.js
│   ├── store
│   ├── reducers
│   │    ├── index.js
│   │    └── example.js
│   ├── registerServiceWorker.js
│   ├── constants.js
│   └── index.js
├── package.json
├── yarn.lock
└── README.md
```

### Naming

- **Extensions:** Use `.js`{.sourceCode} extensions even for React
  components.
- **Reference naming:**: Use PascalCase for React components and
  camelCase for their instances:

```javascript
import WorkbenchItem from './WorkbenchItem';
const workbenchItem = <WorkbenchItem />;
```

## Components

### Presentational and Container Components

We follow the "Presentational and Container Components" pattern, where
all our components fall in one of those two categories. Files inside the
`components`{.sourceCode} directory can be organized within
sub-directories using the structure you see more fit, but each component
must live in a file of its own and container components' files must be
in the `containers`{.sourceCode} directory.

### The render method

The `render`{.sourceCode} method of your React components must not
include arrow functions or bindings. Doing so causes new objects to be
created every time the component re-renders which results in more work
for the garbage collector.

Instead, write your arrow functions as members of your component and use
references to these members inside the `render`{.sourceCode} method.

## State

### Slices' Names

Every slice of the state that you manage in a separate reducer should
have a name defined in the reducer's file and exported as a constant.
Use this constant everywhere you need to access the state as a whole to
avoid hard-coding the slice name.

For example, in your home page reducer you have:

```javascript
export const sliceName = 'homePage';

export const homePageReducer = (state = initialState, action) => {
    switch (action.type) {
    ...
```

And then use this constant when you need to access specific slices of
your state outside the reducer. For example, in the home page actions
file:

```javascript
import { sliceName } from '../reducers/home-page';

function fetchData () {
    return function (dispatch, getState) {
        currentData = getState()[sliceName].data
        ...
```

### Initial state

The initial state of each slice should be defined as a constant as well.
Every state reduction that somehow sets a member of the state to its
initial value can benefit from this approach, especially when the number
of action types in your app starts to grow.

If you sync your state to a storage or do server-side rendering, having
the initial state in a constant will turn out to be particularly
helpful.

## Styles

Be consistent with your styles: either use CSS or inline styles in
Javascript, but not both. Third party stylesheets (like
`normalize.css`{.sourceCode}) are an exception to this rule.

### Inline styles

Your inline styles must live in their own files or in the component's
file. If you're going with the second approach, put all the rules in an
easily identifiable `styles`{.sourceCode} constant at the top of your
component.