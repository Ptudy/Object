package chap04;

public class Reservation {
    private Customer coustmoer;
    private Screening screening;
    private Money fee;
    private int audienceCount;

    public Reservation(Customer coustmoer, Screening screening, Money fee, int audienceCount) {
        this.coustmoer = coustmoer;
        this.screening = screening;
        this.fee = fee;
        this.audienceCount = audienceCount;
    }

    public Customer getCoustmoer() {
        return coustmoer;
    }

    public void setCoustmoer(Customer coustmoer) {
        this.coustmoer = coustmoer;
    }

    public Screening getScreening() {
        return screening;
    }

    public void setScreening(Screening screening) {
        this.screening = screening;
    }

    public Money getFee() {
        return fee;
    }

    public void setFee(Money fee) {
        this.fee = fee;
    }

    public int getAudienceCount() {
        return audienceCount;
    }

    public void setAudienceCount(int audienceCount) {
        this.audienceCount = audienceCount;
    }
}
