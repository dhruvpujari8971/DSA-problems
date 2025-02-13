def word_to_number(word_number: str):
    num_dict = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
        "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90
    }
    
    words = word_number.lower().split()
    result = 0
    temp = 0
    
    for word in words:
        if word in num_dict:
            temp += num_dict[word]
        elif word == "hundred":
            temp *= 100
        elif word == "thousand":
            result += temp * 1000
            temp = 0
        elif word=="lakh":
            result += temp * 100000
            temp = 0
        elif word == "million":
            result += temp * 1000000
            temp = 0
        elif word == "crore":
            result += temp * 10000000
            temp = 0
        
    
    return result + temp

# Example usage
word_input = input("Enter the amount in words!")
numeric_value = word_to_number(word_input)
print("Numeric value:", numeric_value)
