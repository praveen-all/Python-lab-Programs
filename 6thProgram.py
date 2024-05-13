# 6. Develop a program that takes as input an hourly wage and the number of hours an employee worked in the last week. The program should compute and return the employee’s pay. Overtime work is calculated as: any hours beyond 40 but less than or equal 60 should be paid at 1.5 times the regular hourly wage. Any hours beyond 60 should be paid at 2 times the regular hourly wage.

def calculate(time,wage):
    if time>=40 and time<=60:
        return 1.5*time*wage
    elif time>60:
        return 2*time*wage
    else:
        return time*wage
    
time=int(input("Enter the number of hour employee worked last week\n"))
wage=float(input("enter the wage for each hour\n"))

print("last week pay is:",calculate(time,wage))