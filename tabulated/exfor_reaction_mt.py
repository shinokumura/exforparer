####################################################################
#
# This file is part of exfor-parser.
# Copyright (C) 2022 International Atomic Energy Agency (IAEA)
#
# Disclaimer: The code is still under developments and not ready
#             to use. It has been made public to share the progress
#             among collaborators.
# Contact:    nds.contact-point@iaea.org
#
####################################################################
import sys
import json

sys.path.append("../")
from utilities.utilities import slices


def get_mf(react_dict):

    if sf_to_mf.get(react_dict["sf6"]):
        if react_dict["sf6"] == "NU":
            return sf_to_mf[react_dict["sf6"]]

        elif react_dict["sf4"] == "0-G-0":
            return "12"  # Multiplicity of photon production

        else:
            return sf_to_mf[react_dict["sf6"]]
    else:
        return "?"


def get_mt(react_dict):

    if react_dict["sf6"] == "FY":
        return mt_fy_sf5[react_dict["sf5"]]["mt"] if react_dict["sf5"] else ""
    
    elif react_dict["sf6"] == "NU":
        return mt_nu_sf5[react_dict["sf5"]]["mt"] if react_dict["sf5"] else ""
    
    else:
        if (
            react_dict["process"].split(",")[0] == "N"
            and react_dict["process"].split(",")[1] == "INL"
        ):
            return "4"

        elif (
            react_dict["process"].split(",")[0] != "N"
            and react_dict["process"].split(",")[1] == "N"
        ):
            return "4"

        else:
            return sf3_dict[react_dict["process"].split(",")[1]]["mt"]




sf6_to_dir = {
    "SIG": "xs",
    "DA": "angle",
    "DE": "energy",
    "NU": "neutrons",
    "DL": "neutrons",
    "NU/DE": "neutrons/energy",
    "FY": "fission/yield",
    "FY/DE": "fission/energy",
    "KE": "kinetic_energy",
    "AKE": "kinetic_energy/average",
}


## The allowed SF5 for SIG data
sig_sf5 = {"IND": "RP",
            "CUM": "RP", 
            "(CUM)": "RP", 
            "M+": "RP", 
            "M-": "RP", 
            "(M)": "RP"}


## The MT number allocation and directory name for FY data
mt_fy_sf5 = {
    "CUM": {"mt": "459", "name": "cumulative"}, 
    "CHN": {"mt": "459", "name": "cumulative"},
    "IND": {"mt": "454", "name": "independent"},
    "SEC": {"mt": "454", "name": "independent"},
    "MAS": {"mt": "454", "name": "independent"},
    "SEC/CHN": {"mt": "454", "name": "independent"},
    "CHG": {"mt": "454", "name": "independent"},
    "PRE": {"mt": "460", "name": "primary"},
    "PRV": {"mt": "460", "name": "primary"},
    "TER": {"mt": "460", "name": "primary"},
    "QTR": {"mt": "460", "name": "primary"},
    "PR": {"mt": "460", "name": "primary"},
}

## The MT number allocation and directory name for NU (neutron observables) data
mt_nu_sf5 = {
    "": {"mt": "452", "name": ""},
    "PR": {"mt": "456", "name": "prompt"},
    "SEC": "",
    "SEC/PR": {"mt": None, "name": "miscellaneous"},
    "DL": {"mt": "455", "name": "delayed"},
    "TER": {"mt": "456", "name": "prompt"},
    "DL/CUM": {"mt": "455", "name": "delayed"},
    "DL/GRP": {"mt": "455", "name": "delayed"},
    "PR/TER": {"mt": None, "name": "miscellaneous"},
    "PRE/PR": {"mt": None, "name": "miscellaneous"},
    "SEC/PR": {"mt": None, "name": "miscellaneous"},
    "PRE/PR/FRG": {"mt": None, "name": "miscellaneous"},
    "PR/FRG": {"mt": None, "name": "miscellaneous"},
    "PR/PAR": {"mt": None, "name": "miscellaneous"},
    "PR/NUM": {"mt": None, "name": "miscellaneous"},
    "NUM": {"mt": None, "name": "miscellaneous"},
}



def mt_to_reaction():
    with open("tabulated/MTall.dat") as f:
        lines = f.readlines()

    mt_dict = {}
    sf3_dict = {}
    for line in lines:
        if line.startswith("#"):
            continue

        data = line.strip().split()

        mt_dict[data[0]] = {}
        mt_dict[data[0]]["reaction"] = data[1] if len(data) >= 2 else None
        mt_dict[data[0]]["sf3"] = data[2] if len(data) >= 3 else None
        mt_dict[data[0]]["sf5-8"] = data[3] if len(data) >= 4 else None

        sf3_dict[data[2]] = {}  # if len(data) >= 3 else None: {} }
        sf3_dict[data[2]]["mt"] = data[0]
        sf3_dict[data[2]]["reaction"] = data[1] if len(data) >= 2 else None
        sf3_dict[data[2]]["sf5-8"] = data[3] if len(data) >= 4 else None

    return sf3_dict


sf3_dict = mt_to_reaction()


def e_lvl_to_mt50(level_num):
    mt = list(range(50, 91))
    if level_num is None:
        return None
    elif int(level_num) < 40:
        return str(mt[int(level_num)])
    else:
        return "91"


sf_to_mf = {
    "NU": "1",
    "WID": "2",
    "ARE": "2",
    "D": "2",
    "EN": "2",
    "J": "2",
    "SIG": "3",
    "DA": "4",
    "DE": "5",
    "FY": "8",
    "DA/DE": "6",
}

