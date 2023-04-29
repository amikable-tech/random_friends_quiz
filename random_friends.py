import random
num_friends = random.randint(2,10)
each_friends_cash = random.randint(10,75) #money each friend can afford to pay 
total_bill = (num_friends * each_friends_cash)
#picking a random amount of money from the friends regardless of how much is in their pockets
friends_bill = [random.randint(5, 100) for _ in range(each_friends_cash)] 
avg_bill = total_bill//num_friends

#check if any friend paid to little or too much
bill_difference = [bill - avg_bill for bill in friends_bill]
#next
for i in range(num_friends):
    if bill_difference [i] > 15:
        print(f'friend {i+1} paid €{bill_difference[i]:.2f} paid too much.')
    elif bill_difference[i] < 10:
         friends_bill[i] += abs(bill_difference[i])
    bill_difference[i] = 0
    print(f'friend {i + 1} paid €{bill_difference[i]:.2f} paid too little.' )
else:
        print(f'friend{i+1} paid the right amount.')



