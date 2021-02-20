def generate(per_arr):
    global used

    if(len(per_arr) == r):
        print(per_arr)
        return #원소 개수가 r이 되면 멈춤

    for i in range(len(arr)): #arr개수만큼 도는거 ! per_arr이랑 안헷갈리는 이름으로 바꾸기
        if used[i] == 0 :
            per_arr.append(arr[i])
            used[i] = 1

            generate(per_arr)

            used[i] = 0
            per_arr.pop()

def permutaion(arr): #arr에서 r개의 순열 만들기
    arr.sort()
    generate([])


if __name__== "__main__":
    r = 3
    arr = [1,2,3,4,5]
    used = [0 for i in range(len(arr))]
    permutaion(arr)