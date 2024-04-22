def make_snippet(string):
    words = string.split(" ")
    if len(words) > 5:
        return " ".join(words[:5]) + "..."
    else:
        return string
