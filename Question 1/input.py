def take_input():
    with open("input.txt", "r") as input_file:
        row, column = map(int, input_file.readline().strip().split(","))
        start, end = input_file.readline().strip().split(";")
        blocked = input_file.readline().strip().split(";")
        algorithm = input_file.readline().strip()

        matrix = [[0]*column for i in range(row)]
        
        start_i, start_j = map(int, start.split(","))
        end_i, end_j = map(int, end.split(","))

        for coordinate in blocked:
            coor_i, coor_j = map(int, coordinate.split(","))
            matrix[coor_i-1][coor_j-1] = -1

        return [row, column, (start_i-1, start_j-1), (end_i-1, end_j-1), matrix, algorithm]