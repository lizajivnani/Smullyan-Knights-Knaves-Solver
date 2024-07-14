from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# puzzle 0
knowledge0 = And(Biconditional(Not(AKnight), AKnave),
                 Biconditional(Not(And(AKnight, AKnave)), AKnave)
                 )


# puzzle 1
knowledge1 = And(Biconditional(Not(AKnight), AKnave),
                 Biconditional(Not(BKnight), BKnave),
                 Biconditional(Not(And(BKnave, AKnave)), AKnave)

                 )


# puzzle 2
knowledge2 = And(Biconditional(Not(AKnight), AKnave),
                 Biconditional(Not(BKnight), BKnave),
                 Biconditional(Not(Or(And(AKnight, BKnight), And(AKnave, BKnave))), AKnave),
                 Biconditional(Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))), BKnave)
)

# puzzle 3
knowledge3 = And(Biconditional(Not(AKnight), AKnave),
                 Biconditional(Not(CKnight), CKnave),
                 Biconditional(Not(BKnight), BKnave),

                 Biconditional(Not(Or(AKnight, AKnave)), AKnave),
                 Biconditional(Not(AKnave), BKnave),
                 Biconditional(Not(CKnave), BKnave),
                 Biconditional(AKnight, CKnight)
                 )

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
