def solution(strings, n):
    #list.sort() = 리스트 정렬하고 None반환
    #sorted(list) = 정렬된 리스트 반환(그 시점에만 정렬)
    
    strings.sort() #사전순으로 정렬먼저
    return sorted(strings,key=lambda strings: strings[n])
    
