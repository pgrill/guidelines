React testing guidelines
------------------------

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
