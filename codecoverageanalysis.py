import pandas as pd

data = {'EmpID':[111,112,113,114,115,116,117,118],
        'EmpFirstName':['SRavi', 'SShubham', 'SRishabh', 'SSandeep', 'SSourabh', 'SSumanth', 'SKuldeep', 'SAjay'],
        'EmpLastName':['Jha', 'Singh', 'Sharma', 'Dhama', 'Gupta', 'Kumar', 'Negi', 'Kanojiya'],
        'MonthlySalary':[45000.00, 50000.00, 65000.00, 43000.00, 80000.00, 44000.00, 76000.00, 56000.00,]
}

def loadData():
  dataframe = pd.DataFrame(data)
  return dataframe

def AnnualPackage():
  dataframe = loadData()
  yearlyPkg =[]
  for msalary in dataframe['MonthlySalary']:
        yearlyPkg.append(msalary*12+50000)
  dataframe['YearlyPackage'] = yearlyPkg
  for indx in dataframe['YearlyPackage'].index:
        print(f"{dataframe['EmpFirstName'][indx]} {dataframe['EmpLastName'][indx]} Yearly Package is {dataframe['YearlyPackage'][indx]}")
  return dataframe

#calculateAnnualPackage()
