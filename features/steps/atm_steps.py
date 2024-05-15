from behave import given, when, then
from atm import ATM

@given('I have ${amount:d} in my account')
def step_given_i_have_amount_in_my_account(context, amount):
    context.atm = ATM(balance=amount)

@when('I withdraw ${amount:d}')
def step_when_i_withdraw_amount(context, amount):
    context.atm.withdraw(amount)

@when('I deposit ${amount:d}')
def step_when_i_deposit_amount(context, amount):
    context.atm.deposit(amount)

@when('I check my balance')
def step_when_i_check_my_balance(context):
    context.balance = context.atm.get_balance()

@then('I should have ${expected_balance:d} left in my account')
def step_then_i_should_have_expected_balance_left_in_my_account(context, expected_balance):
    assert context.atm.get_balance() == expected_balance, f"Expected {expected_balance}, but got {context.atm.get_balance()}"

@then('I should see that my balance is ${expected_balance:d}')
def step_then_i_should_see_that_my_balance_is_expected_balance(context, expected_balance):
    assert context.balance == expected_balance, f"Expected {expected_balance}, but got {context.balance}"

@then('I should have ${expected_balance:d} in my account')
def step_impl(context, expected_balance):
    assert context.atm.get_balance() == expected_balance, f"Expected {expected_balance}, but got {context.atm.get_balance()}"