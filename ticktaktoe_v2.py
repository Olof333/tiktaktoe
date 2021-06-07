from enum import Enum
from typing import Counter, Optional


class PlayerFigure(Enum):
    x = "X"
    o = "O"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)


class Board:
    def __init__(self) -> None:
        self.grid: list[list[Optional[PlayerFigure]]] = [
            [None for _ in range(3)] for _ in range(3)
        ]

    def set_element(self, loc: tuple[int, int], elem: PlayerFigure) -> None:
        if self.grid[loc[0]][loc[1]] is not None:
            raise ValueError("Cell is already filled")
        self.grid[loc[0]][loc[1]] = elem

    def has_won(self) -> bool:
        for row in self.grid:
            if row[0] == row[1] == row[2] != None:
                return True
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != None:
                return True
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != None:
            return True
        elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != None:
            return True
        else:
            return False

    def is_draw(self) -> bool:
        for row in self.grid:
            for elem in row:
                if elem is None:
                    return False
        return True

    def draw(self) -> None:
        data = [
            "|".join(str(elem) if elem is not None else " " for elem in row)
            for row in self.grid
        ]
        print("\n-----\n".join(data))


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.current_turn = PlayerFigure.x

    def turn(self) -> None:
        player_turn = input("Where you want to place element?")
        try:
            x, y = player_turn.split(" ")
            x, y = int(x), int(y)
        except:
            print("Invalid input")
            return self.turn()

        try:
            self.board.set_element((x - 1, y - 1), self.current_turn)
        except ValueError as error:
            print(error)
            return self.turn()
        except IndexError:
            print("Invalid input")
            return self.turn()

    def start(self) -> None:
        while True:
            self.board.draw()
            self.turn()
            if self.board.has_won() or self.board.is_draw():
                break
            self.current_turn = (
                PlayerFigure.x
                if self.current_turn == PlayerFigure.o
                else PlayerFigure.o
            )
        self.board.draw()
        if self.board.is_draw():
            print("Draw")
        else:
            print(f"{self.current_turn.value} has won!")


def main() -> None:
    print("Starting a new game!")
    while True:
        game = Game()
        game.start()


if __name__ == "__main__":
    main()
