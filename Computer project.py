#display GDP
GDP=0
private_consumption=int(input("Enter the private consumption: "))
gross_investment=int(input("Enter the gross investment: "))
government_investment=int(input("Enter the government investment: "))
government_spending=int(input("Enter the government spending: "))
exports=int(input("Enter the exports: "))
imports=int(input("Enter the imports: "))
GDP=private_consumption+ gross_investment + government_investment + government_spending + (exports - imports)
print("GDP = ",GDP)
print("*"*100)
#Unemployment Rate
Unemployment_Rate=0
Unemployed_People =int(input("Enter the Unemployed People : "))
Labor_Force =int(input("Enter the Labor Force : "))
Unemployment_Rate = Unemployed_People / Labor_Force * 100
print("Unemployment Rate = ",Unemployment_Rate)
print("*"*100)
#Inflation rate
Inflation_rate=0
Target_Year=int(input("Enter the Target Year: "))
Inflation_Base_Year=int(input("Enter the Inflation Base Year: "))
Inflation_rate=((Target_Year - Inflation_Base_Year)/Inflation_Base_Year) * 10
print("Inflation rate = ",Inflation_rate)
print("*"*100)
#intrest rate
r=P=t=I=0
I=int(input("Enter the Interest amount paid in a specific time period (month, year etc.): "))
P=int(input("Enter the Principle amount (the money before interest): "))
t=int(input("Enter the Time period involved: "))
r=(I/P*t)*100
print("intrest rate = ",r)
print("*"*100)
#industry output
industry=["Manufacturing production", "electrical produts", "mining"]
Base_year=[122, 203, 65]
current_year=[300, 400, 87]
by_current100=[245.9, 197.04, 133.8]
wt=[85,5,10]
qrw=[20901.5, 985.20, 1338]
iip=sum(qrw)/sum(wt)
print("Industry output = ",iip)
