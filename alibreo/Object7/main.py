#-*- encoding: utf-8 -*-

employees = ["직원A", "직원B", "직원C"]
basePays = [400, 300, 250]

def getTaxRate():
    print("세율을 입력하세요: ")
    return float(input())

def calculatePayFor(name, taxRate):
    index = employees.index(name)
    basePay = basePays[index]
    return basePay - (basePay * taxRate)

def describeResult(name, pay):
    return "이름: " + name + "급여: " + str(pay)

def main(name):
    taxRate = getTaxRate()
    pay = calculatePayFor(name, taxRate)
    print(describeResult(name, pay))

main("직원C")

