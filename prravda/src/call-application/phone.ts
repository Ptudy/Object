import { Call } from "./call";
import { Money } from "./money";

export class Phone {
  private readonly callList: Call[] = [];

  constructor(
    private readonly amount: Money,
    private readonly seconds: number
  ) {}

  public call(call: Call): void {
    this.callList.push(call);
  }

  public getCalls(): Call[] {
    return this.callList;
  }

  public getAmount() {
    return this.amount;
  }

  public getSeconds() {
    return this.seconds;
  }

  public calculateFee(): Money {
    let result = Money.ZERO;
    for (const eachCall of this.callList) {
      result = result.plus(
        this.amount.times(eachCall.getDurationInSeconds() / this.seconds)
      );
    }
    return result;
  }
}
