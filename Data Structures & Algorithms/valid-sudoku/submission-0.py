class Solution:

    def containDuplicate(self, strs:List[str]) -> bool:
        seen = []
        for s in strs:
            if s == ".":
                continue
            if s in seen:
                return True
            seen.append(s)
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            if self.containDuplicate(row):
                return False

        # check columns
        for i in range(9):
            strs = []
            for row in board:
                strs.append(row[i])
            if self.containDuplicate(strs):
                return False
        
        # check 3x3 sub boxes
        sub_boxes = defaultdict(list)
        for i in range(9):
            for j, row in enumerate(board):
                sub_boxes[(math.floor(i/3),math.floor(j/3))].append(row[i])
        for value in sub_boxes.values():
            if self.containDuplicate(value):
                return False
    
        return True