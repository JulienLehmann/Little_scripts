# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 23:28:14 2022

@author: jlski
"""

from interval import Interval

def test_addition():
    print("TEST ADDITION")
    a = Interval('1','2')
    b = Interval('3','4')
    c = Interval('-1.5','1')
    print(str(a) + " + " + str(b) + " + " + str(c) + " should return [2.5;7] :")
    print(a+b+c)
    # print(a+b+c == Interval('2.5','7'))

test_addition()

def test_substraction():
    print("TEST SUBSTRACTION")
    a = Interval('1','2')
    b = Interval('3','4')
    c = Interval('-1.5','1')
    print("- " + str(a) + " - " + str(b) + " - " + str(c) + " should return [-7;-2.5] :")
    print(-a-b-c)
    # print(b-a-c == Interval('-7','-2.5'))

test_substraction()

def test_multiplication():
    print("TEST MULTIPLICATION")
    a = Interval('1','2')
    b = Interval('3','4')
    c = Interval('-1.5','1')
    
    #+*+
    print(str(a) + " * " + str(b) + " should return [3;8]")
    print(a*b == Interval(3,8))
    #+*-
    print(str(a) + " * " + str(-b) + " should return [-8;-3]")
    print(a*-b == Interval(-8,-3))
    #+*~
    print(str(a) + " * " + str(c) + " should return [-3;2]")
    print(a*c==Interval(-3,2))
    #~*-
    print(str(c) + " * " + str(-a) + " should return [-2;3]")
    print(c*-a==Interval(-2,3))
    #~*~
    e = Interval('-3','3')
    print(str(c) + " * " + str(e) + " should return [-4.5;4.5]")
    print(c*e==Interval(-4.5,4.5))
    #~*+
    print(str(c) + " * " + str(a) + " should return [-3;2]")
    print(c*a==Interval(-3,2))
    #-*-
    print(str(-a) + " * " + str(-b) + " should return [3;8]")
    print(-a*-b==Interval(3,8))
    #-*~
    print(str(-a) + " * " + str(c) + " should return [-2;3]")
    print(-a*c==Interval(-2,3))
    #-*+
    print(str(-a) + " * " + str(b) + " should return [-8;-3]")
    print(-a*b==Interval(-8,-3))
    
    
test_multiplication()

def test_division():
    print("TEST DIVISION")
    a = Interval('1','2')
    b = Interval('3','4')
    c = Interval('-1.5','1')
    e = Interval('0','0.5')
    #+*+
    print(str(a) + " / " + str(b) + " should return [1/4;2/3]")
    print(a/b)
    print(str(a) + " / " + str(c) + " should return [-Infinity;-2/3] U [1;Infinity]")
    res_div = a/c
    print(res_div[0] , res_div[1])
    print(str(-a) + " / " + str(e) + " should return [-Infinity;-2]")
    print(-a/e)


test_division()




def test_addition_substraction_technical():
    a = Interval('0.100000000000000000000000001','0.100000000000000000000000001')
    print("a is the following interval ",a)
    b = a+a
    print("b is the result of a + a :", b)
    b-=a
    print("b is now the result of a + a - a :",b)
    print("b.contains(.1)",b.contains(.1))
    print("b.contains('.1')",b.contains('.1'))

test_addition_substraction_technical()

"""Return :
    a is the following interval  [0.100000000000000000000000001 ; 0.100000000000000000000000001]
    b is the result of a + a : [0.20000000000000000000000000 ; 0.20000000000000000000000001]
    b is now the result of a + a - a : [0.099999999999999999999999999 ; 0.10000000000000000000000001]
    b.contains(.1) False
    b.contains('.1') True
"""
