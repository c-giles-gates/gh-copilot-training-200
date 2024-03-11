def calculate_amortization(principal, annual_interest_rate, years):
    """
    Calculates the monthly amortization for a loan based on the principal amount, annual interest rate, and number of years.

    Parameters:
    principal (float): The principal amount of the loan.
    annual_interest_rate (float): The annual interest rate for the loan.
    years (int): The number of years for the loan.

    Returns:
    float: The monthly amortization amount.

    """
    # Convert annual interest rate from percentage to decimal, and then to monthly
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Calculate total number of payments
    number_of_payments = years * 12

    # Calculate amortization
    amortization = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**number_of_payments) / ((1 + monthly_interest_rate)**number_of_payments - 1)

    return amortization