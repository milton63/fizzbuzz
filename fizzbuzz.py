def fizzbuzz(number):
    return_values = []
    if number % 3 == 0:
        return_values += ["Fizz"]
    if number % 5 == 0:
        return_values += ["Buzz"]
    if not return_values:
        return number
    return " ".join(return_values)

