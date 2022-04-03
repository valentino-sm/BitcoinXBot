"""
Some sugar functions
"""


def from_none_dict(_d: dict) -> dict:
    return {x: y if y else 0 for (x, y) in _d.items()}


def from_none_list(_l: list) -> list:
    return [x if x else 0 for x in _l]
