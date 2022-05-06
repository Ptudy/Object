#-*- encoding: utf-8 -*-

from time import time


basePay = 300
names = ["직원A", "직원B", "직원C", "직원D", "직원E", "직원F"]
basePays = [400, 300, 250, 1, 1, 1.5]
hourlys = [False, False, False, True, True, True]
timeCards = [0, 0, 0, 120, 120, 120]

class Employee:
    def __init__(self, name, basePay):
        self.name = name
        self.basePay = basePay

class SalariedEmployee(Employee):
    def calculatePay(self, taxRate):
        return self.basePay - self.basePay * taxRate
    
    def monthlyBasePay(self):
        return basePay
    
class HourlyEmployee(Employee):
    def __init__(self, name, basePay, timeCard):
        Employee.__init__(self, name, basePay)
        self.timeCard = timeCard

    def calculatePay(taxRate):
        return basePay * timeCard - basePay * timeCard * taxRate
    
    def monthlyBasePay(self):
        return 0

employees = [SalariedEmployee("직원A", 400), HourlyEmployee("알바A", 1, 120)]
