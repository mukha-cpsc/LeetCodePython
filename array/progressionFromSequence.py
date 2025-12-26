class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        srtd = sorted(arr)
        diff = srtd[1] - srtd[0]
        #print()
        n = len(arr)
        for i in range(1, n - 1):
            #print(srtd[i + 1] - srtd[i])
            if (srtd[i + 1] - srtd[i] != diff):
                return False
        return True
arr = [-68,-96,-12,-40,16]