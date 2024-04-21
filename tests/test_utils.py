import pytest

from src.utils import get_mask_number, get_filtered_list, get_sorted_list, print_from_dict


def test_get_mask_number():
    assert get_mask_number("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert get_mask_number("Счет 64686473678894779589") == "Счёт **9589"



def test_get_filtered_list(filtred):
    assert get_filtered_list(filtred)[0] == {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

def test_get_sorted_list(filtred):
    assert get_sorted_list(filtred)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_print_from_dict(filtred):
    assert print_from_dict(filtred[0]) is None


