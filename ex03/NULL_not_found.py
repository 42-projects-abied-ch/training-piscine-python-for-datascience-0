def NULL_not_found(object: any) -> int:
    object_type = type(object)
    type_strings = {
    None: f"Nothing: {object} {object_type}",
    float: f"Cheese: {object} {object_type}",
    int: f"Zero: {object} {object_type}",
    str: f"Empty: {object}{object_type}",

    bool: "Type not found"
    }