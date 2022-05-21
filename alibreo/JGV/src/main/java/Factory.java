import java.time.Duration;

public class Factory {
    public Movie createAvatarMoview() {
        Movie avatar = new Movie("아바타",
                Duration.ofMinutes(120),
                Money.wons(1000), new AmountDefaultDiscountPolicy(Money.ZERO));

        return avatar;
    }
}
