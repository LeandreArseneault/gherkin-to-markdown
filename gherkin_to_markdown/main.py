import os.path
import sys

from gherkin_parser import GherkinParser


def convert_file(source: str, destination: str):
    with open(source, "r") as feature_file:
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        with open(destination, "w") as output_file:
            markdown_result = GherkinParser(feature_file.readlines()).to_markdown()
            output_file.write(markdown_result)


if __name__ == '__main__':
    args = sys.argv
    source = args[1]
    destination = args[2]

    if os.path.isdir(source):
        for file in os.listdir(source):
            if file.endswith(".feature"):
                convert_file(os.path.join(source, file), os.path.join(destination, file.replace(".feature", ".md")))
    else:
        if os.path.isdir(destination):
            convert_file(source, os.path.join(destination, os.path.basename(source).replace(".feature", ".md")))
        else:
            convert_file(source, destination)
