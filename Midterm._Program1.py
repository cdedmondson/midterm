def checkingAccount(customer_name, base_fee, deposit):
    total_service_fee = 0.0

    # No deposit exists
    if not deposit:
        return print(customer_name + ',', '$' + base_fee, "base fee" + ',', "no check deposit")

    total_deposits = sum(deposit)  # Get total number of deposits

    if total_deposits > 50:
        total_deposits = total_deposits - 50
        total_service_fee += (total_deposits * 0.05)
        total_deposits = 50

    if total_deposits > 20 and total_deposits <= 50:
        total_deposits = total_deposits - 20
        total_service_fee += (total_deposits * 0.07)
        total_deposits = 20

    if total_deposits <= 20:
        total_service_fee += (total_deposits * 0.10)

    total_service_fee += int(base_fee)

    deposit = str(deposit)
    string2 = str(total_service_fee)

    return print(customer_name + ',', '$' + base_fee, "base fee" + ',', "check deposits", deposit + ',',
                 'total charges = ' + string2)


# Test input 1
print("Test#1")
customer_1 = "Jack"
baseFee = '10'
deposits = [15, 29, 18, 7]
checkingAccount(customer_1, baseFee, deposits)

# Test input 2
print("Test#2")
customer_2 = "Joan"
baseFee = '10'
deposits = [36]
checkingAccount(customer_2, baseFee, deposits)

# Test input 3
print("Test#3")
customer_3 = "David"
baseFee = '20'
deposits = [3, 5, 2, 6]
checkingAccount(customer_3, baseFee, deposits)

# Test input 4
customer_4 = "Diana"
baseFee = '20'
deposits = []
checkingAccount(customer_4, baseFee, deposits)