def bank(X, Y):
    total = X
    for year in range(1, Y+1):
          interest = total * 0.1
          total += interest
          total *= 1.1
    return total
initial_deposit = 1000.0 
term = 5  
final_amount = bank(initial_deposit, term)
print(f"Сумма на счету пользователя спустя {term} лет: {final_amount:.2f} рублей")