import random


def encode(bit: int, n: int) -> list[int]:
    """Repeat one bit n times (n should be odd)."""
    return [bit] * n


def apply_noise(bits: list[int], p: float, rng: random.Random) -> list[int]:
    """Flip each bit independently with probability p."""
    return [(b ^ 1) if rng.random() < p else b for b in bits]


def decode(bits: list[int]) -> int:
    """Majority vote."""
    return 1 if sum(bits) > len(bits) / 2 else 0


def logical_error_rate(p: float, n: int, trials: int, seed: int = 0) -> float:
    """How often the decoded bit differs from the bit that was sent."""
    rng = random.Random(seed)
    errors = 0
    for _ in range(trials):
        sent = rng.randint(0, 1)
        received = apply_noise(encode(sent, n), p, rng)
        if decode(received) != sent:
            errors += 1
    return errors / trials