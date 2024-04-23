def estimate_reading_time(text):
    if type(text) is not str: raise TypeError("Argument must be a string")
    return len(text.split()) / 200