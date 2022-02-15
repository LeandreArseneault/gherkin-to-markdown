from gherkin_to_markdown.expressions.expression import Expression


class TableTitleExpression(Expression):
    def to_markdown(self, statement: str):
        statement = statement.strip()
        return statement + "\n" + "|".join("-"* len(t) for t in statement.split("|")) + "\n"
