import numpy as np

def format_numpy_array(arr, length=15, padding='_', alignment='center'):
    str_arr = np.char.mod('%s', arr)
    
    if alignment == 'center':
        formatted = np.char.center(str_arr, length, fillchar=padding)
    elif alignment == 'left':
        formatted = np.char.ljust(str_arr, length, fillchar=padding)
    elif alignment == 'right':
        formatted = np.char.rjust(str_arr, length, fillchar=padding)
    else:
        raise ValueError("Alignment must be 'center', 'left', or 'right'.")
    
    return formatted

if __name__ == "__main__":
    arr = np.array(['apple', 'banana', 123, 45.67, 'cherry'])
    
    centered = format_numpy_array(arr, length=15, padding='_', alignment='center')
    left_justified = format_numpy_array(arr, length=15, padding='_', alignment='left')
    right_justified = format_numpy_array(arr, length=15, padding='_', alignment='right')
    
    print("Original Array:")
    print(arr)
    print("\nCentered:")
    print(centered)
    print("\nLeft-Justified:")
    print(left_justified)
    print("\nRight-Justified:")
    print(right_justified)