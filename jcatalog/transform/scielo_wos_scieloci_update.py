# coding: utf-8
'''
This script reads data from various sources to process and store in MongoDB.
'''
import pyexcel
import logging

import models
from transform_date import *
from accent_remover import *

logging.basicConfig(filename='logs/scieloci.info.txt', level=logging.INFO)
logger = logging.getLogger(__name__)


# Add SciELO CI indicators for journals
def scieloci(filename):
    access = pyexcel.get_sheet(
        file_name=filename,
        sheet_name='import',
        name_columns_by_row=0)

    access_json = access.to_records()

    for rec in access_json:
        # # remove empty keys
        # rec = {k: v for k, v in rec.items() if v or v == 0}
        print('\n')

        query = models.Scielo.objects.filter(issn_list=rec['issn_scielo'])
        if len(query) == 1:
            doc = query[0]
            print(query[0]['issn_scielo'])
            data = {'scieloci': {}}
            data['scieloci'] = dict(rec)
        else:
            print('não encontrou: ' + str(rec['issn_scielo']))

        if data:
            doc.modify(**data)


def main():
    # SciELO docs counts Network xlsx
    scieloci('data/scielo/td_wos_all_downloads.xlsx')


if __name__ == "__main__":
    main()
