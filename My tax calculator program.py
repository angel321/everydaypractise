# I have kept this amount in a global variable because it will be used for all
allowable_expense=240000

def taxable_amount_after_exemtion(yearly_gross_salary,exempted_amount):
    """
    I am defining  function which calculates total taxable amount
    """
    return yearly_gross_salary-exempted_amount-allowable_expense


def calculate_tax_on_taxable_amount(taxable_amount):
    """
    I am defining a function which calculates total amount of tax on taxable amount
    """
    total_tax_amount=0
    if taxable_amount<0:
        print"You do not have to pay any tax"
        return 0
    if taxable_amount>300000:
        print "\tIs the first slab of your taxable amount>300000?\n True"
        print "Then your taxable amount will be calculated based on 10% of 300000"
        total_tax_amount+=30000
        taxable_amount-=300000
    else:
        print "\tIs your taxable amount<300000?\n\t\t True!"
        total_tax_amount=taxable_amount*.10
        return total_tax_amount

    if taxable_amount>400000:
        print "\n\t After deducting 300000 Is the second slab of your taxable amount>400000?\n True!"
        print "Then your taxable amount will be calculated based on 15% of 400000"
        total_tax_amount+=60000
        taxable_amount-=400000
    else:
        print "\n\tAfter deducting 300000 is your taxable amount<400000?\n True!"
        print "Then your taxable amount will be calculated based on 15% of deducted amount:"
        total_tax_amount+=taxable_amount*.15
        return total_tax_amount

    if taxable_amount>300000:
        print "\n\tIs the third slab of your taxable amount> another 300000?\n True!"
        print "Then your taxable amount will be calculated based on 10% of 300000:"
        total_tax_amount+=600000
        taxable_amount-=300000
    else:
        print "\n\tAfter deducting 700000 is your taxable amount<another 300000?\n True"
        print "Then your taxable amount will be calculated based on 20% of the rest of the taxable amount."
        total_tax_amount+=taxable_amount*.20
        return total_tax_amount

    print" \n\tYour final slab will be calculated on 25% of the rest of the taxable amount:"
    total_tax_amount+=taxable_amount*.25
    return total_tax_amount


print "Here is your tax calculation sheet"
print(30*".")
print("\n")
print("What's Your Gender?")
print("1: Female")
print("Or")
print("2: Male")
print("\n")
choice=raw_input("Select your gender:")

taxable_amount=0
exempted_amount=0
yearly_gross_salary=0
total_tax_amount=0

# I have kept this outside of choice because this raw input will be used for both genders
yearly_gross_salary=int(raw_input("Enter your yearly salary:\n"))

if choice== "1":

     print(" Here tax calculation for a female starts:\n")
     exempted_amount=250000
     taxable_amount= taxable_amount_after_exemtion(yearly_gross_salary,exempted_amount)

print"\tYour yearly gross salary is: %d\n"%(yearly_gross_salary)
print"\tYour exempted amount is: %d\n"%(exempted_amount)
print"\tYour allowable expense is:%d\n"%(allowable_expense)
print"You can get your total taxable amount by:\n(yearly gross salary:%d \n - exempted amount:%d \n - alllowable expense %d)"\
     %(yearly_gross_salary,exempted_amount,allowable_expense)
print(40*".")
print"So your total taxable amount is:%d"%(taxable_amount)
print"\n"
total_tax_amount=calculate_tax_on_taxable_amount(taxable_amount)
print"\n"
print(40*".")
print"And your total tax amount is:%d"%(total_tax_amount)



if choice== "2":

     print(" Here tax calculation for a female starts:\n")
     exempted_amount=240000
     taxable_amount= taxable_amount_after_exemtion(yearly_gross_salary,exempted_amount)

print"\tYour yearly gross salary is: %d\n"%(yearly_gross_salary)
print"\tYour exempted amount is: %d\n"%(exempted_amount)
print"\tYour allowable expense is:%d\n"%(allowable_expense)
print"You can get your total taxable amount by:\n(yearly gross salary:%d \n - exempted amount:%d \n - alllowable expense %d)"\
     %(yearly_gross_salary,exempted_amount,allowable_expense)
print(40*".")
print"So your total taxable amount is:%d"%(taxable_amount)
print"\n"
total_tax_amount=calculate_tax_on_taxable_amount(taxable_amount)
print"\n"
print(40*".")
print"And your total tax amount is:%d"%(total_tax_amount)
