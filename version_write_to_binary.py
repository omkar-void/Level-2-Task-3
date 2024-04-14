def append_integer_to_bin(filename, value):
    try:
        # Open the binary file in append mode
        with open(filename, 'ab') as file:
            # Convert the integer to bytes and write it to the file
            file.write(value.to_bytes(4, byteorder='little', signed=True))  # Changed to little-endian
        print(f"Integer value {value} successfully appended to {filename}")
    except Exception as e:
        print(f"Error appending integer value to {filename}: {e}")

def extract_last_integer_from_bin(filename):
    try:
        # Open the binary file in read mode
        with open(filename, 'rb') as file:
            # Seek to the start of the last integer value
            file.seek(-4, 2)  # Seek 4 bytes before the end of the file
            # Read the last 4 bytes as the integer value
            value_bytes = file.read(4)
            # Convert bytes to integer
            value = int.from_bytes(value_bytes, byteorder='little', signed=True)  # Changed to little-endian
            return value
    except Exception as e:
        print(f"Error extracting last integer value from {filename}: {e}")
        return None

# Example usage:
filename = "incorrect_version.bin"  # add your file name here
append_integer_to_bin(filename, 1289)
value = extract_last_integer_from_bin(filename)
if value is not None:
    print(f"The last integer value extracted from {filename} is: {value}")
