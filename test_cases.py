import math
from codecoverageanalysis import calculateAnnualPackage

def test_pckg():
   df = calculateAnnualPackage()
   assert df['YearlyPackage'][0] == 590000

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def tesequality():
   assert 10 == 12