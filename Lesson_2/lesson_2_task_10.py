def bank(X, Y):
     rate = 0.1
     for _ in range(Y):
      X += X * rate 
      return X
X = 1000
Y = 10
final_amount = bank(X, Y)
print(f"Через {Y} лет на счету будет {final_amount:.2f} рублей.")