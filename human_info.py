#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Pablo Freitas
# Created Date: Son June 13 12:42:00 PDT 2021
# =============================================================================
"""The Module Has Been Build for having a scrutured place of all information for the patient. """

__author__ = "Pablo Freitas"
__copyright__ = "Copyright 2021, Keep Track of Health"
__credits__ = ["Pablo Freitas", "Diego Freitas"]
__license__ = "None"
__version__ = "1.0.0"
__maintainer__ = "Pablo Freitas"
__email__ = "pablofreitas.fn@gmail.com"
__status__ = "Prototype"

# =============================================================================
# Imports
# =============================================================================


class PatientInfo:
    def __init__(
        self,
        name=None,
        age=None,
        health_plan=None,
        doctor=None,
        protocol=None,
        date=None,
    ):
        """"""
        self.name = name
        self.age = age
        self.health_plan = health_plan
        self.doctor = doctor
        self.protocol = protocol
        self.date = date
