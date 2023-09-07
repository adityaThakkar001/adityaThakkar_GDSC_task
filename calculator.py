import math

def calculate_expression(expression):
    try:
        expression = expression.replace('^', '**')
        result = eval(expression)
        if isinstance(result, float) and result.is_integer():
            return int(result)
        else:
            return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Invalid expression"
    except Exception as e:
        return f"An error occurred: {str(e)}"


expression = input("Enter an expression : ")
result = calculate_expression(expression)
print("Result:", result)
