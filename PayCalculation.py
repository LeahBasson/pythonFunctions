# function that calculates and return the overtime due to the employee.
def overtime_due(ovt_hours=0, hr_wage=0):
    overtime_pay = overtime_hours * 1.5 * hourly_wage 
    return overtime_pay

print("Overtime")
# read in overtime hours
overtime_hours = int(input("Enter overtime hours:"))
hourly_wage = int(input("Enter the hourly wage: "))

#overtime_due
overtime_pay = overtime_due(overtime_hours, hourly_wage)
print("overtime due: R", overtime_pay)

print("\nTotal pay")

# function that calculates and returns the total pay due to an employee.
def pay_due(hr_wage=0,reg_hr=0):
    pay_due = hourly_wage * reg_hours + overtime_pay
    return pay_due
  
# read in regular hours
reg_hours = int(input("Enter regular hours:"))

# total pay
weekly_pay = pay_due(hourly_wage,reg_hours)
print("weekly pay: R", weekly_pay)
    