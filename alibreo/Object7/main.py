#-*- encoding: utf-8 -*-

import Employees

def getTaxRate():
    print("세율을 입력하세요: ")
    return float(input())

def describeResult(name, pay):
    return "이름: " + name + "급여: " + str(pay)

def sumOfBasePays():
    result = 0
    for employee in Employees.employees:
        result += employee.monthlyBasePay()
    print(result)

def calculatePay(name):
    taxRate = getTaxRate()
    for employee in Employees.employees:
        if employee.name == name:       
            pay = employee.calculatePay(taxRate) 
            print(describeResult(name, pay))

def main(operation, args = {}):
    if operation == "pay":
        calculatePay(args["name"])
    elif operation == "basePays":
        sumOfBasePays()

main("pay", {"name": "직원A"})
# main("pay")
