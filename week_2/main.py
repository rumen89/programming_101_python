# main.py

from cash_desk import Bill, BatchBill, CashDesk


def main():
    # a = Bill(10)
    # b = Bill(5)
    # c = Bill(10)
    #
    # print(int(a))
    #
    # print(a)
    # print(str(a))
    #
    # print(a == b)
    # print(a == c)
    #
    # money_holder = {}
    #
    # money_holder[a] = 1
    #
    # if c in money_holder:
    #     money_holder[c] += 1
    #
    # print(money_holder)

    values = [10, 20, 50, 100, 100, 100]

    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)

    print(batch.total())

    for bill in batch:
        print(bill)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print(desk.total())

    print(Bill(5).to_list())
    print(batch.to_list())

    print(desk.inspect())

if __name__ == '__main__':
    main()
