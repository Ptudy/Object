import java.time.Duration;
import java.util.List;

public class AmoundDiscountMovie extends Movie {
    private Money discountAmount;

    public AmoundDiscountMovie(String title, Duration runningTIme, Money fee, List<DiscountCondition> discountConditionList, Money discountAmount) {
        super(title, runningTIme, fee, discountConditionList);
        this.discountAmount = discountAmount;
    }

    @Override
    protected Money calculateDiscountAmount() {
        return discountAmount;
    }
}
