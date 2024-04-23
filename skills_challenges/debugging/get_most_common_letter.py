def get_most_common_letter(text):
    counter = {}
    for char in text:
        # Fixed: exclude all non-alphanumeric characters (since space is not a desired answer)
        # To include punctuation as valid 'letters', instead use `not char.isspace()`
        if char.isalpha(): 
            counter[char] = counter.get(char, 0) + 1

    print(f"Counter dict is {counter}")
    print(f"the sorting lambda looks at, for example, the first value of the first element: {list(counter.items())[1][1]}")
    # Fixed: letter was assigned from 1) the smallest not largest and 2) from the key, not the value``
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]

    print(f"This is the result of the sort: {sorted(counter.items(), key=lambda item: item[1])}")
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
