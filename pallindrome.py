def checkPallindrome(word):
    if len(word) < 1:
        return -1
    
    isPallindrome = True
    start = 0
    end = len(word) - 1
    while start < end:
        if word[start] != word[end]:
            isPallindrome = False
            break
        
        start += 1
        end -= 1
    return isPallindrome

word = "abbaa"
print(checkPallindrome(word))
