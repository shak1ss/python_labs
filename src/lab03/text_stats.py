import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    input_text = sys.stdin.readline()

    text_norm = normalize(input_text)
    tokens = tokenize(text_norm)
    freq = count_freq(tokens)

    words_total = len(tokens)
    unique_words = len(freq)

    top_words = top_n(freq, 5)

    print(f"Всего слов: {words_total}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
