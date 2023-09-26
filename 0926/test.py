# import unittest
import myfunction

# class MyTest(unittest.TestCase) :
#     def test_sum(self):
#         self.assertEqual(myfunction.sum(2, 5), 7)
        
        
#     def test_multiple(self):
#         self.assertEqual(myfunction.multiple(2, 5), 10)

#pytest 활용 실습
def test_sum() :
    assert myfunction.sum(2, 5) == 7 #뒤의 조건이 거짓이면 error
    assert myfunction.sum(2.3, 5.2) == 7.5
    
def test_multiple() :
    assert myfunction.multiple(2, 5) == 10 #false 하나
    assert myfunction.multiple(2.0, 5.0) == 10.0
    
    

