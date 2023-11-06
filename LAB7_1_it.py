import random


# Функція для генерації матриці
def process_matrix(matrix, rows, cols):
    count = 0
    total_sum = 0

    for i in range(rows):
        for j in range(cols):
            if j % 2 != 0 or i % 2 != 0 or matrix[i][j] % 7 == 0:
                count += 1
                total_sum += matrix[i][j]
                matrix[i][j] = 0

    return matrix, count, total_sum


def change(a, row1, row2, cols):
    for j in range(cols):
        tmp = a[row1][j]
        a[row1][j] = a[row2][j]
        a[row2][j] = tmp


def custom_sort(a, rows, cols):
    for i0 in range(rows - 1):
        for i1 in range(rows - i0 - 1):
            if (a[i1][0] < a[i1 + 1][0] or
                    (a[i1][0] == a[i1 + 1][0] and a[i1][1] > a[i1 + 1][1]) or
                    (a[i1][0] == a[i1 + 1][0] and a[i1][1] == a[i1 + 1][1] and a[i1][2] < a[i1 + 1][2])):
                change(a, i1, i1 + 1, cols)
    return a


# Функція для виведення матриці на екран
def print_matrix(matrix, index=0):
    for row in matrix:
        while index < len(row):
            print(f"{row[index]:>5}{'  ' if index == len(row) - 1 else ''}", end='')
            index += 1
        index = 0
        print()


def main():
    rows, cols = 8, 6
    lower_limit, upper_limit = 16, 97
    matrix = [[random.randint(lower_limit, upper_limit) for _ in range(cols)] for _ in range(rows)]

    print("Матриця до обробки:")
    print_matrix(matrix)

    sorted_matrix = custom_sort(matrix, rows, cols)

    print("\nМатриця після сортування:")
    print_matrix(sorted_matrix)

    matrix, count, total_sum = process_matrix(sorted_matrix, rows, cols)

    print("\nМатриця після обробки:")
    print_matrix(matrix)

    print(f"Кількість підходящих елементів: {count}")
    print(f"Сума підходящих елементів: {total_sum}")


if __name__ == "__main__":
    main()
