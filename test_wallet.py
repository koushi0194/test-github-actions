"""
Pytest for wallet app
"""
import pytest
from wallet import Wallet


def test_default_initial_amount():
    """
    Default initial Amount
    """
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    """
    Setting initial amount
    """
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    """
    Add cash to wallet
    """
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    """
    Spend cash from wallet
    """
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    """
    Insufficient amount error
    """
    wallet = Wallet()
    with pytest.raises(Exception):
        wallet.spend_cash(100)
