from gherkin_to_markdown.gherkin_parser import GherkinParser


def test_empty_line():
    result: str = GherkinParser([""]).to_markdown()
    assert result == ""


def test_comments():
    result: str = GherkinParser(["# This is a comment"]).to_markdown()
    assert result == ""


def test_feature_name():
    feature_name = "This is a feature for a default scenario outline"
    result: str = GherkinParser([f"Feature: {feature_name}"]).to_markdown()
    assert result == f"# {feature_name}\n\n"


def test_feature_description():
    feature_description = "This is the first line of the feature description."
    result: str = GherkinParser([feature_description]).to_markdown()
    assert result == feature_description + "\n\n"


def test_scenario_name():
    scenario = "This is a default scenario"
    result: str = GherkinParser([f"Scenario: {scenario}"]).to_markdown()
    assert result == f"## {scenario}\n\n"


def test_scenario_outline_name():
    scenario_outline = "This is a default scenario"
    result: str = GherkinParser([f"Scenario Outline: {scenario_outline}"]).to_markdown()
    assert result == f"## {scenario_outline}\n\n"


def test_scenario_template_name():
    scenario_outline = "This is a default scenario"
    result: str = GherkinParser([f"Scenario Template: {scenario_outline}"]).to_markdown()
    assert result == f"## {scenario_outline}\n\n"


def test_scenario_outline_variables():
    result: str = GherkinParser([f"Given a <state> is set"]).to_markdown()
    assert result == f"_Given_ a **state** is set\n\n"


def test_given_step():
    given = "a state is set"
    result: str = GherkinParser([f"Given {given}"]).to_markdown()
    assert result == f"_Given_ {given}\n\n"


def test_when_step():
    when = "an action is taken"
    result: str = GherkinParser([f"When {when}"]).to_markdown()
    assert result == f"_When_ {when}\n\n"


def test_then_step():
    then = "a result is expected"
    result: str = GherkinParser([f"Then {then}"]).to_markdown()
    assert result == f"_Then_ {then}\n\n"


def test_and_step():
    and_step = "a state is set"
    result: str = GherkinParser([f"And {and_step}"]).to_markdown()
    assert result == f"_And_ {and_step}\n\n"


def test_but_step():
    but_step = "a state is set"
    result: str = GherkinParser([f"But {but_step}"]).to_markdown()
    assert result == f"_But_ {but_step}\n\n"


def test_asterisk_step():
    asterisk_step = "a state is set"
    result: str = GherkinParser([f"* {asterisk_step}"]).to_markdown()
    assert result == f"_*_ {asterisk_step}\n\n"


def test_background():
    result: str = GherkinParser([f"Background:"]).to_markdown()
    assert result == "## Background\n\n"


def test_doc_string_double_quotes():
    doc_string = '''
"""
First line of the docstring!
    Line with 4 spaces indent!
            Line with 8 spaces indent!
"""'''
    lines = doc_string.splitlines()
    result: str = GherkinParser(lines).to_markdown()
    assert result == f"```\n{lines[2]}{lines[3]}{lines[4]}```\n"


def test_doc_string_backticks():
    doc_string = '''
    ```
    First line of the docstring!
        Line with 4 spaces indent!
                Line with 8 spaces indent!
    ```'''
    lines = doc_string.splitlines()
    result: str = GherkinParser(lines).to_markdown()
    assert result == f"```\n{lines[2][4:]}{lines[3][4:]}{lines[4][4:]}```\n"


def test_doc_string_with_language_name():
    doc_string = '''
    ```python
      if value is not None:
          value.make_action()
      else:
          value.dont_make_action()
    ```'''
    lines = doc_string.splitlines()
    result: str = GherkinParser(lines).to_markdown()
    assert result == f"{lines[1][4:]}\n{lines[2][4:]}{lines[3][4:]}{lines[4][4:]}{lines[5][4:]}```\n"


def test_data_table():
    data_table = """
Examples:
| state   | action   | result   |
| state 1 | action 1 | result 1 |
| state 2 | action 2 | result 2 |

"""
    lines = data_table.splitlines()
    result: str = GherkinParser(lines).to_markdown()
    assert result == f"### Examples\n\n{lines[2].strip()}\n|---------|----------|----------|\n" \
                     f"{lines[3].strip()}\n{lines[4].strip()}\n\n"
