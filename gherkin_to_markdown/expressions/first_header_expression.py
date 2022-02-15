from gherkin_to_markdown.expressions.expression import Expression


class FirstHeaderExpression(Expression):
    def to_markdown(self, statement: str):
        return f"#{statement.strip().replace(':', '', 1)[len(self.keyword):]}\n\n"
