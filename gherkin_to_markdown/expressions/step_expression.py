import re

from gherkin_to_markdown.expressions.expression import Expression


class StepExpression(Expression):
    def to_markdown(self, statement: str):
        return f"_{self.keyword}_" \
               f"{re.sub(r'(<.*>)',convert_variable_to_bold_markdown, statement.strip()[len(self.keyword):])}\n\n"


def convert_variable_to_bold_markdown(variable_string):
    return variable_string.group().replace("<", "**").replace(">", "**")
