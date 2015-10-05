#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module counts total amount of guests and total tables needed."""


def prepare_email(appointments):
    appointments = [{}]
    email = ('Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe')
    for names in appointments:
        email.format(appointments)
        return email
