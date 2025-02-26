class Day2:
    def solve(self, a , b) -> int:
        print(a)
        print(b)
        sum = 0
        store = {}
        for elem in b:
            store[elem] = store.get(elem, 0) + 1
        for elem in a:
            if elem in store:
                sum += store[elem] * elem
        return sum