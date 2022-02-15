from gherkin_to_markdown.expressions.expression import Expression


class ExampleExpression(Expression):
    def to_markdown(self, statement: str):
        return f"### {self.keyword}\n\n"
