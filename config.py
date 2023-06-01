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
import os

DEVENV = True

if DEVENV:
    DATA_DIR = "/Users/okumuras/Documents/nucleardata/EXFOR/"
    MODULES_DIR = "/Users/okumuras/Dropbox/Development/"


else:
    DATA_DIR = "/srv/data/dataexplorer2/"
    MODULES_DIR = "/srv/data/dataexplorer2/"



EXFOR_DB = DATA_DIR + "exfor_tmp.sqlite"
ENDFTAB_DB = DATA_DIR + "endftables.sqlite"

## Package locations
EXFOR_PARSER = "exforparser/"
EXFOR_DICTIONARY = "exfor_dictionary/"
RIPL3 = "ripl3_json/"

sys.path.append(os.path.join(MODULES_DIR, EXFOR_DICTIONARY))
sys.path.append(os.path.join(MODULES_DIR, RIPL3))

""" pickel file path """
PICKLE_PATH = os.path.join(MODULES_DIR, EXFOR_DICTIONARY, "pickles/")

""" Pickle path of list of EXFOR master files made by parser.list_x4files.py"""
ENTRY_INDEX_PICKLE = "pickles/entry.pickle"

""" EXFOR master file path """
EXFOR_MASTER_REPO_PATH = os.path.join(DATA_DIR, "exfor_master/")
EXFOR_ALL_PATH = os.path.join(EXFOR_MASTER_REPO_PATH,  "exforall/")


TO_JSON = True
POST_DB = False


OUT_PATH = DATA_DIR +  "../../../Desktop/"


import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


""" SQL database """
engine = db.create_engine("sqlite:///" + EXFOR_DB)
session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
