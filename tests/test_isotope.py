#!/usr/bin/env python

"""Tests for `isotopes` module."""

import pytest

from deepburn import isotope


@pytest.mark.parametrize(
    "name, zzzaaam",
    [
        ("Am241", (95, 241, 0)),
        ("Am241m", (95, 241, 1)),
        ("Am241mm", (95, 241, 2)),
        ("Am-241", (95, 241, 0)),
        ("Am-241m", (95, 241, 1)),
        ("Am-241mm", (95, 241, 2)),
        ("Americium241", (95, 241, 0)),
        ("Americium241m", (95, 241, 1)),
        ("Americium241mm", (95, 241, 2)),
        ("Americium-241", (95, 241, 0)),
        ("Americium-241m", (95, 241, 1)),
        ("Americium-241mm", (95, 241, 2)),
        ("241Am", (95, 241, 0)),
        ("241mAm", (95, 241, 1)),
        ("241mmAm", (95, 241, 2)),
        ("241-Am", (95, 241, 0)),
        ("241m-Am", (95, 241, 1)),
        ("241mm-Am", (95, 241, 2)),
        ("241Americium", (95, 241, 0)),
        ("241mAmericium", (95, 241, 1)),
        ("241mmAmericium", (95, 241, 2)),
        ("241-Americium", (95, 241, 0)),
        ("241m-Americium", (95, 241, 1)),
        ("241mm-Americium", (95, 241, 2))
    ]
)
def test_str2zzzaam(name, zzzaaam):
    result = isotope._str2zzzaaam(name)
    assert result == zzzaaam


def test_str2zzzaam_exceptions_1():
    with pytest.raises(ValueError):
        isotope._str2zzzaaam('Ap241')


def test_str2zzzaam_exceptions_2():
    with pytest.raises(ValueError):
        isotope._str2zzzaaam('Alhambra241')
