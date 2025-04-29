with open("output.txt", "w") as output_file:

    def bfs(world : list[list[int]], start):
        queue : list[int] = []
        visited: list[int] = [[0]*len(world[0]) for i in range(len(world[0]))]
        queue.append(((start-1)//2, start%2-1))

        while queue:
            curr_room = queue.pop(0)
            
            if visited[curr_room[0]][curr_room[1]]:
                continue
            
            curr_room_number = len(world[0])*curr_room[0] + curr_room[1] + 1

            if world[curr_room[0]][curr_room[1]] == 1:
                output_file.write(f"{curr_room_number},S\n")
                print(f"{curr_room_number},S")
            else:
                output_file.write(f"{curr_room_number},N\n")
                print(f"{curr_room_number},N")

            if curr_room[0] != 0:
                queue.append((curr_room[0]-1, curr_room[1], "U", curr_room_number))

            if curr_room[1] != len(world[0])-1:
                queue.append((curr_room[0], curr_room[1]+1, "R", curr_room_number))

            if curr_room[0] != len(world)-1:
                queue.append((curr_room[0]+1, curr_room[1], "D", curr_room_number))

            if curr_room[1] != 0:
                queue.append((curr_room[0], curr_room[1]-1, "L", curr_room_number))

            if queue and not visited[queue[0][0]][queue[0][1]]:
                next_room_number = queue[0][3]
                output_file.write(f"{next_room_number},{queue[0][2]}\n")
                print(f"{next_room_number},{queue[0][2]}")

            visited[curr_room[0]][curr_room[1]] = 1

    def dfs(world : list[list[int]], visited: list[list[int]], curr_room):
        if curr_room[0] < 0 or curr_room[1] < 0 or curr_room[0] > len(world[0]) - 1 or curr_room[1] > len(world) - 1:
            return
        
        if visited[curr_room[0]][curr_room[1]]:
            return
        
        curr_room_number = len(world[0])*curr_room[0] + curr_room[1] + 1
        
        if curr_room[2] != -1:
            output_file.write(f"{curr_room[2]},{curr_room[3]}\n")
            print(f"{curr_room[2]},{curr_room[3]}")

        if world[curr_room[0]][curr_room[1]]:
            output_file.write(f"{curr_room_number},S\n")
            print(f"{curr_room_number},S")
        else:
            output_file.write(f"{curr_room_number},N\n")
            print(f"{curr_room_number},N")

        visited[curr_room[0]][curr_room[1]] = 1

        dfs(world, visited, (curr_room[0]-1, curr_room[1], curr_room_number, "U"))

        dfs(world, visited, (curr_room[0], curr_room[1]+1, curr_room_number, "R"))

        dfs(world, visited, (curr_room[0]+1, curr_room[1], curr_room_number, "D"))

        dfs(world, visited, (curr_room[0], curr_room[1]-1, curr_room_number, "L"))


    with open("input.txt", "r") as input_file:
        input = input_file.readlines()
        start = int(input[0].strip())
        world = [[0, 0], [0, 0]]
        dirt = list(map(int, input[1].split(",")))
        for i in range(2):
            for j in range(2):
                world[i][j] = dirt.pop(0)

        if input[2].strip() == "dfs":
            dfs(world, [[0, 0], [0, 0]], ((start-1)//2, start%2-1, -1, -1))
        else:
            bfs(world, start)