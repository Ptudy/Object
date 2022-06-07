//
//  PolicyTest.swift
//  PolicyTest
//
//  Created by 윤상진 on 2022/06/04.
//

import XCTest

struct Call {
    let from = Date()
    let duration: TimeInterval = 0
}

struct Money: Equatable {
    static let Zero = Money(count: 0)
    let count: Int
    
    func plus(_ rhs: Money) -> Money {
        return Money(count: self.count + rhs.count)
    }
}

fileprivate class Phone {
    let ratePolicy: RatePolicy
    var calls = [Call]()
    
    init(ratePolicy: RatePolicy) {
        self.ratePolicy = ratePolicy
    }
    
    func calculateFee() -> Money {
        ratePolicy.calculateFee(phone: self)
    }
}

fileprivate protocol RatePolicy {
    func calculateFee(phone: Phone) -> Money
}

fileprivate protocol BasicRatePolicy: RatePolicy {
    func calculateCallFee(_ call: Call) -> Money
}

fileprivate extension BasicRatePolicy {
    func calculateFee(phone: Phone) -> Money {
        var result = Money.Zero

        for call in phone.calls {
            result = result.plus(calculateCallFee(call))
        }

        return result
    }
}


fileprivate extension BasicRatePolicy where Self: NightlyDiscountPolicy {
    func calculateFee(phone: Phone) -> Money {
        return Money.Zero
    }
}

fileprivate class NightlyDiscountPolicy: BasicRatePolicy {
    init(nightlyAmount: Money, regularAmount: Money, seconds: TimeInterval) {
        self.nightlyAmount = nightlyAmount
        self.regularAmount = regularAmount
        self.seconds = seconds
    }
    
    func calculateCallFee(_ call: Call) -> Money {
        // 실제 구현
        return Money.init(count: 1)
    }
    
    static let LATE_NIGHT_HOUR = 22
    
    let nightlyAmount: Money
    let regularAmount: Money
    let seconds: TimeInterval
}

fileprivate protocol AdditionalRatePolicy: RatePolicy {
    var next: RatePolicy { get }
    func afterCalculated(_: Money) -> Money
}

fileprivate extension AdditionalRatePolicy {
    func calculateFee(phone: Phone) -> Money {
        let fee = next.calculateFee(phone: phone)
        return afterCalculated(fee)
    }
}

fileprivate protocol TaxablePolicy: BasicRatePolicy {
    var tax: Money { get }
}

fileprivate extension TaxablePolicy where Self: NightlyDiscountPolicy {
    func calculateFee(phone: Phone) -> Money {
        
        let fee = (self as BasicRatePolicy).calculateFee(phone: phone)
        return fee.plus(fee.plus(tax))
    }
}

fileprivate class TaxableRateDiscountablePolicy: NightlyDiscountPolicy, TaxablePolicy {
    internal init(tax: Money) {
        self.tax = tax
        super.init(nightlyAmount: Money(count: 10), regularAmount: Money(count: 10), seconds: .infinity)
    }
    
    var tax: Money
    
    
}

class Mixin: XCTestCase {
    func testMixins() {
        let taxPolicy = TaxableRateDiscountablePolicy(tax: Money(count: 100))
        var phone = Phone(ratePolicy: taxPolicy)
        phone.calls = [Call()]
        XCTAssertEqual(phone.calculateFee(), Money(count: 2))
        
    }
}
