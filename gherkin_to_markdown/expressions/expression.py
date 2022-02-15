from abc import ABC, abstractmethod


class Expression(ABC):
    def __init__(self, keyword: str):
        self.keyword = keyword

    @abstractmethod
    def to_markdown(self, statement: str):
        pass
