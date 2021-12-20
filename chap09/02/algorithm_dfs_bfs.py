'''
n개의 음이 아닌 정수가 있습니다. 
이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 
타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 
solution 함수를 작성해주세요.

제한사항
- 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
- 각 숫자는 1 이상 50 이하인 자연수입니다.
- 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
'''

def bfs_solution(numbers, target):
    answer = 0
    leaves = [0]

    for number in numbers:
        temp = []

        # 더하거나 뺀 경우를 수평적으로 추가해 준다.
        for parent in leaves:
            temp.append(parent + number)
            temp.append(parent - number)
        
        leaves = temp

    # 모든 결과는 leaves에 담기게 된다.
    for leaf in leaves:
        if leaf == target:
            answer += 1
    
    return answer

#깊이우선탐색
def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        return 1 if sum(numbers) == target else 0
    else:
        answer += DFS(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        return answer

def dfs_solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer

#모든 경우의 수에서 재귀를 쓰는 것  같다.
print(bfs_solution([1,1,1,1,1], 3))
