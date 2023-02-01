plus = int(input("Vvedite vyruchku firmy => "))
minus = int(input("Vvedite izderjki firmy => "))
result = plus - minus
print("pribyl ", result)
rentabelnost = result / 1000
sotrudniki = int(input("Vvedite chislennost sotrudnikov => "))
result2 = rentabelnost * sotrudniki * 10
print("pribyl firmy na odnogo sotrudnika ", result2)