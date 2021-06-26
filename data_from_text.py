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
# import unidecode
from pymongo.mongo_client import MongoClient
from human_info import PatientInfo
import re
from typing import Any, Union

import blood_info
from blood_info import CellInfo
import pymongo


class ExamData:
    """"""

    def __init__(self, text) -> None:
        """"""
        self.text = text
        self.PatientInfo_obj: Union[PatientInfo, Any] = None
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

        self.PatientInfo_obj = PatientInfo(
            name=loc_name,
            age=loc_age,
            health_plan=None,
            doctor=None,
            protocol=loc_protocol,
            date=loc_date,
        )

    def set_blood_info(self):
        """"""
        for line in self.text:
            for cell_elem in blood_info.blood_data_tags:
                if cell_elem in line:
                    loc_cell_info_obj = self.number_info(line, cell_elem)
                    if loc_cell_info_obj:
                        self.blood_info_list.append(loc_cell_info_obj)
                    break

    def check_value_unit_group(self, search_obj):
        """"""
        result = []
        for i in range(1, search_obj.groups().__len__() + 1):
            if search_obj.group(i) is not None:
                loc_value = search_obj.group(i)
                result.append(loc_value)
                loc_unit = search_obj.group(i + 1)
                result.append(loc_unit)
                break
        # Do not return a empty list
        if not result:
            result = [None, None]
        return result

    def number_info(self, line, name):
        """
        Receives a line and will search for "integer" or "float" numbers in this line and return
        reference: https://docs.python.org/3/library/re.html

        Since this document dont have a default (yet) so its problematic to work on this, could have missing value
        in the future
        """

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
            # print(line)
            # print(loc_integer_with_unit)
            # print(loc_integer_with_unit.groups().__len__())
            # for i in range(1, loc_integer_with_unit.groups().__len__() + 1):
            #     if loc_integer_with_unit.group(i) is not None:
            #         loc_value = loc_integer_with_unit.group(i)
            #         if loc_integer_with_unit.group(i + 1) is not None:
            #             loc_unit = loc_integer_with_unit.group(i + 1)

            loc_value_unit = self.check_value_unit_group(loc_integer_with_unit)
            # print(loc_integer_with_unit.groups())
            return blood_info.CellInfo(
                name=name,
                value=loc_value_unit[0],
                unit=loc_value_unit[1],
            )
        elif loc_float_with_unit:
            loc_value_unit = self.check_value_unit_group(loc_float_with_unit)
            # print(loc_float_with_unit.groups())
            return blood_info.CellInfo(
                name=name,
                value=loc_value_unit[0],
                unit=loc_value_unit[1],
            )
        elif loc_porcent:
            loc_value_unit = self.check_value_unit_group(loc_porcent)
            # print(loc_porcent.groups())
            return blood_info.CellInfo(
                name=name,
                value=loc_value_unit[0],
                unit=loc_value_unit[1],
            )
        elif loc_alone_numbers:
            # loc_value_unit = self.check_value_unit_group(loc_alone_numbers)
            # print(loc_alone_numbers.groups())
            return blood_info.CellInfo(
                name=name,
                value=loc_alone_numbers.group(),  # TODO avaliate this value 00    00 what to do?
                unit=None,
            )
        else:
            return None

    def search_str(self, sub_str):
        for line in self.text:
            if sub_str in line:
                return line.split(sub_str, 1)[1].split("  ", 1)[0]


class HealthDataBase:
    """"""

    def __init__(self, exam_data_obj) -> None:
        """"""

        self.exam_data_obj: Union[ExamData, Any] = exam_data_obj

        self.db_client: Union[MongoClient] = pymongo.MongoClient(
            "mongodb://localhost:27017/"
        )

        self.health_db = self.db_client["health_database"]
        self.patient_obj: Union[PatientInfo, Any] = self.exam_data_obj.PatientInfo_obj

        collection_name = self.patient_obj.get_name()
        collection_date = self.patient_obj.get_date()
        self.patient_collection = self.health_db[
            collection_name + "_" + collection_date
        ]

        self.load_data()

    def load_data(self):
        """"""
        for elem in self.exam_data_obj.blood_info_list:
            loc_cell_obj: Union[CellInfo] = elem
            post = {
                "name": loc_cell_obj.get_name(),
                "value": loc_cell_obj.get_value(),
                "unit": loc_cell_obj.get_unit(),
            }
            self.patient_collection.insert_one(post)
