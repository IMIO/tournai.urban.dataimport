# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.excel.importer import ExcelDataImporter
from tournai.urban.dataimport.interfaces import ITournaiDataImporter


class TournaiDataImporter(ExcelDataImporter):
    """ """

    implements(ITournaiDataImporter)
