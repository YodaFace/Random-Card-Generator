import random
suites = ['♡', '♢', '♤', '♧']
values = list(range(1,14))
# high_values = 

def get_random_card():
    # your code here
    suite = random.choice(suites)
    value = str(random.choice(values))
    if value == "11":
        value = "J"
    elif value == "12":
        value = "Q"
    elif value == "13":
        value = "K"
    elif value == "14":
        value = "A"
    random_card = suite + str(value)
    return random_card

print(get_random_card())