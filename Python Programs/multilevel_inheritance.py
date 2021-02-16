class Dad:
    basketball_won = 10


class Son(Dad):
    cricket_won = 4
    basketball_won = 6

    def play_cricket(self):
        return f'Yes I can play cricket and I won {self.cricket_won} times ' \
               f'and I won basket ball {self.basketball_won} times'


class GrandSon(Son):
    cricket_won = 12

    def play_cricket(self):
        return f'Grand Child here! I can play cricket very well and I won {self.cricket_won} times'


daddy = Dad()
son = Son()
child = GrandSon()

print(child.play_cricket())
print(child.basketball_won)