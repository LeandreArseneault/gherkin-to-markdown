from gherkin_to_markdown.expressions.expression import Expression


class IndentedTextExpression(Expression):
    def to_markdown(self, statement: str):
        return f"{statement}"
