class CreditCard:
  """A consumer credit card."""
  
  def __init__(self, customer, bank, acnt, limit):
    """Create a new credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    """
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = 0

  def get_customer(self):
    """Return name of the customer."""
    return self._customer
    
  def get_bank(self):
    """Return the bank's name."""
    return self._bank

  def get_account(self):
    """Return the card identifying number (typically stored as a string)."""
    return self._account

  def get_limit(self):
    """Return current credit limit."""
    return self._limit

  def get_balance(self):
    """Return current balance."""
    return self._balance
  
  def _set_balance(self, new_balance):
    """Set current balance."""
    self._balance = new_balance

  def _delta_balance(self, delta):
    """
    Change current balance by given amount.
    Positive delta increases balance (debt of customer to bank).
    """
    self._balance += delta

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed; False if charge was denied.
    """
    if price + self._balance > self._limit:  # if charge would exceed limit,
      return False                           # cannot accept charge
    else:
      self._balance += price
      return True

  def make_payment(self, amount):
    """Process customer payment that reduces balance."""
    self._balance -= amount


class PredatoryCreditCard(CreditCard):
  """An extension to CreditCard that compounds interest and fees."""
  
  def __init__(self, customer, bank, acnt, limit, apr):
    """Create a new predatory credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
    """
    super().__init__(customer, bank, acnt, limit)  # call super constructor
    self._apr = apr
    self._monthly_charge_count = 0
    self._paid_in_current_month = 0

  @property
  def minimum_payment(self):
    return self.get_balance() * 0.1

  def make_payment(self, amount):
    super().make_payment(amount)
    self._paid_in_current_month += amount

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed.
    Return False and assess $5 fee if charge is denied.
    """
    self._monthly_charge_count += 1
    if self._monthly_charge_count > 10:
      price += 1
    success = super().charge(price)          # call inherited method
    if not success:
      self._delta_balance(5)                # assess penalty
    return success                           # caller expects return value

  def process_month(self):
    """Assess monthly interest on outstanding balance."""
    self._monthly_charge_count = 0
    if self._paid_in_current_month < self.minimum_payment:
      self._delta_balance(5)
    if self.get_balance() > 0:
      # if positive balance, convert APR to monthly multiplicative factor
      monthly_factor = pow(1 + self._apr, 1/12)
      self._set_balance(self.get_balance() * monthly_factor)


if __name__ == "__main__":
    my_card = PredatoryCreditCard("Christian Kruf", "Airbank", "5391 0365 9567 5309", 1000, 0.2)
    for _ in range(12):
      my_card.charge(10)
    # surcharge applied to 11th and 12th transaction
    assert my_card.get_balance() == 122
    # surcharge applied for failed transaction
    my_card.charge(1_000_000)
    assert my_card.get_balance() == 127
    # minimum payment fee charged, interest charged
    my_card.process_month()
    assert my_card.get_balance() == 132 * pow(1 + 0.2, 1/12)
    print(f"balance is {my_card.get_balance()}")
    my_card.make_payment(130)
    my_card.process_month()
    print(my_card.get_balance())