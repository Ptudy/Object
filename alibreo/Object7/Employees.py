#-*- encoding: utf-8 -*-

from time import time


basePay = 300
names = ["직원A", "직원B", "직원C", "직원D", "직원E", "직원F"]
basePays = [400, 300, 250, 1, 1, 1.5]
hourlys = [False, False, False, True, True, True]
timeCards = [0, 0, 0, 120, 120, 120]

class Employee:
    def __init__(self, name, basePay, hourly, timeCard):
        self.name = name
        self.basePay = basePay
        self.hourly = hourly
        self.timeCard = timeCard

    def calculatePay(self, taxRate):
        if self.hourly:
            pay = self.calculateHourlyPay(taxRate)
        else:
            pay = self.calculateSalariedPay(taxRate)
        return pay

    def calculateHourlyPay(self, taxRate):
        return self.basePay * self.timeCard - (self.basePay * self.timeCard) * taxRate

    def calculateSalariedPay(self, taxRate):
        return self.monthlyBasePay() - (self.monthlyBasePay() * taxRate)

    def monthlyBasePay(self):
        if self.hourly:
            return 0
        return self.basePay
        
employees = []
for name, basePay, hourly, timeCard in zip(names, basePays, hourlys, timeCards):
    employees.append(Employee(name, basePay, hourly, timeCard))