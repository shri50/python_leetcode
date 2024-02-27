

class Solution:
    def perfect_sqrt(self,num: int)-> bool:
        "using the binary search approach "
        low,high = 1, num//2

        while(low <= high):
            mid = (low + high) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                low = mid+1
            else:
                high = mid-1  
        return False


    def perfect_sqrt_(self, num:int) -> bool:
        "using simple math function"
        if num > 0:
            sq_rt = int(num ** 0.5)
            return sq_rt * sq_rt == num
        

sol = Solution()

print(sol.perfect_sqrt(16))
print(sol.perfect_sqrt(25))

print(sol.perfect_sqrt_(16))
print(sol.perfect_sqrt_(25))
print(sol.perfect_sqrt_(15))


