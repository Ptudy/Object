import java.time.Duration;

public class Client {
    private Factory factory;

    public Client(Factory factory) {
        this.factory = factory;
    }

    public Money getAvatarFee() {
        Movie avatar = factory.createAvatarMoview();
        TestA testA = new TestA();
        testA.a = 3;
        return avatar.getFee();
    }
}


class TestA {
    public int a;
}