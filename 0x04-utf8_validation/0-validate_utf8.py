#!/usr/bin/python3
"""
Validate UTF_8 encoding module
"""


def validUTF8(data):
    """Check if the given data is valid UTF-8 encoding.

    Args:
        data (list of int): List of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        # Get the 8 least significant bits
        byte &= 0xFF

        # Determine the number of bytes in the UTF-8 character
        if num_bytes == 0:
            if (byte >> 7) == 0b0:
                continue  # 1-byte character (0xxxxxxx)
            elif (byte >> 5) == 0b110:
                num_bytes = 1  # 2-byte character (110xxxxx)
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # 3-byte character (1110xxxx)
            elif (byte >> 3) == 0b11110:
                num_bytes = 3  # 4-byte character (11110xxx)
            else:
                return False  # Invalid starting byte
        else:
            # Check continuation bytes
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0  # Ensure all bytes were accounted for
