class FlatIterator:
    def __init__(self, lst):
        self._stopped = False
        self.lst = lst
        self.cursor = 0
        self.cursor_2 = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stopped:
            while self.cursor < len(self.lst):
                if self.cursor_2 < len(self.lst[self.cursor]):
                    new = self.lst[self.cursor][self.cursor_2]
                    self.cursor_2 += 1
                    return new

                self.cursor += 1
                self.cursor_2 = 0
            self._stopped = True
        raise StopIteration


def main():
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]


    for item in FlatIterator(nested_list):
      print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)


main()
