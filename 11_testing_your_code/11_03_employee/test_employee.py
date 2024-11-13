from employee import Employee
import pytest

@pytest.fixture
def beta_employee():
    """Test employee to be used for testing"""
    beta_employee = Employee('John', 'Appleseed', 60000)
    return beta_employee

def test_give_default_raise(beta_employee):
    """Will it work with default raise"""
    beta_employee.give_raise()
    assert beta_employee.salary == 65000

def test_give_custom_raise(beta_employee):
    """Will it work with custom raise"""
    beta_employee.give_raise(10000)
    assert beta_employee.salary == 70000
