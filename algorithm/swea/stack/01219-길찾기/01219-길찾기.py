"""
# 길찾기
A 도시에서 출발하여 B 도시로 가는 길이 존재하는지

첫 줄에 테스트 케이스의 번호와 길의 총 개수, 그 다음 줄에 순서쌍
순서쌍의 경우, 숫자의 나열이며, 나열된 순서대로 순서쌍

# 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력
"""

for tc in range(10):
    num, road = map(int, input().split())

    node = [[] * 100 for _ in range(100)]
    pairs = list(map(int, input().split()))

    for i in range(0, road * 2, 2):  # 2씩 증가
        node[pairs[i]].append(pairs[i + 1])  # 0과 연결 : 0번째 리스트 삽입, 1과 연결 : 1번째 리스트 삽입

    stack = []  # stack
    while node[0]:  # 노드가 0인 동안에
        stack.append(node[0].pop())  # 출발지와 연결된 노드 stack 삽입

    ans = 0

    while stack:  # 스택이 빌 때까지
        new = stack.pop()  # 스택을 꺼내고

        if new == 99:  # 꺼낸 수가 도착지
            ans = 1  # 결과값 변경 후 종료
            break

        while node[new]:  # 현재 꺼낸 수와 연결된 수가 있는 동안에
            stack.append(node[new].pop())  # 연결 수 pop 후 stack 삽입

    print(f"#{tc + 1} {ans}")
