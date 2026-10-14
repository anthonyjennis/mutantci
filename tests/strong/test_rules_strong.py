"""Strong test suite: checks every boundary in the pricing rules.

The rule of thumb: for each threshold, test the value ON it, just BELOW it,
and just ABOVE it. That's where off-by-one bugs (>= vs >) hide.
"""

import pytest

from core.rules import discount_percent, gst_percent, shipping_fee


# --- shipping_fee: free from 500, otherwise 50 ---------------------------

@pytest.mark.parametrize(
    "total, expected",
    [
        (0, 50),      # smallest valid order
        (499, 50),    # just below the threshold
        (500, 0),     # exactly on the threshold
        (501, 0),     # just above the threshold
    ],
)
def test_shipping_fee(total, expected):
    assert shipping_fee(total) == expected


# --- gst_percent: 5% up to and including 1000, 12% above -----------------

@pytest.mark.parametrize(
    "total, expected",
    [
        (0, 5),
        (999, 5),     # just below
        (1000, 5),    # on the threshold (still the low rate)
        (1001, 12),   # just above
    ],
)
def test_gst_percent(total, expected):
    assert gst_percent(total) == expected


# --- discount_percent: 0 below 2000, 10 from 2000, 15 from 5000 ----------

@pytest.mark.parametrize(
    "total, expected",
    [
        (0, 0),
        (1999, 0),    # just below tier 1
        (2000, 10),   # on tier 1
        (2001, 10),   # just above tier 1
        (4999, 10),   # just below tier 2
        (5000, 15),   # on tier 2
        (5001, 15),   # just above tier 2
    ],
)
def test_discount_percent(total, expected):
    assert discount_percent(total) == expected


# --- invalid input: every rule rejects a negative total -------------------

@pytest.mark.parametrize("rule", [shipping_fee, gst_percent, discount_percent])
def test_negative_total_is_rejected(rule):
    # ^ and $ make this an exact match, not "appears somewhere in the message"
    with pytest.raises(ValueError, match="^order total cannot be negative$"):
        rule(-1)