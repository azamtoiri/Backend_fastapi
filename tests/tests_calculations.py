import pytest

from app.calculations import add, subtract, multiply, divide, BankAccount


@pytest.fixture()
def zero_bank_account():
    print("Creating Empty BankAccount")
    return BankAccount(0)


@pytest.fixture()
def bank_account():
    print("Creating BankAccount with 50")
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (4, 5, 9),
    (122, 122, 244),
    (2342342, 235435345, 237777687)
])
def test_add(num1, num2, expected):
    print("Testing add function")
    assert add(num1, num2) == expected


def test_subtract():
    print("Testing subtract function")
    assert subtract(9, 4) == 5


def test_multiply():
    print("Testing multiply function")
    assert multiply(4, 5) == 20


def test_divide():
    print("Testing divide function")
    assert divide(20, 2) == 10


def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50


def test_bank_default_amount(zero_bank_account):
    print("testing my bank account")
    assert zero_bank_account.balance == 0


def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30


def test_deposit(bank_account):
    bank_account.deposit(30)
    assert bank_account.balance == 80


def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55
