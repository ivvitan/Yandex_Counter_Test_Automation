from sender_stand_request import *
from data import *
auth_token = get_new_user_token()


def get_kit_body(name):
    return {"name": name}


def positive_assert(kit_body):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400


def test_valid_name_1_char():
    positive_assert(kit_name_data_1_char)


def test_valid_name_511_chars():
    positive_assert(kit_name_data_511_chars)


def test_invalid_name_0_chars():
    negative_assert_code_400(kit_name_data_0_chars)


def test_invalid_name_512_chars():
    negative_assert_code_400(kit_name_data_512_chars)


def test_valid_name_english_letters():
    positive_assert(kit_name_data_english_letters)


def test_valid_name_russian_letters():
    positive_assert(kit_name_data_russian_letters)


def test_valid_name_special_chars():
    positive_assert(kit_name_data_special_chars)


def test_valid_name_spaces():
    positive_assert(kit_name_data_spaces)


def test_valid_name_numbers():
    positive_assert(kit_name_data_numbers)


def test_invalid_name_not_provided():
    negative_assert_code_400(kit_name_data_not_provided)


def test_invalid_name_wrong_type():
    negative_assert_code_400(kit_name_data_wrong_type)
