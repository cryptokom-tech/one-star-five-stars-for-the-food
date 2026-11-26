"""One Star, Five Stars for the Food — make.fun entry.

Writes one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt: an alien tourist's
one-star review of Earth with a real compliment for the food.
Stdlib only, no network, deterministic.
"""

import os

ENTRY = (
    "One star: I fed your sourdough starter for a week, named it, then "
    "watched you bake its children into bread so good I ate two slices "
    "and filed for custody of the jar before leaving orbit."
)


def validate_entry(text: str) -> None:
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must not have surrounding whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    sentence_endings = [char for char in text if char in ".!?"]
    assert len(sentence_endings) == 1 and text[-1] in ".!?", (
        "entry must be exactly one sentence"
    )


def main() -> None:
    validate_entry(ENTRY)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as output_file:
        output_file.write(ENTRY)

    with open(output_path, "rb") as output_file:
        written_entry = output_file.read().decode("utf-8")
    assert written_entry == ENTRY, "entry.txt differs from ENTRY"
    validate_entry(written_entry)


if __name__ == "__main__":
    main()
