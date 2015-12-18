class Bill:

    def __init__(self, amount):
        self._amount = amount

    def __str__(self):
        return 'A {}$ bill'.format(self._amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self._amount

    def __hash__(self):
        return self._amount

    def __eq__(self, other):
        return self._amount == other.total()

    def total(self):
        return int(self._amount)

    def to_list(self):
        return [self._amount]


class BatchBill:

    def __init__(self, bill):
        self._bill = bill

    def __len__(self):
        return len(self._bill)

    def __int__(self):
        return sum([bill.total() for bill in self._bill])

    def __getitem__(self, index):
        return self._bill[index]

    def total(self):
        return int(self)

    def to_list(self):
        list = [item.total() for item in self._bill]

        return list


class CashDesk:

    def __init__(self):
        self.all_money = []

    def take_money(self, money):
        self.all_money.append(money)

    def total(self):
        return sum([obj.total() for obj in self.all_money])

    def inspect(self):
        result = {}

        for obj in self.all_money:
            for item in obj.to_list():
                if item in result:
                    result[item] += 1
                else:
                    result[item] = 1

        return result
