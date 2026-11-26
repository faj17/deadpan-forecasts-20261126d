#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist.

Writes a single deadpan weather forecast line for Quesselton to
/output/entry.txt, exactly as a TV meteorologist would read it.
"""

import os

FORECAST_PARTS = [
    "Overnight in Quesselton: a high of 72, a low of 19, ",
    "and a 40 percent chance of rain falling upward, ",
    "so bring an umbrella and hold it underneath you.",
]

MAX_CHARS = 160

OUTPUT_PATH = "/output/entry.txt"


def assemble(parts):
    return "".join(parts)


def validate(line):
    if len(line) > MAX_CHARS:
        raise ValueError(
            "forecast is %d chars, over the %d-char limit" % (len(line), MAX_CHARS)
        )
    if not line.strip():
        raise ValueError("forecast is empty")
    return line


FORECAST = validate(assemble(FORECAST_PARTS))


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORECAST)
    print(FORECAST)


if __name__ == "__main__":
    main()
