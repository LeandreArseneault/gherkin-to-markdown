from typing import List

from gherkin_to_markdown.constants import KEYWORD_TO_EXPRESSION


class GherkinParser:
    def __init__(self, lines: List[str]):
        self.lines = lines
        self.in_a_table = False
        self.in_a_docstring = False
        self.current_docstring_indent = 0

    def to_markdown(self) -> str:
        output: str = ""
        for line in self.lines:
            result = self._parse_line(line)
            if result is not None:
                output += result
        return output

    def _parse_line(self, line: str) -> str:
        keyword = self._get_keyword(line)

        if keyword in KEYWORD_TO_EXPRESSION:
            return KEYWORD_TO_EXPRESSION[keyword](keyword).to_markdown(line[self.current_docstring_indent:])
        else:
            return line[self.current_docstring_indent:] + "\n\n"

    def _get_keyword(self, line: str) -> str:
        stripped_line = line.strip()
        keyword = next((word for word in stripped_line.split(" ") if word != ""), "").replace(":", "")
        if keyword.startswith('"""') or keyword.startswith("```"):
            keyword = '"""'
            self.current_docstring_indent = len(line) - len(line.lstrip()) if not self.in_a_docstring else 0
            self.in_a_docstring = not self.in_a_docstring
        elif keyword == "Scenario":
            keyword = stripped_line.split(":")[0]
        elif keyword == "|":
            if self.in_a_table:
                keyword = "Table line"
            else:
                keyword = "Table title"
                self.in_a_table = True
        elif self.in_a_docstring:
            return "Indented text"
        else:
            self.in_a_table = False
        return keyword
