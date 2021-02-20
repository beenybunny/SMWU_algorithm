def generate(chosen):
    if(len(chosen) == r):
        print(chosen)
        return

    start = 0
    if len(chosen)> 0 :
        start= arr.index(chosen[-1])+1
    #start = arr.index(chosen[-1])+1 if chosen else 0

    for nxt in range(start,len(arr)):
        chosen.append(arr[nxt])
        generate(chosen)
        chosen.pop()

def combination(arr):
    arr.sort()
    generate([])

r = 3
arr =[1,2,3,4,5]
combination(arr)