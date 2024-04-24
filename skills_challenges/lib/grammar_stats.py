class GrammarStats:
    def __init__(self):
        self._checks_undertaken = 0
        self._checks_passed = 0

    def check(self, text):
        if type(text) != str: raise TypeError("Argument must be a string")
        if not text: raise ValueError("String may not be empty")

        check_result = text[0].isupper() and text[-1] in [".", "!", "?"]
        self._checks_undertaken += 1
        if check_result: self._checks_passed += 1
        return check_result

    def percentage_good(self):
        if self._checks_undertaken == 0: return 0
        return round(100 * (self._checks_passed / self._checks_undertaken))
