import lombok.Getter;
import lombok.Setter;

import java.time.Duration;
import java.time.LocalDateTime;
import java.util.List;

@Setter
@Getter
public abstract class Movie {
    private String title;
    private Duration runningTIme;
    private Money fee;
    private List<DiscountCondition> discountConditionList;

    public Movie(String title, Duration runningTIme, Money fee, List<DiscountCondition> discountConditionList) {
        this.title = title;
        this.runningTIme = runningTIme;
        this.fee = fee;
        this.discountConditionList = discountConditionList;
    }

    public boolean isDiscountable(Screening screening) {
        return discountConditionList.stream().anyMatch(condition -> condition.isSatisfiedBy(screening));
    }

    public Money calculateFee(Screening screening) {
        if (isDiscountable(screening)) {
            return fee.minus(calculateDiscountAmount());
        }
        return fee;
    }

    abstract protected Money calculateDiscountAmount();
}
