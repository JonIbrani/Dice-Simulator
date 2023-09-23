import random
def dice():
    if random.randint(1,6)==1:
        return "One"
    elif random.randint(1,6)==2:
        return "Two"
    elif random.randint(1,6)==3:
        return 'Three'
    elif random.randint(1,6)==4:
        return "Four"
    elif random.randint(1,6)==5:
        return "Five"
    else:
        return "Six"


number1 = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0
number6 = 0


roll = int(input('Enter how many time you want to roll the dice: '))
for trial in range(roll):
    if dice() == 'One':
        number1 += 1
    elif dice() == 'Two':
        number2 += 1
    elif dice() == 'Three':
        number3 += 1
    elif dice() == 'Four':
        number4 += 1
    elif dice() == 'Five':
        number5 +=1
    else:
        number6 +=1

print(f'Number of ones that have roled is {number1}, number of two that have roled is {number2}, number of threes that have roled is {number3}, number of fours that have roled is {number4}, number of fives that have roled is {number5},number of sixs that have roled is {number6}')
prob_1 = number1/roll
prob_2 = number2/roll
prob_3 = number3/roll
prob_4 = number4/roll
prob_5 = number5/roll
prob_6 = number6/roll

total_probability = prob_1 + prob_2 + prob_3 + prob_4 + prob_5 + prob_6
print(total_probability)
print(f'Probability of 1: {prob_1}, probability of 2: {prob_2}, probability of 3: {prob_3}, probability of 4: {prob_4}, probability of 5: {prob_5},probability of 6: {prob_6}')





