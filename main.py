# Apollos Eastman
# Dec 10 2024
# While loop practice

# 7-5 Movie Tickets and 7-6 Three exits
run = True

while run == True:
    age = input('Enter your age or "exit" to quit:')
    
    if age == 'exit':
        break
    
    if age.isdigit():
        age = int(age)

        if age < 200 and age > 0:
            if age > 12:
                print('Your ticket costs $15!')
                run = False
        
            elif age < 3:
                print('Your ticket is free!')
                run = False
        
            elif age <= 12:
                print('Your ticket costs $10!')
                run = False
        
        else:
            print('Invalid input, try again.')
    
    else:
        print('Invalid input, try again.')

print('End.')
