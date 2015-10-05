#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module counts total amount of guests and total tables needed."""


def get_party_stats(families, table_size=6):
    """
    This function that can analyze arbitrary lists of families and return a
    total headcount for your caterer as well as a total number of tables needed.

    Args:
        families (str): Nested list of guests names

        table_size (int): number of tables default = 6

        loop (for): counts every guest and adds it to the total_guest count
                    counts each family and adds it to the tables needed

    Returns:
        int: total guests, int: total amount of tables per family

    Examples:

        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
        (6, 3)

        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']]
                            , 2)
        (6, 4)

    """
    total_tables = 0
    total_guests = 0
    for guests in families:
        num_guests = len(guests)
        total_guests += num_guests
        total_tables += (-(-num_guests // table_size))
    return (total_guests, total_tables)
