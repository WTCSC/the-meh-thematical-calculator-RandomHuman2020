import pytest
import calc_functs

def test_adding_positive():
    assert calc_functs.add("1337", "3005") == 4342
def test_adding_negative():
    assert calc_functs.add("-5", "-112") == -117
def test_adding_invalid():
    assert calc_functs.add("fish", "fish") == "fail_invalid"
    assert calc_functs.add("133.7", "300.5") == "fail_invalid"
def test_subtracting_positive():
    assert calc_functs.subtract("3005", "1337") == 1668
def test_subtracting_negative():
    assert calc_functs.subtract("-3005", "-1337") == -1668
def test_subtracting_big_from_small():
    assert calc_functs.subtract("1337", "3005") == -1668
def test_subtracting_invalid():
    assert calc_functs.subtract("H", "fish") == "fail_invalid"
    assert calc_functs.subtract("300.5", "133.7") == "fail_invalid"
def test_multiplying_positive():
    assert calc_functs.multiply("3005", "1337") == 4017685
def test_multiplying_negative():
    assert calc_functs.multiply("-3005", "-1337") == 4017685
def test_multiplying_one():
    assert calc_functs.multiply("3005", "1") == 3005
def test_multiplying_invalid():
    assert calc_functs.multiply("H", "fish") == "fail_invalid"
    assert calc_functs.multiply("300.5", "133.7") == "fail_invalid"
def test_dividing_positive():
    assert calc_functs.divide("3005", "1337") == 2.24757
def test_dividing_one():
    assert calc_functs.divide("3005", "1") == 3005
def test_dividing_zero():
    assert calc_functs.divide("3005", "0") == "fail_dividebyzero"
def test_dividing_invalid():
    assert calc_functs.divide("H", "fish") == "fail_invalid"
    assert calc_functs.divide("300.5", "133.7") == "fail_invalid"