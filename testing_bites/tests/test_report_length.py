from lib.report_length import *

def test_report_length_when_string_length_17():
    assert report_length("aaaaaaaaaaaaaaaaa") == "This string was 17 characters long."

def test_report_length_when_string_length_0():
    assert report_length("") == "This string was 0 characters long."
