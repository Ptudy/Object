import { Phone } from "../phone";
import { Call } from "../call";
import { Money } from "../money";

describe("Test: Call application", () => {
  let call: Call;
  let phone: Phone;

  beforeEach(() => {
    call = new Call(new Date(), new Date());
    phone = new Phone(Money.wons(5), 10);
  });

  it("should be defined", () => {
    expect(call).toBeDefined();
    expect(phone).toBeDefined();
  });

  it("Return 60 KRW as a result of call in 2 minutes, which the fee is 5 KRW / 10 SEC", () => {
    phone.call(
      new Call(new Date("2022-05-30 16:32:00"), new Date("2022-05-30 16:33:00"))
    );
    phone.call(
      new Call(new Date("2022-05-30 16:33:00"), new Date("2022-05-30 16:34:00"))
    );
    console.log(phone.calculateFee());
  });
});
