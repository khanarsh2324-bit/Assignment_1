principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in %): "))
time = float(input("Enter time (in years): "))
n = int(input("Enter number of times interest compounds per year: "))

amount = principal * (1 + (rate / 100) / n) ** (n * time)
compound_interest = amount - principal

print("Compound Interest =", round(compound_interest, 2))
print("Total Amount =", round(amount, 2))
