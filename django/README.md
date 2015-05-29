# Django

**[⬅ back to index](./)**

## Table of Contents
1. -
1. -
1. -
1. -

## Files

```
py: lowercase_with_underscores.py
html: lowercase_with_underscores.html
javascript: lowercase-with-dashes.js
images: lowercase-with-dashes.*
css/scss: lowercase-with-dashes.* 

//with the exception of partials, which start with underscore
scss partials: _lowercase-with-dashes.scss
```

**[⬆ back to top](#table-of-contents)**

## Templates
- Name blocks with lowercase and underscores.
```html
{% block lowercase_with_underscores %}
```

- In endblocks, add the name of the block they close.
```htmldjango
{% block foo_bar %}
    ...
{% endblock foo_bar %}
```

- Indent everything within template tags.
```djangohtml
{% block foo_bar %}
    <html-tag></html-tag>
        {% if foo %}
            <html-tag></html-tag>
        {% else %}
            <html-tag></html-tag>
        {% endif %}    ...
{% endblock foo_bar %}
```

**[⬆ back to top](#table-of-contents)**

## Books
 - Django Two Scoops

**[⬆ back to top](#table-of-contents)**
