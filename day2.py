


strat_guide = []
with open("day2.txt", "r") as f:
    for line in f:
        round_data = line.strip().split(" ")
        strat_guide.append(round_data)


def part2():
    total = 0
    outcome_dict = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }

    score_dict = {
        "AX": 3,    # Rock, Lose  --  0 + 3
        "AY": 4,    # Rock, Draw  --  3 + 1
        "AZ": 8,    # Rock, Win  --   6 + 2
        "BX": 1,    # Paper, Lose  -- 0 + 1
        "BY": 5,    # Paper, Draw  -- 3 + 2
        "BZ": 9,    # Paper, Win  --  6 + 3
        "CX": 2,    # Scissors, Lose  -- 0 + 2
        "CY": 6,    # Scissors, Draw  -- 3 + 3
        "CZ": 7     # Scissors, Win  --  6 + 1
    }


    for round_ in strat_guide:
        round_score = score_dict[str(round_[0])+str(round_[1])]
        total += round_score
    print(total)




def part1():
    total = 0


    score_dict = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    outcome_dict = {
        "AX": 3,
        "AY": 6,
        "AZ": 0,
        "BX": 0,
        "BY": 3,
        "BZ": 6,
        "CX": 6,
        "CY": 0,
        "CZ": 3
    }


    for round_ in strat_guide:
        round_score = score_dict[round_[1]]
        outcome_score = outcome_dict[str(round_[0])+str(round_[1])]
        round_score += outcome_score
        print(f"{score_dict[round_[1]]} + {outcome_score} = {round_score} ")
        total += round_score

    print(total)

# part1()
part2()
    
    











