price = float(input("Price: "))
discount = float(input("Discount: "))
vat = float(input("VAT: "))
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(
    f"База после скидки: {base:.2f} ₽\n"
    f"НДС: {vat_amount:.2f} ₽\n"
    f"Итого к оплате: {total:.2f} ₽\n"
)
