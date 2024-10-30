#!/usr/bin/python3
"""
    This method determines if a given data set
    represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
        Return: True if data is a valid UTF-8 encoding,
        else return False
        A character in UTF-8 can be 1 to 4 bytes long
        The data set can contain multiple characters
        The data will be represented by a list of integers
        Each integer represents 1 byte of data,
        therefore you only need to handle the
        8 least significant bits of each integer
    """
    # Number of bytes remaining in the current UTF-8 character
    remaining_bytes = 0

    for byte in data:
        # Extract the 8 least significant bits (ensure it is a byte)
        byte = byte & 0xFF

        if remaining_bytes == 0:
            # Determine how many bytes the current UTF-8 character should have
            if (byte >> 7) == 0:  # 1-byte character (0xxxxxxx)
                continue  # Valid single byte, move to the next one
            elif (byte >> 5) == 0b110:  # 2-byte character (110xxxxx)
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
                remaining_bytes = 3
            else:
                return False  # Invalid leading byte
        else:
            # Check if the byte is a valid continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    # If there are remaining bytes expected, it's an incomplete character
    return remaining_bytes == 0
