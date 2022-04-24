import java.time.Duration;
import java.util.List;

public class NoneDiscoutMovie extends Movie {
    public NoneDiscoutMovie(String title, Duration runningTIme, Money fee, List<DiscountCondition> discountConditionList) {
        super(title, runningTIme, fee, discountConditionList);
    }

    @Override
    protected Money calculateDiscountAmount() {
        return Money.ZERO;
    }
}
