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
import blood_info
from blood_info import CellInfo
import re
from typing import Union, Any


class ExamData:
    """"""

    def __init__(self, text) -> None:
        """"""
        self.text = text
        self.PatientInfo_obj = None
        self.blood_info_list: Union[CellInfo, Any] = []
        self.set_patient_info()
        self.set_blood_info()

    def set_patient_info(self):
        """"""
        loc_name = self.search_str("Paciente: ")
        loc_age = self.search_str("Idade: ")
        loc_protocol = self.search_str("Protocolo: ")
        loc_date = self.search_str("Data: ")

        # loc_health_plan = self.search_str("Convenio: ")
        # loc_doctor = self.search_str("Medico: ")

        PatientInfo_obj = PatientInfo(
            name=loc_name,
            age=loc_age,
            health_plan=None,
            doctor=None,
            protocol=loc_protocol,
            date=loc_date,
        )
        PatientInfo

    def set_blood_info(self):
        """"""
        for line in self.text:
            for cell_elem in blood_info.blood_data_tags:
                if cell_elem in line:
                    loc_cell_info_obj = self.number_info(line, cell_elem)
                    if loc_cell_info_obj:
                        self.blood_info_list.append(loc_cell_info_obj)
                    break

        print(self.blood_info_list)

    @staticmethod
    def number_info(line, name):
        """
        Receives a line and will search for "integer" or "float" numbers in this line and return
        reference: https://docs.python.org/3/library/re.html

        Since this document dont have a default (yet) so its problematic to work on this, could have missing value
        in the future
        """
        numbers = []

        loc_integer_with_unit = re.search(
            r"(\s\d+\s)(\/\w+) | (\s\d+\s)(\w+)|(\s\d+\s)(\w+\d)|(\s\d+\s)(\w+\/\w+)",
            line,
        )  # 00,00 xX/xX         | 00 xX/xX      | 00,00 xX      | 00 xX    | 00 xX0     | 00,00 /xX       | 00 /xX
        loc_porcent = re.search(r"(\d+\,\d+\s)(\%) | (\d+\s)(\%)", line)

        loc_alone_numbers = re.search(r"(\d+\s) | (\d+\,\d+\s) | (\d+\s+\d+\s)", line)

        loc_float_with_unit = re.search(
            r"(\d+\,\d+\s)(\w+\/\w+)|(\d+\,\d+\s)(\/\w+)", line
        )

        if loc_integer_with_unit:  # 00,00 unit/unit
            return blood_info.CellInfo(
                name=name,
                value=loc_integer_with_unit.group(1),
                unit=loc_integer_with_unit.group(2),
            )
        elif loc_float_with_unit:
            return blood_info.CellInfo(
                name=name,
                value=loc_float_with_unit.group(1),
                unit=loc_float_with_unit.group(2),
            )
        elif loc_porcent:
            return blood_info.CellInfo(
                name=name,
                value=loc_porcent.group(1),
                unit=loc_porcent.group(2),
            )
        elif loc_alone_numbers:
            return blood_info.CellInfo(
                name=name,
                value=loc_alone_numbers.group(1),
                unit=loc_alone_numbers.group(2),
            )
        else:
            return None

    def search_str(self, sub_str):
        for line in self.text:
            if sub_str in line:
                return line.split(sub_str, 1)[1].split("  ", 1)[0]
