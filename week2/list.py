def fast_transpose(sparse_matrix, rows, cols):
    """
    sparse_matrix: 리스트 형태의 희소행렬 [행, 열, 값]
    rows: 원래 행렬의 행 개수
    cols: 원래 행렬의 열 개수
    """
    num_terms = len(sparse_matrix)  # 0이 아닌 값 개수

    # 1단계: 각 열에 몇 개의 항목이 있는지 count
    row_terms = [0] * cols
    for term in sparse_matrix:
        row_terms[term[1]] += 1  # 열 기준으로 세기

    print("rowterm:" ,row_terms)
    # 2단계: 시작 위치(starting position) 계산
    starting_pos = [0] * cols
    starting_pos[0] = 0
    for i in range(1, cols):
        starting_pos[i] = starting_pos[i - 1] + row_terms[i - 1]
    print("starting_pos:",starting_pos)

    # 3단계: 전치된 행렬을 새로운 리스트에 저장
    transposed = [None] * num_terms
    for term in sparse_matrix:
        col = term[1]
        pos = starting_pos[col]
        transposed[pos] = [term[1], term[0], term[2]]  # 열과 행을 바꿔서 저장
        starting_pos[col] += 1

    return transposed

# [0, 0, 5, 0]
# [3, 8, 0, 0]
# [0, 0, 0, 6]

# 예제 희소행렬 (행, 열, 값)
sparse_matrix = [
    [0, 1, 4],
    [0, 2, 5],
    [1, 0, 3],
    [1, 1, 8],
    [2, 3, 6]
]

rows = 3  # 원래 행 수
cols = 4  # 원래 열 수

print("원본 희소행렬 (row, col, value):")
for row in sparse_matrix:
    print(row)

transposed_matrix = fast_transpose(sparse_matrix, rows, cols)

print("\n전치된 희소행렬 (row, col, value):")
for row in transposed_matrix:
    print(row)
