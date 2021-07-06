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

    def get_name(self) -> str:
        if self.name is not None:
            return self.name.replace(" ", "_")

    def get_age(self) -> int:
        if self.age is not None:
            return int(self.age.replace(" ", ""))

    def get_date(self) -> str:
        if self.date is not None:
            return self.date.replace("/", "_")

    def get_health_plan(self) -> str:
        if self.health_plan is not None:
            return self.health_plan

    def get_doctor(self) -> str:
        if self.doctor is not None:
            return self.doctor
