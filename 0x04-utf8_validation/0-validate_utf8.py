#!/usr/bin/python3
"""
Defines a UTF-8 Validation function
"""


def validUTF8(data):
    """
    UTF-8 Validation
    Args:
        data (list[int]): an array of characters represented as 1byte int
    Returns:
        (True): if all characters in data are valid UTF-8 code point
        (False): if one or more characters in data are invalid code point
    """
    msb_mask = 1 << 7
    second_msb_mask = 1 << 6
    byte_count = 0
    for code_point in data:
        leading_bit_mask = 1 << 7
        if byte_count == 0:
            while leading_bit_mask & code_point:
                byte_count += 1
                leading_bit_mask = leading_bit_mask >> 1
            if byte_count == 0:
                continue
            if byte_count == 1 or byte_count > 4:
                return False
        else:
            if not (code_point & msb_mask and not (
                    code_point & second_msb_mask)):
                return False
        byte_count -= 1
    return byte_count == 0
