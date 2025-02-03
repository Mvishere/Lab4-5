from input import take_input
from algorithms import dfs
from algorithms import bfs


def main():
    row, column, start, end, matrix, algorithm = take_input()

    paths = []
    if algorithm == "dfs":
        paths = dfs.search(matrix, start, end)
    elif algorithm == "bfs":
        paths = bfs.search(matrix, start, end)
    else:
        print("Invalid Input")
    for i in paths:
        print(i)

if __name__ == "__main__":
    main()