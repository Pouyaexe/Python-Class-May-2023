def make_pizza(
    size: int = 16,
    toppings_list: list = [],
):
    """Summarize the pizza we are about to make."""

    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings_list:
        print(f"- {topping}")


def print_have_a_nice_day():
    print("Have a nice day!")
