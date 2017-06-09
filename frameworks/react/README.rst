React
-----

Project structure
=================

Our usual structure is built around the Flux pattern, so we have specific
folders for our actions, components, reducers and stores. Redux is the Flux
implementation we normally use, so our :code:`stores` directory is called 
:code:`store` instead.

.. code:: bash

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
    
Naming
^^^^^^
- **Extensions:** Use :code:`.js` extensions even for React components.
-  **Reference naming:**: Use PascalCase for React components and camelCase for their instances:

.. code:: js

    import WorkbenchItem from './WorkbenchItem';
    const workbenchItem = <WorkbenchItem />;

        

Components
==========

**Presentational and Container Components**

We follow the "Presentational and Container Components" pattern, where all our
components fall in one of those two categories. Files inside the 
:code:`components` directory can be organized within sub-directories using
the structure you see more fit, but each component must live in a file of its 
own and container components' files must be in the :code:`containers` directory.

**The render method**

The :code:`render` method of your React components must not include arrow 
functions or bindings. Doing so causes new objects to be created every time
the component re-renders which results in more work for the garbage collector.

Instead, write your arrow functions as members of your component and use
references to these members inside the :code:`render` method.

State
=====

**Slices' names**

Every slice of the state that you manage in a separate reducer should have a
name defined in the reducer's file and exported as a constant. Use this 
constant everywhere you need to access the state as a whole to avoid 
hard-coding the slice name.

For example, in your home page reducer you have:

.. code:: javascript

    export const sliceName = 'homePage';
    
    export const homePageReducer = (state = initialState, action) => {
        switch (action.type) {
        ...
        
And then use this constant when you need to access specific slices of your
state outside the reducer. For example, in the home page actions file:

.. code:: javascript

    import { sliceName } from '../reducers/home-page';
    
    function fetchData () {
        return function (dispatch, getState) {
            currentData = getState()[sliceName].data
            ...
            
**Initial state**

The initial state of each slice should be defined as a constant as well. Every
state reduction that somehow sets a member of the state to its initial value
can benefit from this approach, especially when the number of action types in
your app starts to grow.

If you sync your state to a storage or do server-side rendering, having the
initial state in a constant will turn out to be particularly helpful.

Styles
======

Be consistent with your styles: either use CSS or inline styles in Javascript,
but not both. Third party stylesheets (like :code:`normalize.css`) are an
exception to this rule.

**Inline styles**

Your inline styles must live in their own files or in the component's file. If
you're going with the second approach, put all the rules in an easily 
identifiable :code:`styles` constant at the top of your component.

Testing
=======

We recommend using Jest along with Airbnb's :code:`enzyme` library in order to make efficient reducer and component tests.
Each test should live in each component directory and should have the name of the component plus :code:`.test.js`.
We use the :code:`expect` module from :code:`chai` in order to compare values.

**Reducer testing**

As the reducers are pure functions, they are very easy to test. You just have to make sure that if you call the function with a state :code:`x` and an action :code:`y`, you get a new state :code:`z`.

**Component testing**

We use shallow rendering in order to test React components in an efficient way.

.. code:: javascript
    
    import { expect } from 'chai';
    import { shallow } from 'enzyme';

    describe('<MyComponent />', () => {

      it('should render three <Foo /> components', () => {
        const wrapper = shallow(<MyComponent />);
        expect(wrapper.find(Foo)).to.have.length(3);
      });

      it('should render an `.icon-star`', () => {
        const wrapper = shallow(<MyComponent />);
        expect(wrapper.find('.icon-star')).to.have.length(1);
      });

      it('should render children when passed in', () => {
        const wrapper = shallow(
          <MyComponent>
            <div className="unique" />
          </MyComponent>
        );
        expect(wrapper.contains(<div className="unique" />)).to.equal(true);
      });

      it('simulates click events', () => {
        const onButtonClick = sinon.spy();
        const wrapper = shallow(
          <Foo onButtonClick={onButtonClick} />
        );
        wrapper.find('button').simulate('click');
        expect(onButtonClick.calledOnce).to.equal(true);
      });

    });
    
    

