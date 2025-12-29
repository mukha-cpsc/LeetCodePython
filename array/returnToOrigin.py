class Solution:
    def judgeCircle(self, moves) -> bool:
        x_start, y_start = 0, 0
        for move in moves:
            #print(x_start, y_start)
            if move == "U":
                y_start += 1
            if move == "D":
                y_start -= 1
            if move == "L":
                x_start -= 1
            if move == "R":
                x_start += 1
        if x_start == y_start == 0:
            return True
        return False
moves = "RLUURDDDLU"
print(Solution.judgeCircle(Solution(), moves))