# change making machine
# function to take customers payment in cash
def customer_payout(cash):
    cash_100cents = cash * 100
    return cash_100cents


def purchase_cost():
    purchase = float(input("Enter the Purchase cost: "))
    purchase_100cents = purchase * 100
    return purchase_100cents


def customers_change():
    buying_cost = purchase_cost()
    cash = customer_payout(cash=0)
    customers_return = cash - buying_cost
    return customers_return


def change_denomination():
    cash = customers_change()
    cash = cash / 100
    one_denomination = 0
    while cash > 1:
        cash = cash - 1
        one_denomination = one_denomination + 1
    return one_denomination, cash


def currency_output():
    notes, coins = change_denomination()
    one_hundred = 0
    fifty_note = 0
    twenty_note = 0
    ten_note = 0
    five_note = 0
    one_note = 0
    coins_q = 0

    if notes > 100:
        notes = notes - 100
        one_hundred = one_hundred + 1
    elif notes > 50:
        notes = notes - 50
        fifty_note = fifty_note + 1
    elif notes > 20:
        notes = notes - 20
        twenty_note = twenty_note + 1
    elif notes > 10:
        notes = notes - 10
        ten_note = ten_note + 1
    elif notes > 5:
        notes = notes - 5
        five_note = five_note + 1
    elif notes > 1:
        notes = notes - 1
        one_note = one_note + 1
    elif 0 < notes < 1:
        coins = coins - 25
        coins_q = coins_q + 1

        print(one_hundred, fifty_note, twenty_note, ten_note, five_note, one_note, coins_q)


customer_payout(45)
purchase_cost()
customers_change()
change_denomination()
currency_output()
