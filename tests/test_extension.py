from jinja2 import Environment

from jinja_markdown import MarkdownExtension


SOURCE = """
<article>
    {% markdown %}
    # Heading
    Regular text

    ```python
    pass
    ```
    {% endmarkdown %}
</article>
"""

EXPECTED = """
<article>
    <h1>Heading</h1>
<p>Regular text</p>
<div class="highlight"><pre><span></span><code><span class="k">pass</span>
</code></pre></div>
</article>"""


def test_render_markdown():
    jinja_env = Environment(extensions=[MarkdownExtension])
    tmpl = jinja_env.from_string(SOURCE)
    output = tmpl.render()
    print(output)
    assert output == EXPECTED
