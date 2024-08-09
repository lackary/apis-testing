

def dict_to_dataclass(data_class, data_dict):
    """Converts a dictionary to a dataclass instance, ignoring extra keys.

    Args:
        data_class: The dataclass type to create.
        data_dict: The dictionary to convert.

    Returns:
        An instance of the specified dataclass.
    """

    dataclass_fields = set(data_class.__annotations__.keys())
    filtered_data = {k: v for k, v in data_dict.items() if k in dataclass_fields}
    return data_class(**filtered_data)

def dict_array_to_dataclass_list(data_class, dict_array):
    """Converts a dictionary array to a list of dataclass instances, ignoring extra keys.

    Args:
        data_class: The dataclass type to create.
        json_array: The JSON array of objects.

    Returns:
        A list of dataclass instances.
    """

    dataclass_fields = set(data_class.__annotations__.keys())
    return [
        data_class(**{k: v for k, v in item.items() if k in dataclass_fields})
        for item in dict_array
    ]