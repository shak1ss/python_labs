def normalize(text, *, casefold=True, yo2e=True):
    s = text if text is not None else ""
    if casefold:
        s = s.casefold()
    if yo2e:
        s = s.replace("ё", "е")
    s = s.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    s = " ".join(s.split())
    return s


def tokenize(text):
    tokens = []
    buf = []
    used_hyphen = False  # один дефис внутри слова

    def flush():
        nonlocal buf, used_hyphen
        if buf:
            tokens.append("".join(buf))
            buf = []
            used_hyphen = False

    for ch in text:
        if ch.isalnum() or ch == "_":
            buf.append(ch)
        elif ch == "-":
            if buf and not used_hyphen:
                buf.append(ch)
                used_hyphen = True
            else:
                flush()
        else:
            flush()
    flush()
    return tokens


def count_freq(tokens):
    freq = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1
    return freq


def top_n(freq, n=5):
    items = list(freq.items())
    items.sort(key=lambda kv: (-kv[1], kv[0]))
    return items[:max(0, int(n))]