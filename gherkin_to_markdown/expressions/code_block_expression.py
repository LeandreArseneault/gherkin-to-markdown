from gherkin_to_markdown.expressions.expression import Expression


class CodeBlockExpression(Expression):
    def to_markdown(self, statement: str):
        return f"{statement.strip().replace(self.keyword, '```', 1)}\n"
