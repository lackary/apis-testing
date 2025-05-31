from typing import Union, Dict, Any, get_type_hints, get_args, TypeVar

T = TypeVar('T')  # 定義一個類型變數 T

def handle_dataclass(data: Dict[str, Any], dataclass_type: type) -> T:
    """Recursively creates dataclass instances from nested JSON."""

    type_hints = get_type_hints(dataclass_type)
    fields = {}

    for field_name, field_type in type_hints.items():
        if field_name not in data:
            if type(None) in get_args(field_type):  # Optional field
                fields[field_name] = None
                continue
            else:
                raise ValueError(f"Missing required field '{field_name}' in JSON.")

        field_value = data[field_name]

        if field_value is None and type(None) in get_args(field_type):  # Explicitly handle None for Optional
            fields[field_name] = None
            continue

        if hasattr(field_type, '__origin__') and field_type.__origin__ is list:  # Handle lists
            inner_type = get_args(field_type)[0]
            if isinstance(field_value, list):
                # If inner_type is Union, recursively handle each item with Union logic
                if hasattr(inner_type, '__origin__') and inner_type.__origin__ is Union:
                    fields[field_name] = [
                        handle_union(item, get_args(inner_type)) for item in field_value
                    ]
                else:
                    fields[field_name] = [
                        handle_dataclass(item, inner_type) if hasattr(inner_type, '__dataclass_fields__') and isinstance(item, dict) else item
                        for item in field_value
                    ]
            elif field_value is None:
                fields[field_name] = []  # Handle missing list as empty list
            else:
                raise TypeError(f"Expected a list for field '{field_name}', got {type(field_value)}")

        elif hasattr(field_type, '__origin__') and field_type.__origin__ is Union:  # Handle Unions
            inner_types = get_args(field_type)
            for inner_type in inner_types:
                if inner_type is type(None) and field_value is None:
                    fields[field_name] = None
                    break
                elif hasattr(inner_type, '__dataclass_fields__') and isinstance(field_value, dict):
                    try:
                        fields[field_name] = handle_dataclass(field_value, inner_type)
                        break  # Successfully converted
                    except (TypeError, ValueError):
                        pass  # Try the next type
                elif isinstance(field_value, inner_type.__origin__ if hasattr(inner_type, '__origin__') else inner_type):
                    fields[field_name] = field_value
                    break
            else:
                raise TypeError(f"No matching type found for Union field '{field_name}'")

        elif hasattr(field_type, '__dataclass_fields__') and isinstance(field_value, dict):  # Nested dataclasses
            fields[field_name] = handle_dataclass(field_value, field_type)
        else:
            fields[field_name] = field_value

    try:
        return dataclass_type(**fields)
    except TypeError as e:
        raise TypeError(f"Error creating {dataclass_type.__name__}: {e}. Check JSON and dataclass definitions.")

def handle_union(field_value, inner_types):
    for inner_type in inner_types:
        if inner_type is type(None) and field_value is None:
            return None
        elif hasattr(inner_type, '__dataclass_fields__') and isinstance(field_value, dict):
            try:
                return handle_dataclass(field_value, inner_type)
            except (TypeError, ValueError):
                pass
        elif isinstance(field_value, inner_type.__origin__ if hasattr(inner_type, '__origin__') else inner_type):
            return field_value
    raise TypeError(f"No matching type found for Union item: {field_value}")

def parse_json(json_data: Dict[str, Any], dataclass_type: type):
    """parse json data to dataclass"""
    if type(json_data) is list:
        return [handle_dataclass(item, dataclass_type) for item in json_data]
    else:
        return handle_dataclass(json_data, dataclass_type)