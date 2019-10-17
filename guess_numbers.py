from typing import Tuple

Numbers = Tuple[int, int, int]

class GuessResult:
    """이 함수는 수정 하지 않는 것을 권장합니다. (약간의 기능을 추가하는 정도는 괜찮습니다)"""

    def __init__(self, count_of_correct_position: int, count_of_incorrect_position: int):
        self.count_of_correct_position = count_of_correct_position
        self.count_of_incorrect_position = count_of_incorrect_position

    def is_success(self):
        return self.count_of_correct_position == 3


class GameHost:
    def guess(self, guess_numbers: Numbers) -> GuessResult:
        raise NotImplementedError()


class GameGuest:
    def guess(self) -> Numbers:
        raise NotImplementedError()

    def feedback(self, numbers: Numbers, result: GuessResult):
        raise NotImplementedError()
