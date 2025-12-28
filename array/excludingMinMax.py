class Solution:
    def average(self, salary) -> float:
        mn = 1000000
        mx = 0
        total = 0
        for sal in salary:
            total += sal
            if sal < mn:
                mn = sal
            if sal > mx:
                mx = sal
        return float ((total - mn - mx) / (len(salary) - 2))
salary = [4000,3000,1000,2000]
print(Solution.average(Solution(), salary))