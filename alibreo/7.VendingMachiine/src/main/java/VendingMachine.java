public class VendingMachine {
    private Money money = new Money(0);

    public Item purchase(String itemName) {
        Item item = Item.createItem(itemName);
        if (item != null && item.isAvailableWith(money)) {
            money = money.minus(item.getPrice());
            return item;
        }
        return null;
    }

    public void receiveMoney(Money inputMoney) {
        money = money.add(inputMoney);
    }

    public Money getRemainMoney() {
        return money;
    }

    public void receiveCard(Card card) {
        money = card.getMoney();
    }

    public Item settle(Payment payment) {
        return Item.createWater();
    }

    public Payment prepare(String water) {
        return new Payment();
    }
}
