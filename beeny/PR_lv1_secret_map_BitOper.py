def solution(n, arr1, arr2):
    answer = []
    bin_format = "0" + str(n) + "b"

    for i in range(n):
        ans = ""
        a = format(arr1[i], bin_format)
        b = format(arr2[i], bin_format)
        for j in range(n):
            if int(a[j]) | int(b[j]) == 1:
                ans += "#"
            else:
                ans += " "
        answer.append(ans)
    print(answer)
    return answer

if __name__ == "__main__":
    solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])