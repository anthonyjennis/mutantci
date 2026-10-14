"""Pricing rules for an online shop. All amounts are whole rupees (int).

These rules are invented for the demo; they are not real tax law.
"""


def _reject_negative(total: int) -> None:
    if total < 0:
        raise ValueError("order total cannot be negative")


def shipping_fee(total: int) -> int:
    """Free shipping from 500 upwards, otherwise a flat 50."""
    _reject_negative(total)
    if total >= 500:
        return 0
    return 50


def gst_percent(total: int) -> int:
    """5% GST up to and including 1000, 12% above that."""
    _reject_negative(total)
    if total <= 1000:
        return 5
    return 12


def discount_percent(total: int) -> int:
    """No discount below 2000, 10% from 2000, 15% from 5000."""
    _reject_negative(total)
    if total >= 5000:
        return 15
    if total >= 2000:
        return 10
    return 0