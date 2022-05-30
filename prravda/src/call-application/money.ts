export class Money {
  public static ZERO = Money.wons(0);
  private readonly amount: number;

  constructor(amount: number) {
    this.amount = amount;
  }

  public static wons(amount: number) {
    return new Money(amount);
  }

  public plus(amount: Money) {
    return new Money(this.amount + amount.amount);
  }

  public minus(amount: Money) {
    return new Money(this.amount - amount.amount);
  }

  public times(percent: number) {
    return new Money(this.amount * percent);
  }

  public isLessThan(other: Money) {
    return this.amount < other.amount;
  }

  public isGreaterThanOrEqual(other: Money) {
    return this.amount >= other.amount;
  }
}
