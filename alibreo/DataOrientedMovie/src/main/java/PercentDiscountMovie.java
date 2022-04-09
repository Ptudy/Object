import java.time.Duration;
import java.util.List;

public class PercentDiscountMovie extends Movie {
    private Double discountPercent;

    public PercentDiscountMovie(String title, Duration runningTIme, Money fee, List<DiscountCondition> discountConditionList, Double discountPercent) {
        super(title, runningTIme, fee, discountConditionList);
        this.discountPercent = discountPercent;
    }

    @Override
    protected Money calculateDiscountAmount() {
        return getFee().times(discountPercent);
    }
}