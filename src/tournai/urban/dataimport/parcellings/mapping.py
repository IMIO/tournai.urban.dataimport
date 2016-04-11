# -*- coding: utf-8 -*-

from tournai.urban.dataimport.parcellings.mappers import DescriptionMapper
from tournai.urban.dataimport.parcellings.mappers import LabelMapper
from tournai.urban.dataimport.parcellings.mappers import ParcellingFactory

from imio.urban.dataimport.mapper import SimpleMapper


OBJECTS_NESTING = [
    (
        'PARCELLING', [
        ],
    ),
]

FIELDS_MAPPINGS = {
    'PARCELLING':
    {
        'factory': [ParcellingFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'ID',
                    'to': 'id',
                },
                {
                    'from': 'DATE_D',
                    'to': 'authorizationDate',
                },
                {
                    'from': 'NBLOTS',
                    'to': 'numberOfParcels',
                },
            ),

            LabelMapper: {
                'from': (
                    'CODE_COMMU',
                    'REFDIREXT',
                    'SOUSCOM',
                    'TYPE',
                    'RUE',
                ),
                'to': 'label',
            },

            DescriptionMapper: {
                'from': (
                    'CODE_CREAT',
                    'CODE_UNIQU',
                    'TYPEDATE',
                    'REM_CREAT',
                    'N_MODIF',
                    'DATEPEREMP',
                    'PEREMPT',
                    'RENON',
                    'RENON_TYPE',
                    'REM_RW',
                ),
                'to': 'changesDescription',
            },
        },
    },
}
