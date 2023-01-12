import random


thirty_days = { 4, 6, 9, 11 }


def share_birthday(n: int) -> bool:
    """
    Run an experiment simulating whether, in a room of n people, two people share a birthday.
    Birthdays are randomly generated. Returns True if there are two people who share a birthday, False otherwise.

    :param n: number of people in the room
    """
    birthdays = dict()
    for _ in range(n):
        birth_month = random.randint(0, 12)
        if birth_month in thirty_days:
            last_day = 30
        elif birth_month == 2:
            last_day = 28
        else:
            last_day = 31
        birth_day = random.randint(1, last_day)
        birthday = (birth_day, birth_month)
        birthdays[birthday] = birthdays.get(birthday, 0) + 1
    
    for key, value in birthdays.items():
        if value > 1:
            return True

    return False


def share_birthday_experiments(trials: int, people_counts: list[int] = [5, 10, 15, 20, 23, 25, 30, 35, 40, 45, 50]) -> dict [int, float]:
    """
    Run experiments on the birthday paradox. Find the probabilities that two people share a birthday in 
    a room of 5, 10, 15... people. Does experiments the given number of times using randomly generated birthdays

    :param trials: number of repeats to do at each 'room size'
    :param people_counts: room sizes to test out
    """
    results = dict()
    for room_size in people_counts:
        success_count = 0
        for _ in range(trials):
            success_count += int(share_birthday(room_size))
        results[room_size] = success_count / trials
    
    return results


if __name__ == "__main__":
    print(share_birthday_experiments(1000))