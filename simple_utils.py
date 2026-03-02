# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Return the input string with its characters reversed.
    
    Returns:
        reversed_text (str): The input string with character order reversed.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the words in a sentence separated by whitespace.
    
    Parameters:
        sentence (str): Input string whose words are separated by whitespace.
    
    Returns:
        int: Number of whitespace-separated words in `sentence`.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from degrees Celsius to degrees Fahrenheit.
    
    Parameters:
        celsius (float): Temperature in degrees Celsius.
    
    Returns:
        float: Temperature converted to degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32
