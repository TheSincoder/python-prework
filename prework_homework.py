# Question 1
def hello_name(user_name):
    """Question 1: print 'hello_USERNAME!'"""
    print(f"hello_{user_name.upper()}!")


hello_name('creeves') 

# Question 2
def first_odds():
    """Question 2: count 1 - 100 only odd numbers"""
    odd_numbers = list(range(1,100,2))
    print(odd_numbers)
        
first_odds()

# Question 3
def max_num_in_list(a_list):
    """Question 3: return max number in the list"""
    print(max(a_list))

max_num_in_list(list(range(1,100001)))

# Question 4
def is_leap_year(a_year):
    """Question 4: Is the given year a leap year?"""
    if a_year % 400 == 0:
        leap_year = True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        leap_year = True
    else: leap_year = False
    
    return leap_year

print(is_leap_year(2022))


# Question 5
def is_consecutive(a_list_0):
    """Question 5: Are all numbers consective numbers?"""
    sorted(a_list_0)
    if min(a_list_0) + 1 == a_list_0[1] and a_list_0[1] + 1 == a_list_0[2] and a_list_0[2] +1 == a_list_0[3]:
        consectuve = True
    else:
        consectuve = False
    return consectuve

print(is_consecutive([1,2,3,4]))





   

