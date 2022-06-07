//
//  Hapsung.swift
//  PolicyTest
//
//  Created by 윤상진 on 2022/06/05.
//

import XCTest

fileprivate class Phone {
    let ratePolicy: RatePolicy
    let calls = [Call]()
    
    init(ratePolicy: RatePolicy) {
        self.ratePolicy = ratePolicy
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

fileprivate class NightlyDiscountPolicy: BasicRatePolicy {
    init(nightlyAmount: Money, regularAmount: Money, seconds: TimeInterval) {
        self.nightlyAmount = nightlyAmount
        self.regularAmount = regularAmount
        self.seconds = seconds
    }
    
    func calculateCallFee(_ call: Call) -> Money {
        // 실제 구현
        return Money.Zero
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

fileprivate class TaxablePolicy: AdditionalRatePolicy {
    var next: RatePolicy
    
    init(next: RatePolicy) {
        self.next = next
    }
    
    func afterCalculated(_ fee: Money) -> Money {
        // fee에다가 세금처리
        let tax = 1000000000000
        return fee.plus(Money(count: tax))
    }
}

class Hapsung: XCTestCase {

}
