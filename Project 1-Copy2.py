#!/usr/bin/env python
# coding: utf-8

# # Project 1
# ## Budget Manager
# ### Juan Ballas, John Cason, Zoe Mecklenburg

# - To design the project, you will need to use the Functions, Loops, Conditions, Formatted Strings, and List/Dictionary. (Which modules will you be going to use, like list, for loop, while loop, if else statements, etc.) and how?

# - Step 3: Present the project, like what the project is about and how you all of the Python modules to design the project in class (11/13/2023). 
# - Step 4: Submit the project report by 11/15/2023 by 10 am
# 

# ### 5.	Budget Manager: Create an app for managing personal finances. Users can log expenses, set budgets, and view expense analytics. Integrate data visualization to help users understand their spending habits.

#  Helpful Link
#  https://codereview.stackexchange.com/questions/173486/simple-budget-program

# In[53]:


#Helpfull code
print("Insert \na \nnew \nline \ncharacter \nin \na \nstring")

#check power point with fonts and stuff


# Left to do:
# 
# budget income and actual Income: other
# 
# budget expense and actual expense:
# 1.  Housing
# 2. Utilities
# 3. Education
# 4. Food and Dinning
# 5. Auto and Transportation
# 6. Entretainment
# 7. Health and Fitness
# 8. Investments
# 9. Other
# 
# variance cell:
# - if function for positive balance and negative balance
#     if positive ----towarsd savings.
#     if negative --- recall expenses and "reduce expenses."
#     
# Power point showing what I am using. 

# In[ ]:


# Budget
budget_salary_income_list=[]
budget_bonus_income_list=[]
budget_utilities_expense_list=[]
budget_rent_expense_list=[]

while True:
    print('Select Expected Budget section: ')
    print('1: Income')
    print('2: Expense')
    print(other)
    print('3: I am done creating my budget.')
    choice=int(input('Enter your choice (1-3): '))
    
    if choice==1:
        while True:
            print('Select an income type:')
            print('1: Salary')
            print('2: Bonus')
            income=int(input('Enter income type here: '))
            
            if income==1:
                salary_income=int(input('Enter Salary amount expected: '))
                salary_income_list.append(salary_income)
                break
            elif income==2:
                bonus_income=int(input('Enter Bonus expected: '))
                bonus_income_list.append(bonus_income)
                break
            else:
                print('You chose a wrong option. Try again.')
    elif choice==2:
        while True:
            print('Select an expense type: ')
            print('1: Utilities')
            print('2: Rent')
            expense=int(input('Enter your expense type here: '))
            
            if expense==1:
                utilities_expense=int(input('Enter Utilities cost expected:'))
                utilities_expense_list.append(utilities_expense)
                break
            elif expense==2:
                rent_expense=int(input('Enter Rent cost expected:'))
                rent_expense_list.append(rent_expense)
                break
            else:
                print('You chose a wrong option. Try again.')
    elif choice==3:
        print('Thanks!')
        
        break
    else:
        print('You chose a wrong option. Try again.')


print(f'Total Salary Income expected: ${sum(budget_salary_income_list)}')
print(f'Total Bonus Income expected: ${sum(budget_bonus_income_list)}')

budget_total_income=[]
budget_total_income.append(sum(budget_salary_income_list))
budget_total_income.append(sum(budget_bonus_income_list))
print(f'Total Income expected: ${sum(budget_total_income)}')


print(f'Total Utilities Expense expected: {sum(budget_utilities_expense_list)}')
print(f'Total Rent Expense expected: {sum(budget_rent_expense_list)}')

budget_total_expense=[]
budget_total_expense.append(sum(budget_utilities_expense_list))
budget_total_expense.append(sum(budget_rent_expense_list))
print(f'Total Expense expect: ${sum(budget_total_expense)}')

budget_net_value=[]
for i in range(len(budget_total_income)):
    budget_net_value.append(budget_total_income[i]-budget_total_expense[i])
print(f'Expected Budget Net Value: ${sum(budget_net_value)}')


# In[39]:


# Actual
# add more options to income and expense
salary_income_list=[]
bonus_income_list=[]
utilities_expense_list=[]
rent_expense_list=[]

while True:
    print('Select a transaction type: ')
    print('1: Income')
    print('2: Expense')
    print('3: No more transactions.')
    choice=int(input('Enter your choice (1-3): '))
    
    if choice==1:
        while True:
            print('Select an income type:')
            print('1: Salary')
            print('2: Bonus')
            income=int(input('Enter income type here: '))
            
            if income==1:
                salary_income=int(input('Enter Salary amount: '))
                salary_income_list.append(salary_income)
                break
            elif income==2:
                bonus_income=int(input('Enter Bonus here: '))
                bonus_income_list.append(bonus_income)
                break
            else:
                print('Pick another')
    elif choice==2:
        while True:
            print('Select an expense type: ')
            print('1: Utilities')
            print('2: Rent')
            expense=int(input('Enter your expense type here: '))
            
            if expense==1:
                utilities_expense=int(input('Enter Utilities here:'))
                utilities_expense_list.append(utilities_expense)
                break
            elif expense==2:
                rent_expense=int(input('Enter Rent here:'))
                rent_expense_list.append(rent_expense)
                break
            else:
                print('Pick another')
    elif choice==3:
        print('Thanks!')
        
        break
    else:
        print('Pick another')


print(f'Total Salary Income: ${sum(salary_income_list)}')
print(f'Total Bonus Income: ${sum(bonus_income_list)}')

total_income=[]
total_income.append(sum(salary_income_list))
total_income.append(sum(bonus_income_list))
print(f'Total Income: ${sum(total_income)}')


print(f'Total Utilities Expense: {sum(utilities_expense_list)}')
print(f'Total Rent Expense: {sum(rent_expense_list)}')

total_expense=[]
total_expense.append(sum(utilities_expense_list))
total_expense.append(sum(rent_expense_list))
print(f'Total Expense: ${sum(total_expense)}')

net_value=[]
for i in range(len(total_income)):
    net_value.append(total_income[i]-total_expense[i])
print(f'Net Value: ${sum(net_value)}')


# In[51]:


#Variance

print(f'Total Income expected: ${sum(budget_total_income)}')
print(f'Total Income: ${sum(total_income)}')
print(f'Income Variance: ${sum(budget_total_income)-sum(total_income)}.')

#if positive,else you rdid good or bad



print(f'Total Expense expect: ${sum(budget_total_expense)}')
print(f'Total Expense: ${sum(total_expense)}')
print(f'Income Variance: ${sum(budget_total_expense)-sum(total_expense)}.')

#if positive,else you rdid good or bad



print(f'Expected Budget Net Value: ${sum(budget_net_value)}')
print(f'Net Value: ${sum(net_value)}')
print(f'Net Value Variance: ${sum(budget_net_value)-sum(net_value)}.')

#if positive: savings.. if negative.. birng back expenses and point place them in order.


# do a cell for total revenue per categorie and total
# 
# example but maybe not correct way:
# number1= int(input("Enter a integer :"))
# number2= float(input("Enter a floating point number: "))
# print(f"The first number is {number1}. The second number is {number2}.")
# print(f"Multiplication equals: {number1*number2}")
# 
# 
# h=[2,3,4,5,6]
# len(h) =5
# 
# total= float(input("Enter the amount you spent: "))
# tax=.06*total
# print(f"The subtotal is: {total+tax}")

# In[ ]:




