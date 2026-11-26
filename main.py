"""One deadpan forecast for a city that does not exist.

Produces /output/entry.txt (or $ENTRY_OUTPUT): a single overnight
forecast for Dribbleford, read out in the flat, unbothered voice of
a late-night weather presenter. It gets cold, the river turns into
a skating rink, and the local ducks have already lodged a formal
complaint about the whole business.
"""

import os

ENTRY = (
    "Overnight in Dribbleford, temperatures fall to minus two, "
    "the river freezes solid enough to skate on, and the ducks "
    "have already filed complaints."
)

CHAR_LIMIT = 160


def is_one_sentence(text):
    """One forecast, one sentence: no line breaks, one full stop."""
    if "\n" in text or "\r" in text:
        raise ValueError("forecast must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("forecast must be exactly one sentence")
    return True


def mentions_city(text):
    """The forecast has to be about Dribbleford, the invented city."""
    if "Dribbleford" not in text:
        raise ValueError("forecast must name Dribbleford")
    return True


def has_temperature_drop(text):
    """An overnight forecast needs the cold: a falling temperature."""
    lowered = text.lower()
    if "temperatures fall" not in lowered:
        raise ValueError("forecast must say the temperature falls")
    if "minus two" not in lowered:
        raise ValueError("forecast must give the overnight low")
    return True


def has_ducks_complaint(text):
    """The deadpan punchline: the ducks have filed complaints."""
    if "ducks have already filed complaints" not in text:
        raise ValueError("forecast is missing the ducks' complaint")
    return True


def has_frozen_river(text):
    """The freeze has to be hard: a river solid enough to skate on."""
    lowered = text.lower()
    if "river freezes solid" not in lowered:
        raise ValueError("forecast must freeze the river solid")
    if "skate on" not in lowered:
        raise ValueError("forecast must let someone skate on the river")
    return True


def within_length(text):
    """Broadcast lines stay short: 1 to 160 characters, no padding."""
    if not text.strip():
        raise ValueError("forecast must not be blank")
    if len(text) > CHAR_LIMIT:
        raise ValueError("forecast too long: %d chars" % len(text))
    return True


def validate(text):
    """Run every check on the forecast before it is written out."""
    for check in (
        is_one_sentence,
        mentions_city,
        has_temperature_drop,
        has_frozen_river,
        has_ducks_complaint,
        within_length,
    ):
        check(text)
    return True


def main():
    validate(ENTRY)
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print("wrote %d characters to %s" % (len(ENTRY), output_path))


if __name__ == "__main__":
    main()
