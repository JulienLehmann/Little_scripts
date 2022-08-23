# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 23:24:44 2022

@author: jlski
"""

import decimal as d

class Interval:
    
    
    """Type recommandé : str"""
    def __init__(self,inf : str ,sup : str, prec : int = 26):
        assert inf<=sup, " inf (" + str(inf) + ") need to be less than or equal to sup (" + str(sup) + ")."
        d.getcontext().prec = prec
        self.prec = prec
        
        d.getcontext().rounding = d.ROUND_FLOOR
        self.inf = d.Decimal(inf)
        d.getcontext().rounding = d.ROUND_CEILING
        self.sup = d.Decimal(sup)

    
    
    def __add__(self,e):
        d.getcontext().rounding = d.ROUND_FLOOR
        i = self.inf + e.inf
        d.getcontext().rounding = d.ROUND_CEILING
        s = self.sup + e.sup
        
        return Interval(i,s,self.prec)
    
    # def __iadd__(self,e):

    #     return self.__add__(e)
    
    def __sub__(self,e):
        d.getcontext().rounding = d.ROUND_FLOOR
        i = self.inf - e.sup
        d.getcontext().rounding = d.ROUND_CEILING
        s = self.sup - e.inf
        return Interval(i,s,self.prec)
    
    def __neg__(self):
        return Interval(-self.sup,-self.inf,self.prec)
    
    # def __isub__(self,e):
    #     self.inf -= e.sup
    #     self.sup -= e.inf
    #     return self
    
    def __mul__(self,e):
        # #EASIER
        # d.getcontext().rounding = d.ROUND_FLOOR
        # i = min(self.inf * e.inf, self.inf * e.sup, self.sup * e.inf, self.sup * e.sup)
        # d.getcontext().rounding = d.ROUND_CEILING
        # s = max(self.inf * e.inf, self.inf * e.sup, self.sup * e.inf, self.sup * e.sup)
       
        #FASTER but way too much test 
        if self>=0 and e >=0:
            d.getcontext().rounding = d.ROUND_FLOOR
            i = self.inf * e.inf
            d.getcontext().rounding = d.ROUND_CEILING
            s = self.sup * e.sup
            # print("+ +")
        elif self<=0 and e<=0 :
            d.getcontext().rounding = d.ROUND_FLOOR
            i = self.sup * e.sup
            d.getcontext().rounding = d.ROUND_CEILING
            s = self.inf * e.inf
            # print(" - - ")
        elif e>=0 and self<=0:
            d.getcontext().rounding = d.ROUND_FLOOR
            i = self.inf * e.sup
            d.getcontext().rounding = d.ROUND_CEILING
            s = self.sup * e.inf
            # print(" - +")
        elif self>=0 and e<=0:
            d.getcontext().rounding = d.ROUND_FLOOR
            i = self.sup * e.inf
            d.getcontext().rounding = d.ROUND_CEILING
            s = self.inf * e.sup 
            # print(" + -")
        elif e>=0:
            d.getcontext().rounding = d.ROUND_FLOOR
            i = self.inf * e.sup
            d.getcontext().rounding = d.ROUND_CEILING
            s = self.sup * e.sup
            # print(" ~ +")
        elif e<=0:
            d.getcontext().rounding = d.ROUND_FLOOR
            i = self.sup * e.inf
            d.getcontext().rounding = d.ROUND_CEILING
            s = self.inf * e.inf
            # print(" ~ -")
        elif self>=0 :
            d.getcontext().rounding = d.ROUND_FLOOR
            i = self.sup * e.inf
            d.getcontext().rounding = d.ROUND_CEILING
            s = self.sup * e.sup
            # print( "+ ~ ")
        elif self<=0:
            d.getcontext().rounding = d.ROUND_FLOOR
            i = self.inf * e.sup
            d.getcontext().rounding = d.ROUND_CEILING
            s = self.inf * e.inf
            # print(" - ~ ")
        else:
            #Meaning both self and e can contains 0 => thus
            #self.inf and e.inf are negative and self.sup and e.sup are positive
            d.getcontext().rounding = d.ROUND_FLOOR
            i = min(self.inf * e.sup, self.sup * e.inf)
            d.getcontext().rounding = d.ROUND_CEILING
            s = max(self.inf * e.inf, self.sup * e.sup)
            # print(" ~ ~ ")
        return Interval(i,s,self.prec)
    
    def __truediv__(self,e):
        if not e.contains(0):
            d.getcontext().rounding = d.ROUND_FLOOR
            i = 1/e.sup
            d.getcontext().rounding = d.ROUND_CEILING
            s = 1/e.inf
        elif e.inf == 0:
            d.getcontext().rounding = d.ROUND_FLOOR
            i = 1/e.sup
            s = d.Decimal('inf')
        elif e.sup == 0:
            d.getcontext().rounding = d.ROUND_CEILING
            i = d.Decimal('-inf')
            s = 1/e.inf
        else:
            d.getcontext().rounding = d.ROUND_CEILING
            a = 1/e.inf
            d.getcontext().rounding = d.ROUND_FLOOR
            b = 1/e.sup
            neg_interv = self * Interval(d.Decimal('-inf'), a)
            pos_interv = self * Interval(b,d.Decimal('inf'))
            return [neg_interv,pos_interv]
        return self * Interval(i,s)
    
    def __ge__(self,e : str):
        return self.inf >= d.Decimal(e)
    
    def __gt__(self, e : str):
        return self.inf >= d.Decimal(e)
    
    def __le__(self,e : str):
        return self.sup <= d.Decimal(e)
    
    def __lt__(self,e : str):
        return self.sup < d.Decimal(e)
    
    def __eq__(self,e):
        return self.inf == e.inf and self.sup == e.sup
    
    def contains(self,e : str):
        return self.inf<=d.Decimal(e) and self.sup>=d.Decimal(e)
    
    def __str__(self):
        return "[" + str(self.inf) + " ; " + str(self.sup) + "]"
    
    
