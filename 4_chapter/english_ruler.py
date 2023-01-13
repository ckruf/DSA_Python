draw_line_calls = 0
draw_interval_calls = 0


def draw_ruler(major_length: int, inches: int) -> None:
    """
    Given the length of the major tick, and a number of inches, draw an English ruler recursively.

    For each inch of the ruler, we have a central tick of length L. Before and after the central tick, 
    we have identical intervals with a central tick of length L - 1. We can therefore draw inches
    iteratively, and the part between the inches recursively.

    :param major_length: The number of ticks that a whole inch marking has. This determines the accuracy of the ruler. For example,
    if the major length is 2, the ruler will only have one marking between whole inches - 1/2 inch accuracy. If it's 3, 1/4 inch accuracy, etc.

    :param inches: how many inches the ruler has in total
    """
    if major_length < 1:
        raise ValueError("Length of major tick must be at least 1")
    if inches < 1:
        raise ValueError("Number of inches must be at least 1")

    draw_line(major_length, 0)

    for i in range(1, inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, i)


    
def draw_line(ticks: int, label: int | None = None) -> None:
    """Draw a single line on the ruler"""
    global draw_line_calls
    draw_line_calls += 1
    line = "-" * ticks
    if label is not None:
        line += f" {label}"
    print(line)


def draw_interval(central_tick_length: int) -> None:
    """Given a central tick length, draw an interval on the ruler"""
    print(f"draw_interval({central_tick_length})")
    global draw_interval_calls
    draw_interval_calls += 1
    if central_tick_length > 0:
        draw_interval(central_tick_length - 1)
        draw_line(central_tick_length)
        draw_interval(central_tick_length - 1)

if __name__ == "__main__":
    draw_ruler(4, 1)
    print(f"calls to draw_line(): {draw_line_calls}")
    print(f"calls to draw_interval(): {draw_interval_calls}")