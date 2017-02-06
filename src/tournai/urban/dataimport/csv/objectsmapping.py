# -*- coding: utf-8 -*-

from tournai.urban.dataimport.csv.mappers import *
from imio.urban.dataimport.mapper import SimpleMapper

OBJECTS_NESTING = [
    (
        'LICENCE', [
            ('CONTACT', []),
            ('PARCEL', []),
            # ('DEPOSIT EVENT 1', []),
            ('DECISION EVENT', []),
            ('COLLEGE REPORT EVENT', []),
            # ('DOCUMENTS', []),
        ],
    ),
]

FIELDS_MAPPINGS = {
    'LICENCE':
    {
        'factory': [LicenceFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': "Reference",
                    'to': 'referenceDGATLP',
                },
                {
                    'from': 'Objet',
                    'to': 'licenceSubject',
                },
                {
                    'from': 'Delai annonce',
                    'to': 'annoncedDelay',
                },
            ),

            IdMapper: {
                'from': 'id',
                'to': 'id',
            },

            PortalTypeMapper: {
                'from': 'Type',
                'to': ('portal_type', 'folderCategory',)
            },

            WorklocationMapper: {
                'from': ('AdresseTravauxRue', 'AdresseTravauxNumero', 'AdresseTravauxBoite', 'AdresseTravauxVille'),
                'to': 'workLocations',
            },

           ArchitectMapper: {
               'allowed_containers': ['BuildLicence'],
               'from': ('Nom Architecte', 'Prenom Architecte', 'Societe Architecte'),
               'to': ('architects',)
           },

            FolderZoneTableMapper: {
               'from': ('Plan de Secteur 1', 'Plan de Secteur 2'),
               'to': 'folderZone',
           },



            # WorkTypeMapper: {
            #     'allowed_containers': ['BuildLicence', 'ParcelOutLicence'],
            #     'from': 'Code_220+',
            #     'to': 'workType',
            # },

            InquiryStartDateMapper: {
                'allowed_containers': ['BuildLicence', 'ParcelOutLicence', 'UrbanCertificateTwo'],
                'from': 'DateDebEnq',
                'to': 'investigationStart',
            },

            InquiryEndDateMapper: {
                'allowed_containers': ['BuildLicence', 'ParcelOutLicence', 'UrbanCertificateTwo'],
                'from': 'DateFinEnq',
                'to': 'investigationEnd',
            },

            InvestigationReasonsMapper: {
                'allowed_containers': ['BuildLicence', 'ParcelOutLicence', 'UrbanCertificateTwo'],
                'from': ('ParticularitesEnq1', 'ParticularitesEnq2'),
                'to': 'investigationReasons',
            },

            AskOpinionsMapper: {
                'from': (),
                'to': 'solicitOpinionsTo',
            },

            #
            # InquiryReclamationNumbersMapper: {
            #     'allowed_containers': ['BuildLicence', 'ParcelOutLicence', 'UrbanCertificateTwo'],
            #     'from': 'NBRec',
            #     'to': 'investigationWriteReclamationNumber',
            # },
            #
            # InquiryArticlesMapper: {
            #     'allowed_containers': ['BuildLicence', 'ParcelOutLicence', 'UrbanCertificateTwo'],
            #     'from': 'Enquete',
            #     'to': 'investigationArticles',
            # },
            #
            # ObservationsMapper: {
            #     'from': ('ParticularitesEnq1', 'ParticularitesEnq2'),
            #     'to': 'description',
            # },
            #
            # TechnicalConditionsMapper: {
            #     'from': ('memo_Autorisation', 'memo_Autorisation2'),
            #     'to': 'locationTechnicalConditions',
            # },

#            GeometricianMapper: {
#                'allowed_containers': ['ParcelOutLicence'],
#                'from': ('Titre', 'Nom', 'Prenom'),
#                'to': ('geometricians',)
#            },

            # ParcellingsMapper: {
            #     'table': 'LOTISSEM',
            #     'KEYS': ('Cle_Urba', 'Cle_Lot'),
            #     'mappers': {
            #         SimpleMapper: (
            #             {
            #                 'from': 'Lot',
            #                 'to': 'subdivisionDetails',
            #             },
            #         ),
            #         ParcellingUIDMapper: {
            #             'from': 'Lotis',
            #             'to': 'parcellings',
            #         },
            #
            #         IsInSubdivisionMapper: {
            #             'from': 'Lotis',
            #             'to': 'isInSubdivision',
            #         }
            #     },
            # },
            #
            # PcaMapper: {
            #     'table': 'PPA',
            #     'KEYS': ('Cle_Urba', 'Cle_PPA'),
            #     'mappers': {
            #         SimpleMapper: (
            #             {
            #                 'from': 'PPA_Affectation',
            #                 'to': 'pcaDetails',
            #             },
            #         ),
            #         PcaUIDMapper: {
            #             'from': 'PPA',
            #             'to': 'pca',
            #         },
            #
            #         IsInPcaMapper: {
            #             'from': 'PPA',
            #             'to': 'isInPCA',
            #         }
            #     },
            # },

            # EnvRubricsMapper: {
            #     'allowed_containers': ['EnvClassOne', 'EnvClassTwo', 'EnvClassThree'],
            #     'from': 'LibNat',
            #     'to': 'description',
            # },
            #
            CompletionStateMapper: {
                'from': ('Date Permis', 'Date Refus', 'Date Permis sur recours', 'Date Refus sur recours'),
                'to': (),  # <- no field to fill, its the workflow state that has to be changed
            },

            ErrorsMapper: {
                'from': (),
                'to': ('description',),  # log all the errors in the description field
            }
        },
    },

    'PARCEL':
    {
        'factory': [ParcelFactory, {'portal_type': 'PortionOut'}],

        'mappers': {
            ParcelDataMapper: {
                'from': ('Parcelle1section', 'Parcelle1numero', 'Parcelle1numerosuite', 'Parcelle2section', 'Parcelle2numero', 'Parcelle2numerosuite', 'AdresseTravauxVille'),
                'to': (),
            },
        },
    },

    'CONTACT':
    {
        'factory': [ContactFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'NomDemandeur1',
                    'to': 'name1',
                },
                {
                    'from': 'PrenomDemandeur1',
                    'to': 'name2',
                },
                {
                    'from': ('AdresseDemandeur1'),
                    'to': 'street',
                },
            ),

            ContactIdMapper: {
                'from': ('NomDemandeur1', 'PrenomDemandeur1', 'id'),
                'to': 'id',
            },
        },
    },

    'DECISION EVENT':
    {
        'factory': [UrbanEventFactory],

        'mappers': {
            DecisionEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            DecisionEventIdMapper: {
                'from': (),
                'to': 'id',
            },

            DecisionEventDateMapper: {
                'from': ('Date Permis', 'Date Refus', 'Date Permis sur recours', 'Date Refus sur recours'),
                'to': 'decisionDate',
            },

            DecisionEventDecisionMapper: {
                'from': ('Date Permis', 'Date Refus', 'Date Permis sur recours', 'Date Refus sur recours'),
                'to': 'decision',
            },

            DecisionEventNotificationDateMapper: {
                'from': ('Date Permis', 'Date Refus', 'Date Permis sur recours', 'Date Refus sur recours'),
                'to': 'eventDate',
            }
        },
    },

    'COLLEGE REPORT EVENT':
    {
        'factory': [UrbanEventFactory],

        'mappers': {
            CollegeReportTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            CollegeReportIdMapper: {
                'from': (),
                'to': 'id',
            },

            CollegeReportEventDateMapper: {
                'from': ('Rapport du College'),
                'to': 'eventDate',
            }
        },
    },
}