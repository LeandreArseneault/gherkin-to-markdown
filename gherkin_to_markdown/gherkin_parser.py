import os
import sys
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
            output += self._parse_line(line)
        return output

    def _parse_line(self, line: str) -> str:
        keyword = self._get_keyword(line)

        extra_text = ""
        if keyword != "Table line" and keyword != "Table title" and self.in_a_table is True:
            extra_text += "\n"
            self.in_a_table = False

        if keyword in KEYWORD_TO_EXPRESSION:
            new_line = KEYWORD_TO_EXPRESSION[keyword](keyword).to_markdown(line[self.current_docstring_indent:]) \
                       + extra_text
            return new_line
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
        return keyword


if __name__ == '__main__':
    def convert_file(source_path: str, destination_path: str):
        with open(source_path, "r") as feature_file:
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            with open(destination_path, "w") as output_file:
                markdown_result = GherkinParser(feature_file.readlines()).to_markdown()
                output_file.write(markdown_result)

    args = sys.argv
    source = args[1]
    destination = args[2]

    if os.path.isdir(source):
        for file in os.listdir(source):
            if file.endswith(".feature"):
                convert_file(os.path.join(source, file), os.path.join(destination, file.replace(".feature", ".md")))
    else:
        if os.path.isdir(destination):
            convert_file(source, os.path.join(destination, os.path.basename(source).replace(".feature", ".md")))
        else:
            convert_file(source, destination)
