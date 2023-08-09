from AoC2015Day1 import check_has_five_zeros, concatenate_input_and_number, generate_md5_hash


def test_check_has_five_works():
    assert check_has_five_zeros("00000123") == True


def test_check_has_five_fails():
    assert check_has_five_zeros("000123") == False


def test_check_has_five_empty():
    assert check_has_five_zeros("") == False


def test_check_has_five_random():
    assert check_has_five_zeros("982hnhsd18hono82uw") == False


def test_concatenate():
    assert concatenate_input_and_number("abc", 123) == "abc123"


def test_generate_md5_hash():
    assert generate_md5_hash("yzbqklnj") == "dd9391a66659d33f01cc20141ce540b8"
