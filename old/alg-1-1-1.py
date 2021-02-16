def is_palindrome(word):
    word_list = list(word)

    word_half_len = int(len(word_list))

    result_same = True

    for i in range(word_half_len):
        front_letter =  word_list[i]
        #print(front_letter)
        end_letter = word_list[-(i+1)]
        #print(end_letter)
        if front_letter != end_letter:
            result_same= False
            break

    return result_same



print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))