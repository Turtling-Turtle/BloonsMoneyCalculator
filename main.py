# print("Welcome to BloonsMoneyPerRound")
class Round:
    def __init__(self, round_number: int, cash: int):
        self.round_number = round_number
        self.money_in_round = cash


file = open("rounds.txt")

rounds = []
for line in file:
    aspects = line.split()
    rounds.append(Round(int(aspects[0]), int(aspects[1])))

while True:
    start_round = int(input("Enter Start Round: "))
    end_round = int(input("Enter End Round: "))
    cash_total = 0
    if end_round - 1 == start_round:
        print(f"You will make a total of ${rounds[start_round].money_in_round:,} on round {end_round}")
        continue

    for round_num in range(start_round - 1, end_round):
        current_round = rounds[round_num]
        cash_total = cash_total + current_round.money_in_round
    print(f"You will make a total of ${cash_total:,} between round(s) {start_round} - {end_round}")
