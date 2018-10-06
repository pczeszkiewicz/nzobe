NONE_VALUES = (None, '\\N', '')


def obj_or_none(value):
    if value in NONE_VALUES:
        return None
    if isinstance(value, float) and value != value:
        # it is float('nan')
        return None
    return value
