export class Call {
  constructor(private readonly from: Date, private readonly to: Date) {}

  public getDurationInSeconds(): number {
    return (this.to.valueOf() - this.from.valueOf()) / 1000;
  }

  public getFrom(): Date {
    return this.from;
  }
}
