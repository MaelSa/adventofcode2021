def checkLines(board, calledNumbers):
    for line in board:
        broken = False 

        for number in line:
            if number not in calledNumbers:
                broken = True
                break    
        if not broken:
            s = sum([sum(l) for l in board])
            return s - sum(line) 
    return 0 
    


def linesToColumns(board):
    columns = [[] for i in range(len(board[0]))]
    for line in board:
        for i in range(len(line)):
            columns[i].append(line[i])
    return columns



data = open("day4_data","r")
L = [i for i in data.read().split('\n')]
numbersToCall = [int(i) for i in L[0].split(',')]

L = L[2:]
numberOfBoards = len(L)//6 +1 
boards = []
for i in range(numberOfBoards):
    rawBoard = L[i*6:i*6+5]
    board = []
    for line in rawBoard:
        board.append([int(i) for i in line.split()])
    boards.append(board)
resF = -1
winningBoard = []
for n in range(len(numbersToCall)):
    calledNumbers = numbersToCall[:n+1]
    winningBoards = []
    for board in boards:
        winningBoard = board
        res = checkLines(board, calledNumbers)
        if res !=0: 
           winningBoards.append(board) 
        columns = linesToColumns(board)
        res = checkLines(columns, calledNumbers)
        if res !=0: 
            winningBoards.append(board)
    for board in winningBoards:
        if len(boards) == 1:
            print(len(winningBoards))
            resF = 0
            break
        if board in boards:
            boards.remove(board)
    if resF == 0:
        break

sumUnmarked = 0
print(winningBoard)
print(len(calledNumbers))
for line in winningBoard:
    for number in line:
        if number not in calledNumbers:
            sumUnmarked += number

print(sumUnmarked*calledNumbers[-1])
print(checkLines(linesToColumns(winningBoard), calledNumbers))

finalBoard = [[50, 66, 43, 39, 16], [88, 94, 60, 70, 64], [63, 80, 56, 69, 36], [53, 48, 32, 22, 79], [59, 77, 20, 30, 67]]

for n in range(len(numbersToCall)):
    calledNumbersFinal = numbersToCall[:n+1]
    s = checkLines(finalBoard, calledNumbersFinal)
    if s!=0:
        print('done')
        print(n)
        break
    s = checkLines(linesToColumns(finalBoard), calledNumbersFinal) 
    if s!=0:
        print('done')
        print(n)
        break
sumUnmarked = 0
for line in finalBoard:
    for number in line:
        if number not in calledNumbersFinal:
            sumUnmarked += number

print(sumUnmarked*calledNumbersFinal[-1])