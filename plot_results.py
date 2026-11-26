import matplotlib

matplotlib.use("Agg")  # draw to a file, no window needed
import matplotlib.pyplot as plt

from repetition_code import logical_error_rate


def main():
    error_rates = [i / 100 for i in range(1, 51)]  # 0.01 to 0.50
    plt.figure(figsize=(7, 5))
    for copies in (1, 3, 5, 7):
        results = [logical_error_rate(p, copies, trials=5000) for p in error_rates]
        plt.plot(error_rates, results, label=f"{copies} copy" if copies == 1 else f"{copies} copies")
    plt.xlabel("Physical error rate (chance each bit flips)")
    plt.ylabel("Logical error rate (decoded bit is wrong)")
    plt.title("Repetition code: more copies, fewer errors")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("results.png", dpi=150, bbox_inches="tight")
    print("Saved results.png")


if __name__ == "__main__":
    main()