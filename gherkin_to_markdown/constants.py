from expressions.indented_text_expression import IndentedTextExpression
from expressions.code_block_expression import CodeBlockExpression
from gherkin_to_markdown.expressions.background_expression import BackgroundExpression
from gherkin_to_markdown.expressions.empty_expression import EmptyExpression
from gherkin_to_markdown.expressions.example_expression import ExampleExpression
from gherkin_to_markdown.expressions.first_header_expression import FirstHeaderExpression
from gherkin_to_markdown.expressions.second_header_expression import SecondHeaderExpression
from gherkin_to_markdown.expressions.step_expression import StepExpression
from gherkin_to_markdown.expressions.table_line_expression import TableLineExpression
from gherkin_to_markdown.expressions.table_title_expression import TableTitleExpression

KEYWORD_TO_EXPRESSION = {
    "Given": StepExpression,
    "When": StepExpression,
    "Then": StepExpression,
    "And": StepExpression,
    "But": StepExpression,
    "*": StepExpression,
    "": EmptyExpression,
    "#": EmptyExpression,
    "Feature": FirstHeaderExpression,
    "Scenario": SecondHeaderExpression,
    "Scenario Outline": SecondHeaderExpression,
    "Scenario Template": SecondHeaderExpression,
    "Background": BackgroundExpression,
    '"""': CodeBlockExpression,
    "```": CodeBlockExpression,
    "Examples": ExampleExpression,
    "Table title": TableTitleExpression,
    "Table line": TableLineExpression,
    "Indented text": IndentedTextExpression
}
