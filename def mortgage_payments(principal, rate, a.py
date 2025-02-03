def mortgage_payments(principal, rate, amortization):
    """
    Calculate various mortgage payment frequencies.
    
    Parameters:
        principal (float): The mortgage principal.
        rate (float): The quoted annual interest rate (in percent).
        amortization (int): The amortization period in years.
    
    Returns:
        tuple: A tuple of six values representing the payments for:
               (monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly, rapid weekly)
    """
    # Convert quoted rate (percent) to a decimal.
    r = rate / 100.0

    # Monthly payments (12 payments per year)
    n_monthly = amortization * 12
    monthly_rate = (1 + r/2) ** (2/12) - 1
    monthly = principal * (monthly_rate * (1 + monthly_rate) ** n_monthly) / ((1 + monthly_rate) ** n_monthly - 1)

    # Semi-monthly payments (24 payments per year)
    n_semi = amortization * 24
    semi_rate = (1 + r/2) ** (2/24) - 1
    semi_monthly = principal * (semi_rate * (1 + semi_rate) ** n_semi) / ((1 + semi_rate) ** n_semi - 1)

    # Bi-weekly payments (26 payments per year)
    n_bi = amortization * 26
    bi_rate = (1 + r/2) ** (2/26) - 1
    bi_weekly = principal * (bi_rate * (1 + bi_rate) ** n_bi) / ((1 + bi_rate) ** n_bi - 1)

    # Weekly payments (52 payments per year)
    n_week = amortization * 52
    week_rate = (1 + r/2) ** (2/52) - 1
    weekly = principal * (week_rate * (1 + week_rate) ** n_week) / ((1 + week_rate) ** n_week - 1)

    # Rapid payments are based on the monthly payment.
    rapid_bi_weekly = monthly / 2
    rapid_weekly = monthly / 4

    return (monthly, semi_monthly, bi_weekly, weekly, rapid_bi_weekly, rapid_weekly)


def main():
    # Prompt the user for input values.
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the quoted interest rate (percent): "))
    amortization = int(input("Enter the amortization period (years): "))

    # Get the various payments.
    payments = mortgage_payments(principal, rate, amortization)

    # Format and display the results rounded to the nearest penny.
    print(f"Monthly Payment: ${payments[0]:.2f}")
    print(f"Semi-monthly Payment: ${payments[1]:.2f}")
    print(f"Bi-weekly Payment: ${payments[2]:.2f}")
    print(f"Weekly Payment: ${payments[3]:.2f}")
    print(f"Rapid Bi-weekly Payment: ${payments[4]:.2f}")
    print(f"Rapid Weekly Payment: ${payments[5]:.2f}")


if __name__ == "__main__":
    main()