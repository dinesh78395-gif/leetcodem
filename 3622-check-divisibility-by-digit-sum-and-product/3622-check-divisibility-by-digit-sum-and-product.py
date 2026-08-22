class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sums = 0
        product=1
        a = n 
        r = n
        while n>0:
            temp = n%10
            sums+=temp
            n//=10
        while a>0:
            ans= a%10
            product*=ans
            a//=10
        d = sums+product
        
        if(r % d == 0):
            return True
        else:
            return False

