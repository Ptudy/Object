#-*- encoding: utf-8 -*-

import Employees

employees = ["직원A", "직원B", "직원C"]
basePays = [400, 300, 250]

def getTaxRate():
    print("세율을 입력하세요: ")
    return float(input())

def describeResult(name, pay):
    return "이름: " + name + "급여: " + str(pay)

def sumOfBasePays():
    result = 0
    for basePay in basePays:
        result += basePay
    print(result)

def calculatePay(name):
    taxRate = getTaxRate()
    pay = Employees.calculatePayFor(name, taxRate)
    print(describeResult(name, pay))

def main(operation, args = {}):
    if operation == "pay":
        calculatePay(args["name"])
    elif operation == "basePays":
        sumOfBasePays()

main("pay", {"name": "직원C"})
# main("pay")
