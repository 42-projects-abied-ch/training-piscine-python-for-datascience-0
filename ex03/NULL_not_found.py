import math

def NULL_not_found(object: any) -> int:
    object_type = type(object)
    type_strings = {
        float: f"Cheese: {object} {object_type}",
        int: f"Zero: {object} {object_type}",
        str: f"Empty: {object}{object_type}",
        bool: f"Fake: {object} {object_type}",
    }
    if (ret := 0 if object in [None, 0, ""] or (object_type not in [None, str] and math.isnan(object)) else 1) == 0:
        print(type_strings[object_type] if object is not None else f"Nothing: {object} {object_type}")
    else:
        print("Type not found")
    return ret