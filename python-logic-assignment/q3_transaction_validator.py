balance = input("Enter account balance: ")
balance = int(balance)

withdrawal = input("Enter withdrawal amount: ")
withdrawal = int(withdrawal)

verified = input("Are you verified (True/False): ")
verified = verified == "True"

if verified and withdrawal <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")
