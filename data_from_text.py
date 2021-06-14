#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Pablo Freitas
# Created Date: Son June 13 12:42:00 PDT 2021
# =============================================================================
"""The Module Has Been Build for having a scrutured place of all information from the text. """

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
import unidecode
from human_info import PatientInfo


class ExamData:
    """"""

    def __init__(self, text) -> None:
        """"""
        self.text = text
        self.PatientInfo_obj = PatientInfo()
        self.set_patient_info()

    def set_patient_info(self):
        """"""
        loc_name = self.search_str("Paciente: ")
        loc_age = self.search_str("Idade: ")
        loc_protocol = self.search_str("Protocolo: ")
        loc_date = self.search_str("Data: ")
        # loc_health_plan = self.search_str("Convenio: ")
        # loc_doctor = self.search_str("Medico: ")

    def search_str(self, sub_str):
        for line in self.text:
            if sub_str in line:
                return line.split(sub_str, 1)[1].split("  ", 1)[0]
