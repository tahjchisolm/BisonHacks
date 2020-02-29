import math

def MonthlyPayments():
	amount = int(input('Enter your loan amount($): '))
	rate = float(input('Enter your interest rate(%): '))
	rate = rate/1200 # percentage per month
	time = int(input('Enter your goal term(years): '))
	time = time*12 # time in months

	monthly = amount / (((1+rate)**time-1)/(rate*(1+rate)**time))
	monthly = round(monthly, 2)
	return monthly

def Term():
	amount = int(input('Enter your loan amount($): '))
	rate = float(input('Enter your interest rate(%): '))
	rate = rate/1200 # percentage per month
	monthly = float(input('Enter your desired monthly payment($): '))
	

	time = math.log(monthly/(monthly-rate*amount))/math.log(1+rate)
	return round(time)



answer = input("Are you trying to determine loan term(t) or monthly payment(p)?")
if answer == 't':
	time = Term()
	print("It would take you approximately" , time, "months or", round(time/12), "years.")
if answer == 'p':
	print("Your monthly payment is: $" , MonthlyPayments())
