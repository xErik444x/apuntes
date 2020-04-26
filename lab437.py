def isYearLeap(year):
    if (year % 4 == 0):
        if ( year % 100== 0):
            if( year % 400== 0):
                return(True)
            else:
                return(False)
        else:
            return(True)
    else:
        return(False)

def daysInMonth(year, month):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return(31)
        elif month == 6 or month == 4 or month == 9 or month == 11:
            return(30)
        elif month == 2:
            if(isYearLeap(year)):
                return(29)
            else:
                return(28)
        else:
            return(0)

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]


for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
