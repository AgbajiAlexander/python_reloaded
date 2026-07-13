# text-tool

A simple command-line text completion / editing / auto-correction tool written in Python.

It reads a text file, applies a series of formatting and correction rules, and writes the
result to an output file.

## Usage

```bash
python3 main.py <input_file> <output_file>
```

Example:

```bash
python3 main.py input.txt output.txt
```

If the wrong number of arguments is given, the program prints a usage message and exits
with a non-zero status code.

## What it does

The tool applies the following transformations, in order:

1. **`(hex)`** — replaces the word before it with the decimal value of that hexadecimal
   number.
   `"1E (hex) files were added"` → `"30 files were added"`

2. **`(bin)`** — replaces the word before it with the decimal value of that binary number.
   `"It has been 10 (bin) years"` → `"It has been 2 years"`

3. **`(up)`** — uppercases the word before it.
   `"Ready, set, go (up) !"` → `"Ready, set, GO!"`

4. **`(low)`** — lowercases the word before it.
   `"I should stop SHOUTING (low)"` → `"I should stop shouting"`

5. **`(cap)`** — capitalizes the word before it.
   `"Welcome to the Brooklyn bridge (cap)"` → `"Welcome to the Brooklyn Bridge"`

   `(up)`, `(low)`, and `(cap)` all accept an optional count, e.g. `(up, 2)`, which applies
   the transformation to that many words before the tag instead of just one.
   `"This is so exciting (up, 2)"` → `"This is SO EXCITING"`

6. **Punctuation spacing** — `. , ! ? : ;` are moved to sit directly against the previous
   word, with exactly one space before the next word. Consecutive punctuation marks
   (e.g. `...`, `!?`) are treated as a single group and not split apart.
   `"I was sitting over there ,and then BAMM !!"` → `"I was sitting over there, and then BAMM!!"`

7. **Quotes (`'`)** — pairs of single-quote marks are moved to hug the word(s) between
   them, with no internal spacing.
   `"I am exactly how they describe me: ' awesome '"` → `"I am exactly how they describe me: 'awesome'"`

8. **`a` → `an`** — a standalone `a` is changed to `an` if the following word begins with
   a vowel (`a, e, i, o, u`) or `h`. Original capitalization is preserved.
   `"There it was. A amazing rock!"` → `"There it was. An amazing rock!"`

## Project structure

```
text-tool/
├── main.py                  # entry point: reads args, reads file, runs pipeline, writes file
├── transformations.py       # all transformation functions
├── test_transformations.py  # unit tests
├── input.txt                # sample input
└── output.txt               # generated output
```

## How it works internally

`main.py` reads the input file into a string, passes it through `process_text()` from
`transformations.py`, and writes the result to the output file.

`process_text()` runs the following pipeline, each step feeding its output into the next:

```python
def process_text(text):
    text = convert_hex(text)
    text = convert_bin(text)
    text = convert_case(text, "up")
    text = convert_case(text, "low")
    text = convert_case(text, "cap")
    text = fix_a_an(text)
    text = fix_punctuation(text)
    text = fix_quotes(text)
    return text
```

Order matters: number/case tags are resolved first (while the text is still cleanly
tag-marked), then `a`/`an` correction, then whitespace/punctuation cleanup, then quote
tightening last.

## Running tests

Unit tests are written with Python's built-in `unittest` module.

```bash
python3 -m unittest
```

## Requirements

- Python 3
- No third-party packages — only the standard library (`sys`, `re`) is used.
