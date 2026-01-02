class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        Solution.allCombosBrackets(Solution(), n, 0, 0, "", res)
        for elem in res[:]:
            if (len(elem) % 2 != 0):
                res.remove(elem)
        print(res)



    def allCombosBrackets(self, n, open, closed, current, res):
        if n == 0:
            return []
        if closed == n:
            res.append(current)
            return
        # Decision 1
        if open < n :
            #print("Before change(open-branch):", current)
            current += '('
            #print("After change(open-branch):", current)
            Solution.allCombosBrackets(Solution(), n, open + 1, closed, current, res)
            current = current[ : len(current) - 1]
        #Decision 2
        if closed < open:
            #print("Before change(closed-branch):", current)
            current += ')'
            #print("Before change(closed-branch):", current)
            Solution.allCombosBrackets(Solution(), n, open, closed + 1, current, res)
            current = current[: len(current) - 1]
        return None


n = 3
Solution.allCombosBrackets(Solution(), n, 0, 0, "", [])
Solution.generateParenthesis(Solution(), n)