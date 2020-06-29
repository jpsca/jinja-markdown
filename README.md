
# Jinja-Markdown

[![Tests](https://travis-ci.org/jpsca/jinja_markdown.svg)](https://travis-ci.org/jpsca/jinja_markdown/)

A jinja2 extension that adds a `{% markdown %}` tag powered with [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/).


## Installation

```
pip install jinja_markdown
```

## Usage

```python
jinja_env = Environment(extensions=['jinja_markdown.MarkdownExtension'])
```

or

```python
from jinja_markdown import MarkdownExtension

jinja_env.add_extension(MarkdownExtension)
```

Then your templates can contain Markdown inside `{% markdown %}` / `{% endmarkdown %}` block tags.

```html+jinja
<article>
{% markdown %}
# Heading
Regular text

    print("Hello world!")
{% endmarkdown %}
</article>
```

## About indentation

To avoid issues is recommended that you don't indent the markdown code inside the tag.
If you prefer do it anyway, make sure the first line has the baseline indentation level.

```html+jinja
<!-- Supported but not recommended -->
<article>
    {% markdown %}
    # Baseline of identation
    Regular paragraph
    
        This will be interpreted as code
</article>
```
