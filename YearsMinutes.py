# function that takes the number of years as a parameter.
# function returns the number of minutes in that period.
# ask the user to input the number of years to be converted.
# display the number of minutes corresponding to the input.

def cal_min(years=0):
    num_min = num_years * 525600
    return num_min

num_years = int(input("Enter the number of years:"))
total = cal_min(num_years)
print("number of years:",total)