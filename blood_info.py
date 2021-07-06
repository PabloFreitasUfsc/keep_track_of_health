#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Pablo Freitas
# Created Date: Son June 13 12:42:00 PDT 2021
# =============================================================================
"""The Module Has Been Build for having a scrutured place of all information inside the blood. """

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
import colorama


def warning_text(text):
    """"""
    print(colorama.Fore.YELLOW + text + colorama.Style.RESET_ALL)


def error_text(text):
    """"""
    print(colorama.Fore.RED + colorama.Back.GREEN + text + colorama.Style.RESET_ALL)


class CellInfo:
    def __init__(self, name="default", value="0.0", unit="None") -> None:
        self.name = name
        self.value = value
        self.unit = unit  # TODO treat with pint maybe

    def get_name(self):
        if self.name is not None:
            return self.name.replace(" ", "")
        else:
            warning_text("Name missing.")
            return None

    def get_value(self):
        if self.value is not None:
            return float(
                self.value.replace(" ", "").replace(",", ".")
            )  # Be careful witht the , and the .
        else:
            warning_text(
                "Missing value definition, CellInfo.value = %s." % self.get_value()
            )

    def get_unit(self):
        if self.unit is not None:
            return self.unit.replace(" ", "")
        else:
            warning_text(
                "Missing unit definition, CellInfo.name = %s." % self.get_name()
            )
            return None


class ExamTypeInfo:
    def __init__(self) -> None:
        self.methode
        self.observation
        self.material
        self.result
        self.indice


eritrograma = [
    "Hemacias",
    "Hemoglobina",
    "Hematocrito",
    "VCM",
    "HCM",
    "CHCM",
    "Plaquetas",
]
leucograma = [
    "Leucocitos",
    "Blastos",
    "Mieloblastos",
    "Promielocitos",
    "Mielocitos",
    "Metamielocitos",
    "Bastoes",
    "Segmentados",
    "Eosinofilos",
    "Basofilos",
    "Linfocitos",
    "Monocitos",
]
not_sorted = ["BILIRRUBINA TOTAL E FRACOES"]

not_sorted = not_sorted + ["CALCIO"]

not_sorted = not_sorted + ["CPK - CREATINOFOSFOQUINASE"]

not_sorted = not_sorted + ["CREATININA"]

not_sorted = not_sorted + ["RITMO DE FILTRACAO GLOMERULAR (RFG)"]

not_sorted = not_sorted + ["FOSFATASE ALCALINA"]

not_sorted = not_sorted + ["FOSFORO INORGANICO"]

not_sorted = not_sorted + ["GAMA-GT"]

not_sorted = not_sorted + ["GLICEMIA DE JEJUM"]

not_sorted = not_sorted + ["Colesterol"]

not_sorted = not_sorted + ["Triglicerides"]

not_sorted = not_sorted + ["Colesterol Hdl"]

not_sorted = not_sorted + ["Colesterol Ldl"]

not_sorted = not_sorted + ["Colesterol Vldl"]

not_sorted = not_sorted + ["TGO - Transaminase Oxalacetica"]

not_sorted = not_sorted + ["TGP - Transaminase Piruvica"]

not_sorted = not_sorted + ["Ureia"]

not_sorted = not_sorted + ["ANTI HBS - HEPATITE B"]

not_sorted = not_sorted + ["ANTICORPOS IgG HEPATITE A ANTI HVA-IgG"]

blood_data_tags = eritrograma + leucograma + not_sorted
