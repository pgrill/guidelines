# Django

**[⬅ back to index](./)**

## Table of Contents
1. [Read](#Read)
1. [Files](#Files)
1. [Templates](#Templates)
1. [Signals](#Signals)
1. [Books](#Books)

## Read
[Django Two Scoops](http://twoscoopspress.org/), Now.


## Files

```yaml
py: lowercase_with_underscores.py
html: lowercase_with_underscores.html
javascript: lowercase-with-dashes.js
images: lowercase-with-dashes.*
css/scss: lowercase-with-dashes.*

# With the exception of partials, which start with underscore
scss partials: _lowercase-with-dashes.scss
```

**[⬆ back to top](#table-of-contents)**

## Templates
- Name blocks with lowercase and underscores.

```html
{% block lowercase_with_underscores %}
{% endbblock lowercase_with_underscore %}
```

- If the block/endblock is inline you should avoid the name on the endblock.

- In endblocks, add the name of the block they close.
```html
{% block foo_bar %}
    ...
{% endblock foo_bar %}
```

- Indent everything within template tags.
```html
{% block foo_bar %}
    <html-tag></html-tag>
    {% if foo %}
        <html-tag></html-tag>
    {% else %}
        <html-tag></html-tag>
    {% endif %}
{% endblock foo_bar %}
```

**[⬆ back to top](#table-of-contents)**

## Signals
```bash
app/signals/__init__.py # Define new signals
app/signals/handlers.py # Define handlers
```

```python
from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    ...

    def ready(self):
        import app.signals.handlers  # noqa
```

**[⬆ back to top](#table-of-contents)**

## Books
 - [Django Two Scoops](http://twoscoopspress.org/)

**[⬆ back to top](#table-of-contents)**
