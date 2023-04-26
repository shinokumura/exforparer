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

DICTIONARY_URL = "https://nds.iaea.org/nrdc/ndsx4/trans/dictionaries/"
DICTIONARY_PATH = "./exfor_dictionary/"
LATEST_TRANS = "9127"

""" EXFOR master file path """
EXFOR_MASTER_REPO_PATH = "/Users/okumuras/Documents/nucleardata/EXFOR/exfor_master/"
EXFOR_ALL_PATH = EXFOR_MASTER_REPO_PATH + "exforall/"


""" Pickle path of list of EXFOR master files made by parser.list_x4files.py"""
ENTRY_INDEX_PICKLE = "pickles/entry.pickle"


""" Pickle path of list of all reactions made by indexing.py """
REACTION_INDEX_PICKLE = "pickles/reactions.pickle"

TO_JSON = True
POST_DB = False


OUT_PATH = "../"
MONGOBASE_URI = "https://data.mongodb-api.com/app/data-qfzzc/endpoint/data/beta/"
