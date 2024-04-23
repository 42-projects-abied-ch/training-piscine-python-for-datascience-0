def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    type_strings = {
        list: f"List : {object_type}",
        tuple: f"Tuple : {object_type}",
        set: f"Set : {object_type}",
        dict: f"Dict : {object_type}",
        str: f"{object} is in the kitchen : {object_type}",
        int: "Type not found",
    }
    print(type_strings[object_type])
    return 42
