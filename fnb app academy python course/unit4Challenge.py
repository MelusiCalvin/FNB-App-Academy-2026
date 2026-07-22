BALANCE = 500
output = 0
withdrawal_amount = float(input("How much do you want to withdraw: "))
if withdrawal_amount <= BALANCE:
    output = BALANCE - withdrawal_amount
    print("Withdrawal successful! Remaining balance: R", output)
elif withdrawal_amount <= 0:
    print("Invalid amount")
else:
    print("Declined. Insufficient funds")