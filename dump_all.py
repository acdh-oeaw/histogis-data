import os
import glob
import json
from histogis.histogis import HistoGis
from histogis.histogis import merge_single_files


try:
    os.mkdir('single_files')
except FileExistsError:
    pass

dump = HistoGis().dump_all_file_per_feature(path='single_files')
all_in_one = merge_single_files()
