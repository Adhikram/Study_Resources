class Day1:
    def solve(self, a , b) -> int:
        # print(a)
        # print(b)
        sum = 0
        a = sorted(a)
        b = sorted(b)
        for left, right in zip(a,b):
            sum += abs(left - right)
        return sum

    def solve2(self, a , b) -> int:
        # print(a)
        # print(b)
        sum = 0
        store = {}
        for elem in b:
            store[elem] = store.get(elem, 0) + 1
        for elem in a:
            if elem in store:
                sum += store[elem] * elem
        return sum