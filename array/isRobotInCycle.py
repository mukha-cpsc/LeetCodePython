class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        move_count = {}
        start_x = 0
        start_y = 0
        direction = "North"
        move_count[(start_x, start_y)] = 1
        for move in instructions:
            if move == "G":
                if direction == "North":
                    start_y += 1


            move_count[(start_x, start_y) ]