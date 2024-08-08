import pytest
from string_utils import StringUtils
utils = StringUtils()

def test_capitalize_positive():
    assert utils.capitilize("pytest") == "Pytest" 
    assert utils.capitilize("пятая нога") == "Пятая нога" 
   # assert utils.capitilize("трасса e95") == "Трасса e95" 

def test_capitalize_negative():
   # assert utils.capitilize("PYTHON") == "PYTHON" 
    assert utils.capitilize("999") == "999" 
    assert utils.capitilize(" ") == " " 

def test_trim_positive():
    assert utils.trim(" pytest") == "pytest" 
    assert utils.trim(" пятая нога") == "пятая нога" 
    assert utils.trim(" 999") == "999" 
    assert utils.trim(" ") == "" 

def test_trim_negative():
    assert utils.trim("") == "" 
    assert utils.trim("пятая нога") == "пятая нога" 
    assert utils.trim("999") == "999" 

@pytest.mark.parametrize('string, delimeter, result', [
       # positive
   ("вчера, сегодня, завтра", ",", ["вчера", "сегодня", "завтра"]),
   ("yesterday, today, tomorrow", ",", ["yesterday", "today", "tomorrow"]),
   ("5, $, 18, %", ",", ["5", "$", "18", "%"]),
      # negative
   ("", None, [""]),
   ("9 9 9", None, ["9 9 9"])
])
def test_to_list (string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result

@pytest.mark.parametrize("string, symbol, result", [
    ("маляр", "я", True),
    ("E95", "9", True),
    (" ", " ", True),
    ("E95", "e", False),
    ("E95", "Е", False), # в первом случае Е в английской раскладке, во втором в русской
    ("заяц", "18", False),
    ("True", None, False)
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result
  
@pytest.mark.parametrize("string, symbol, result", [
    ("маляр", "я", "маяр"),
    ("E95", "9", "E5"),
    (" ", " ", " "),
    ("yesterday", "z", "yesterday"),
    ("вчервшний день", " ", "вчерашнийдень"),
    ("заяц", None, "заяц")
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize("string, symbol, result", [
    ("маляр", "м", True),
    ("E95", "E", True),
    (" ", " ", True),
    ("E95", "e", False),
    ("E95", "Е", False), # в первом случае Е в английской раскладке, во втором в русской
    ("заяц", "у", False),
    ("True", " ", False)
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize("string, symbol, result", [
    ("маляр", "р", True),
    ("E95", "5", True),
    (" ", " ", True),
    ("E95", "e", False),
    ("E95", " ", False), 
    ("заяц", "у", False),
    ("True", "E ", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize("string, result", [
    (" ", True),
    ("   ", True),
    (" ", True),
    ("E95", False),
    ("120 тыс. лет назад", False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

@pytest.mark.parametrize("lst, joiner, result", [
    (["a", "b", "c"], ";", "a;b;c"),
    (["5 2 6 9 4"], "-", "5-2-6-9-4"),
    ([" "], ".", " "),
    ([" "], None, " ")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
       res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result

