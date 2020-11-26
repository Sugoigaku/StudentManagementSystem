class Template(object):

    def __init__(self, header):
        self.header = header
        self.length = len(header)
        self.rows = []

    def add_row(self, row):
        if len(row) != self.length:
            raise ValueError
        self.rows.append(row)

    def print_table(self):
        temp = [r for r in self.rows]
        temp.append(self.header)
        max_len = [0] * self.length
        for t in temp:
            for i in range(self.length):
                if max_len[i] < len(t[i]):
                    max_len[i] = len(t[i])
        h_bar = '+' + '―' * (sum(max_len) + 2 * self.length + self.length-2) + '+'
        head, tail = '|　', '　'
        print(h_bar)
        for i in range(self.length):
            print("{0}{1:{2}<{3}}{4}".format(head, self.header[i], '　', max_len[i], tail), end="")
        print('|')
        print(h_bar)
        for r in self.rows:
            for i in range(self.length):
                print("{0}{1:{2}<{3}}{4}".format(head, r[i], '　', max_len[i], tail), end="")
            print('|')
        print(h_bar)
