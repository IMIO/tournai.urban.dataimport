# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.csv.importer import CSVDataImporter
from tournai.urban.dataimport.interfaces import ITournaiDataImporter


class TournaiDataImporter(CSVDataImporter):
    """ """

    implements(ITournaiDataImporter)
