# https://www.codewars.com/kata/human-readable-duration-format

def format_duration(seconds):
    if not seconds:
        return "now"

    units = [
        ("year",  365 * 24 * 60 * 60),
        ("day",  24 * 60 * 60),
        ("hour",  60 * 60),
        ("minute",  60),
        ("second",  1)
    ]

    parts = []

    for unit, divisor in units:
        quantity, seconds = divmod(seconds, divisor)
        if quantity:
            parts.append("{} {}{}".format(quantity, unit, "s" if quantity > 1 else ""))

    return parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + " and " + parts[-1]