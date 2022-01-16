import textwrap
import typing as t

import markdown
from jinja2.ext import Extension
from jinja2.nodes import CallBlock

if t.TYPE_CHECKING:
    from jinja2 import Environment
    from jinja2.nodes import Node
    from jinja2.parser import Parser


__all__ = ["EXTENSIONS", "MarkdownExtension"]

EXTENSIONS = [
    "admonition",
    "attr_list",
    "codehilite",
    "smarty",
    "tables",
    "pymdownx.betterem",
    "pymdownx.caret",
    "pymdownx.details",
    "pymdownx.emoji",
    "pymdownx.keys",
    "pymdownx.magiclink",
    "pymdownx.mark",
    "pymdownx.smartsymbols",
    "pymdownx.superfences",
    "pymdownx.tabbed",
    "pymdownx.tasklist",
    "pymdownx.tilde",
]


class MarkdownExtension(Extension):
    tags = set(["markdown"])

    def __init__(self, environment: "Environment") -> None:
        super(MarkdownExtension, self).__init__(environment)
        self.markdowner = markdown.Markdown(extensions=EXTENSIONS)
        environment.extend(markdowner=self.markdowner)

    def parse(self, parser: "Parser") -> t.Union["Node", t.List["Node"]]:
        lineno = next(parser.stream).lineno
        body = parser.parse_statements(
            ("name:endmarkdown", ),
            drop_needle=True
        )
        return CallBlock(
            self.call_method("_render_markdown"),
            [],
            [],
            body
        ).set_lineno(lineno)

    def _render_markdown(self, caller: t.Callable) -> str:
        text = caller()
        text = self._dedent(text)
        return self.markdowner.convert(text)

    def _dedent(self, text: str) -> str:
        return textwrap.dedent(text.strip("\n"))
