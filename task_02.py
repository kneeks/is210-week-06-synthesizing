#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module prepares an email template."""


def prepare_email(appointments):
    """
    This function sends automatic email responses with designated format.

    Args:
        appointments (mixed): name, date

    Returns:
        mixed: automatic response with appointments filled in designated areas

    Examples:

        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']

    """
    email = ('Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe')
    apt = []
    for items in appointments:
        apt.append(email.format(items[0], items[1]))
    return apt
