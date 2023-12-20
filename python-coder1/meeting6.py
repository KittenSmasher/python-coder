# Function Project

def calculate_avg():
    scores = [70, 85, 90, 65, 80]  
    total = 0
    
    for score in scores:
        total += score
        
    avg = total/len(scores)
        
    if avg >= 70:
        status = 'Pass'
    else:
        status = 'Fail'
    
    print("Average score: ", avg)
    print("Pass status: ", status)

print("Exam Score Average Calculator")
calculate_avg()

def find_even_num():
    # number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_list = []
    count = int(input("Enter the number of values in the list: "))
    
    for i in range(count):
        value = int(input("Enter value: "))
        number_list.append(value)
    
    even_numbers = []
    
    for number in number_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

result = find_even_num()
print("Even numbers in the list:", result)
