from gherkin_to_markdown.expressions.expression import Expression


class BackgroundExpression(Expression):
    def to_markdown(self, statement: str):
        return f"## {self.keyword}\n\n"
