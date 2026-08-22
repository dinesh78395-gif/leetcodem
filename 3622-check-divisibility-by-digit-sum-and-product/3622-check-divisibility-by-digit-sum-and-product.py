class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sums = 0
        product=1
        
        r = n
        while n>0:
            temp = n%10
            sums+=temp
            product*=temp
            n//=10
        
        d = sums+product
        
        if(r % d == 0):
            return True
        else:
            return False

