"""
Some sugar functions
"""
logic_div = lambda n, d: d and n / d or 0
logic_mult = lambda a, b: a * b if a and b else 0


def from_none_dict(_d: dict) -> dict:
    return {x: y if y else 0 for (x, y) in _d.items()}


def from_none_list(_l: list) -> list:
    return [x if x else 0 for x in _l]
