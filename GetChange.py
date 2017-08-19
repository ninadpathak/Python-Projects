def main():
    one_rupee = 100
    count_five, count_ten, count_hundred = 0, 0, 0
    amount = int(input("Enter the amount in paise: "))
    count_one = int(amount / one_rupee)

# This was the code I tried before. Takes too much computation

#   while count_one >= 5:
#        count_one -= 5
#        count_five += 1
#        if count_five == 2:
#            count_five = 0
#            count_ten += 1
#            if count_ten == 10:
#                count_ten = 0
#                count_hundred += 1

    if amount < 100:
        print("Amount too small to divide")
        exit()

    count_hundred = int(amount / 10000)
    amount -= (count_hundred * 10000)
    count_ten = int(amount / 1000)
    amount -= (count_ten * 1000)
    count_five = int(amount / 500)
    amount -= (count_five * 500)
    count_one = int(amount / 100)
    amount -= (count_one * 100)

    print("You'll need the following breakup of coins")
    print("One Rupee coins: ", count_one)
    print("Five rupee coins: ", count_five)
    print("Ten rupee notes: ", count_ten)
    print("Hundred rupee notes: ", count_hundred)


main()