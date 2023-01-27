def checkPallindrome(word):
    isPallindrome = True
    
    if len(word) < 1:
        return -1
    elif len(word) == 1:
        return isPallindrome
    
    start = 0
    end = len(word) - 1
    while start < end:
        if word[start] != word[end]:
            isPallindrome = False
            break
        start += 1
        end -= 1
    return isPallindrome

word = "aabbaa"
print(checkPallindrome(word))
