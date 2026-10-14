"""Weak test suite: DELIBERATELY lazy. Used in the demo. Do not improve it.

Every line of core/rules.py runs, so coverage is 100%. But every value is far
from a threshold, so these tests can't notice a boundary bug like >= becoming >.
That gap is what mutation testing exposes.
"""

import pytest

from core.rules import discount_percent, gst_percent, shipping_fee


def test_shipping_fee():
    assert shipping_fee(100) == 50
    assert shipping_fee(3000) == 0


def test_gst_percent():
    assert gst_percent(100) == 5
    assert gst_percent(3000) == 12


def test_discount_percent():
    assert discount_percent(100) == 0
    assert discount_percent(3000) == 10
    assert discount_percent(9000) == 15


def test_negative_total_is_rejected():
    with pytest.raises(ValueError):
        shipping_fee(-50)