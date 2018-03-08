# Angular guidelines

## Learning Resources

- [Shaping up with Angular 1.5](https://www.codeschool.com/courses/shaping-up-with-angularjs)
- [Angular 1.5 at Pluralsight](https://app.pluralsight.com/paths/skills/an/angular-js)

## Coding Style

### Rules

#### Modules

- Your main application module should be in your root client directory.
- Modules should reference other modules using the Angular Module's "name" property

```js
// file submodulea.js:
  goog.provide('my.submoduleA');
  my.submoduleA = angular.module('my.submoduleA', []);
// ...
// file app.js
  goog.require('my.submoduleA');
  my.application.module = angular.module('hello', [my.submoduleA.name]);
// ...
```

#### Controllers and Scopes

- Controllers are classes. Methods should be defined on MyCtrl.prototype.

```js
/**
 * Home controller.
 *
 * @constructor
 * @ngInject
 * @export
 */
hello.mainpage.HomeCtrl = function() {
  /**
   * @type {string}
   * @export
   */
  this.myColor = 'blue';
};


/**
 * @param {number} a
 * @param {number} b
 * @export
 */
hello.mainpage.HomeCtrl.prototype.add = function(a, b) {
  return a + b;
};
```

```html
<div ng-controller="hello.mainpage.HomeCtrl as homeCtrl"/>
  <span ng-class="homeCtrl.myColor">I'm in a color!</span>
  <span>{{homeCtrl.add(5, 6)}}</span>
</div>
```

#### Directives

- All DOM manipulation should be done inside directives. Directives should be kept small and use composition.

### Naming Conventions

We recommend follow the naming conventions proposed by [Angular Naming Guidelines](https://angular.io/guide/styleguide#general-naming-guidelines)

## References

- [Google AngularJS Style Guideline](https://google.github.io/styleguide/angularjs-google-style.html)
- [Angular Styleguide](https://angular.io/guide/styleguide)