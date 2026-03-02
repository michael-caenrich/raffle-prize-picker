"""A Simple raffle with prizes and random winners."""

import random


# --- Helper functions ---
def print_banner(text: str, color: int = 92, file=None) -> None:
    """Print a centered banner, with color for console or plain text for file."""
    border = 40 * "="
    formatted = f"{border}\n{text.center(40)}\n{border}"

    if file is None:
        print(f"\033[{color}m{formatted}\033[0m")
    else:
        print(f"{formatted}", file=file)

def collect_candidates() -> list[str]:
    """Collect participant names from user input (minimum 3)."""
    candidates = []

    # Ask for number of participants (minimum 3)
    while True:
        try:
            count = int(input("\nHow many names are entering the raffle?: "))
            if count < 3:
                print("⚠️The number must be at least 3.")
                continue
            break
        except ValueError:
            print("⚠️Invalid input. Enter a number.")

    for i in range(count):
        name = input(f"Enter name #{i + 1}: ").strip().capitalize()
        candidates.append(name)

    return candidates

def collect_prizes(num_prizes: int = 3) -> list[str]:
    """Collect prize names from user input."""
    print(f"\nCollect {num_prizes} prize names")
    prizes = []

    for i in range(num_prizes):
        prize_name = input(f"Enter prize name #{i + 1}: ").strip().capitalize()
        prizes.append(prize_name)

    print()
    return prizes


def run_raffle() -> None:
    """Run the raffle and assign three prizes to random winners."""
    candidates = collect_candidates()
    prizes = collect_prizes()

    # Select 3 prize names
    winners = random.sample(candidates, 3)

    # Print the result to console and save to file
    with open("raffle_results.txt", "w", encoding="utf-8") as f:
        for stream in (None, f):
            print_banner("🎉 Raffle Results 🎉", file=stream)

        for i, (winner, prize) in enumerate(zip(winners, prizes[:-1]), 1):
            for stream in (None, f):
                print(f"{i}. {winner} wins {prize}", file=stream)

        for stream in (None, f):
            print("", file=stream)  # blank line

        for stream in (None, f):
            print_banner("🏆 GRAND PRIZE 🏆", color=93, file=stream)
            print(f"{winners[-1]} wins {prizes[-1]}", file=stream)


if __name__ == "__main__":
    run_raffle()