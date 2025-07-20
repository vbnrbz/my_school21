from typing import List, Dict, Union, Optional, Callable


class DataProcessor:
    """Class for working with data"""

    @staticmethod
    def process_data(int_value: int, str_value: str) -> str:
        """Method that takes an int and a str and returns their merger."""
        return f"Integer: {int_value}, String: {str_value}"

    @staticmethod
    def combine_lists(list1: List[int], list2: List[int]) -> List[int]:
        """A method that takes two lists of integers and returns their merger."""
        return list1 + list2

    @staticmethod
    def create_mapping(keys: List[str], values: List[Union[int, str]]) -> Dict[str, Union[int, str]]:
        """Method that creates a dictionary from two lists of strings."""
        return dict(zip(keys, values))

    @staticmethod
    def calculate(a: Union[int, float], b: Union[int, float]) -> int:
        """A method that takes an int or float in each of the arguments and returns their sum."""
        return round(a + b)


class OptionalHandler:
    """Optional function"""

    @staticmethod
    def handle_optional(value: Optional[int] = None) -> str:
        """A method that takes an optional integer and returns a string."""
        if value is None:
            return "Value not passed"
        return f"Value - {value}"

    @staticmethod
    def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
        """A method that takes a function and two integers and applies the function to them."""
        return func(a, b)


def func_sum(a: int, b: int) -> int:
    return a + b


def func_dot(a: int, b: int) -> int:
    return a * b


def main() -> None:
    """Main method, entry point"""
    processor = DataProcessor()
    print(processor.process_data(15, 'world'))
    print(processor.combine_lists([1, 2, 3], [4, 5, 6]))
    print(processor.create_mapping(['a', 'b'], [1, 'not_an_int']))
    print(processor.calculate(10, 20))
    print(processor.calculate(10.5, 20.5))

    handler = OptionalHandler()
    print(handler.handle_optional(10))
    print(handler.apply_function(func_sum, 10, 20))
    print(handler.apply_function(func_dot, 10, 20))


if __name__ == "__main__":
    main()
