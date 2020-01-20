#!/usr/bin/python3


def add_attribute(obj, name, value):
    try:
        setattr(obj, name, value)
    except Exception:
        raise TypeError("can't add new attribute")
