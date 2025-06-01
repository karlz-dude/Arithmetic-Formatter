def arithmetic_formatter(problems, show_answers=False):
    # Tasks: Not more than 5 problems, Not more than 4 digits, only + -, show answers when true, only numbers 
    if len(problems) > 5:
        return 'Error: Not more than 5 problems'
    
    first_number = []
    second_number = []
    dashes = []
    answere = []

    for problem in problems:
        parts = problem.split()

        left, operator, right = parts

        # Additional check to see if it is right format
        if len(parts) != 3:
            return 'Error: Invalid format'

        # Only numbers
        if not left.isnumeric() or not right.isnumeric():
            return 'Error: Only Numbers'

        # Max 4 Digits
        if len(left) > 4 or len(right) > 4:
            return 'Error: Not more than 4 digits'

        # Only + and - 
        if operator not in ['+', '-']:
            return 'Error: Only use "+" or "-"'

        # Formatting
        width = max(len(left), len(right)) + 2
        first_number.append(left.rjust(width))
        second_number.append(operator + right.rjust(width - 1))
        dashes.append(width * '_')
        # Calculate answere
        if show_answers:
            if operator == '+':
                result = str((int(left) + int(right)))
                answere.append(result.rjust(width))
            else:
               result = str((int(left) - int(right)))
               answere.append(result.rjust(width))
               
    #Arrange Numbers
    arranged = ('    ' .join(first_number) + '\n' +
                '    ' .join(second_number) + '\n' +
                '    ' .join(dashes) + '\n')
     
    
    #Arrange the Answere as well
    if show_answers: 
        arranged += '\n' + '    '.join(answere)
        
    return arranged
    

# Run the function
print(arithmetic_formatter(['212 - 12', '67 + 181', '50 + 50', '64 - 31'], True))
