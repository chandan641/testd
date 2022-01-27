import math
from codecoverage import AnnualPackage

#test cases
def test_pckg():
   df = AnnualPackage()
   assert df['YearlyPackage'][0] == 590000

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def tesequality():
   assert 10 == 12
