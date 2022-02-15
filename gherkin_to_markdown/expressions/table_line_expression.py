from gherkin_to_markdown.expressions.expression import Expression


class TableLineExpression(Expression):
    def to_markdown(self, statement: str):
        return statement.strip() + "\n"
