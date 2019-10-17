from typing import List


def numbers_to_list(numbers: List[int]):
    #이 함수는 리스트를 나누는 함수입니다. [4, 5, 6, 9, 11, 12, 13] 이렇게 입력을 받으면 4,6 / 9 9/ 11 13 이런식으로 시작하는 숫자랑 끝나는 숫자로 나누어줍니다
    result = []
    start = numbers[0]
    end = numbers[0]
    pre = start

    for n in numbers[1:]:
        if n == pre + 1:
            end = n
        else:
            result.append([start, end])
            start = n
            end = n

        pre = n

    result.append([start, end])

    return result


def numbers_to_string(numbers: List[int]) -> str:
    #이 함수는 위의 함수로 나눈걸 문자열로 바꾸어 주는 함수입니다.
    num_list = numbers_to_list(numbers)
    answer = ""
    for n in num_list:
        if n[0] == n[1]:
            answer += str(n[0])
        else:
            answer += (str(n[0]) + '~' + str(n[1]))

        answer += ', '

    answer = answer[:-2]

# [4, 5, 6, 9, 11, 12, 13]
    return answer




if __name__ == "__main__":
    #list모양대로  [4, 5, 6, 9, 11, 12, 13] 이런식으로 입력하면 리스트 형태로 변환 할 수 있도록 했습니다
    list_input = input()
    num = list_input[1:-1]
    num = list(map(int, num.split(',')))

    result = numbers_to_string(num)

    print(result)
