def palin_check(mystring):
    if mystring == "q":
        return
    left = 0
    right = len(mystring) - 1
    
    while left <= right:
        if mystring[left] != mystring[right]:
            return f"The string {mystring} is not a palindrome"
        left += 1
        right -= 1
    return f"The string {mystring} is a palindrome"


while True:
    user_input = input("Enter a string (or 'q' to quit): ")
    result = palin_check(user_input)
    print(result)
    if user_input == "q":
        break



