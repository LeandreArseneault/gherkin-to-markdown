from gherkin_to_markdown.expressions.expression import Expression


class EmptyExpression(Expression):
    def to_markdown(self, statement: str):
        return None
