class math:
    def fibnaci(self,n:int)-> int:
        self.n = n
        if n==1:
            return n
        else:
            return n + fibnaci(n-1)

     
