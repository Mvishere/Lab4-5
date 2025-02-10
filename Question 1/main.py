from input import take_input
from algorithms import dfs
from algorithms import bfs
from algorithms import dls
from algorithms import greedy
from algorithms import ucs
from algorithms import a_star

def main():
    row, column, start, end, matrix, algorithm = take_input()

    path = []
    if algorithm == "dfs":
        path = dfs.search(matrix, start, end)
    elif algorithm == "bfs":
        path = bfs.search(matrix, start, end)
    elif algorithm == "dls":
        path = dls.search(matrix, start, end)
    elif algorithm == "greedy":
        path = greedy.search(matrix, start, end)
    elif algorithm == "ucs":
        path = ucs.search(matrix, start, end)
    elif algorithm == "a_star":
        path = a_star.search(matrix, start, end)
    else:
        print("Invalid Input")
    with open("output.txt", "+a") as output_file:
        output_file.write(f"{algorithm}: {path}\n")

if __name__ == "__main__":
    main()