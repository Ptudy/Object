#-*- encoding: utf-8 -*-

basePay = 300
employees = ["직원A", "직원B", "직원C", "직원D", "직원E", "직원F"]
basePays = [400, 300, 250, 1, 1, 1.5]
hourlys = [False, False, False, True, True, True]
timeCards = [0, 0, 0, 120, 120, 120]

def getTaxRate():
    print("세율을 입력하세요: ")
    return float(input())

def calculatePay(name, taxRate):
    if isHourly(name):
        pay = calculateHourlyPayFor(name, taxRate)
    else:
        pay = calculatePayFor(name, taxRate)
    return pay

def isHourly(name):
    return hourlys[employees.index(name)]

def calculateHourlyPayFor(name, taxRate):
    index = employees.index(name)
    basePay = basePays[index] * timeCards[index]
    return basePay - (basePay * taxRate)

def calculatePayFor(name, taxRate):
    return basePay - (basePay * taxRate)

def describeResult(name, pay):
    return "이름: " + name + "급여: " + str(pay)

def sumOfBasePays():
    result = 0
    for name in employees:
        if (not isHourly(name)):
            result += basePays[employees.index(name)]

    return result

def calculatePay(name):
    taxRate = getTaxRate()
    pay = calculatePayFor(name, taxRate)
    print(describeResult(name, pay))
