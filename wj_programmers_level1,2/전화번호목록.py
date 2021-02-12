def solution(phone_book):
    answer = True
    phone_book.sort()
    for p in range(0,len(phone_book)-1):
        if phone_book[p] in phone_book[p+1]:
            answer = False
            return answer
        
    return answer
