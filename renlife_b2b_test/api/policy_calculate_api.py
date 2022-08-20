import datetime
import json


def policy_calculate_zapros_api(
        breef: str = 'INVESTOR_LUMP_4.1_BASE3_113_TM_CB_UBRIR',
        b2b_user_uuid: str = 'e4bf4d87-c500-424f-bed6-ca2355dab7a1',
        birth_date: str = '2000-10-10',
        ag_contract_num: int = 91061,
        base_sum: int = 30000,
        bso_series: int = 487,
        payment_terms: str = 'Единовременно',
        policy_period_brief: str = '3_YEARS',
        product_brief: str = 'INVESTOR_LUMP_4.1_BASE3_113_TM_CB',
        start_date: str = '2022-08-15',
        dtp_risk: int = None,
        calc_only: str = 'NO',
        save_policy:str = 'YES'
                            ):
    policy_calculate_zapros_api = '''
    {
        "method": "policy_calculate",
        "params": {
            "b2b_policy_params": {
                "b2b_partner_branch_office_id": 821,
                "b2b_partner_product_brief": "''' + breef +'''",
                "b2b_partner_product_version_id": 1161,
                "b2b_partner_sales_channel_brief": "RETAIL",
                "b2b_user_uuid": "''' + b2b_user_uuid +  '''"
            },
            "calc_only": "''' + calc_only + '''",
            "insured": [
                {
                    "assured_is_insuree": true,
                    "birth_date": "''' + str(birth_date) + '''",
                    "borlas_contact_id": null,
                    "gender": "f",
                    "surname": "Фамилия",
                    "name": "Имя",
                    "midname": "Отчество",
                    "programs": [
                        {
                            "is_enabled": true,
                            "proc": null,
                            "program_brief": "DMS_DD_TELEMEDICINE",
                            "program_name": "Обращение Застрахованного к Страховщику/ в Сервисную компанию за помощью, требующей оказания медицинских и иных услуг"
                        },
                        {
                            "is_enabled": true,
                            "proc": null,
                            "program_brief": "TERM_2",
                            "program_name": "Смерть Застрахованного по любой причине"
                        },
                        ''' + risk__ad_avto(enable_risk=dtp_risk) + '''
                        {
                            "is_enabled": true,
                            "proc": null,
                            "program_brief": "PEPR",
                            "program_name": "Дожитие с возвратом взносов в случае смерти"
                        }
                    ]
                }
            ],
            "insuree": {
                "borlas_contact_id": null
            },
            "policy": {
                "additional_properties": [
                    {
                        "property_brief": "HIGHER_OR_SECONDARY_FINANCIAL_EDUCATION_V2",
                        "property_name": "Я имею высшее образование (среднее специальное) в области экономики или финансов и/или окончил(а) курсы повышения квалификации в сфере экономики или финансов, и/или получил(а) хотя бы один из следующих сертификатов: квалификационный аттестат специалиста финансового рынка; квалификационный аттестат аудитора; квалификационный аттестат страхового актуария; сертификат «CharteredFinancialAnalyst (CFA)»; сертификат «CertifiedInternationalInvestmentAnalyst (CIIA); сертификат «FinancialRiskManager (FRM)».",
                        "value": "НЕТ"
                    },
                    {
                        "property_brief": "EXPERIENCE_WITH_FINANCIAL_INSTRUMENTS",
                        "property_name": "Я имею опыт работы с финансовыми инструментами: не менее 2х лет в организации, являющейся квалифицированным инвестором, не менее 3х лет в организации, которая осуществляла сделки с ценными бумагами и/или иными финансовыми инструментами (в том числе страховые компании, НПФ, Банки, УК)",
                        "value": "НЕТ"
                    },
                    {
                        "property_brief": "SECURITIES_TRANSACTIONS_V2",
                        "property_name": "Я регулярно совершал/совершаю сделки с ценными бумагами и/или заключал/заключаю договоры, являющиеся производными финансовыми инструментами за последние четыре квартала в среднем не реже 10 раз в квартал и не реже одного раза в месяц и/или ранее заключал договоры страхования с инвестиционной составляющей  и/или имею уже завершивший свое действие договор страхования с инвестиционной составляющей.",
                        "value": "НЕТ"
                    },
                    {
                        "property_brief": "VOLUME_OF_FINANCIAL_ASSETS",
                        "property_name": "Совокупный объем моих активов и финансовых инструментов (включая депозиты, текущие счета, ценные бумаги, доверительное управление, паи ПИФов (Паевых инвестиционных фондов), ИИС (Индивидуальный инвестиционный счёт), денежные средства, в том числе в иностранной валюте и т.п. превышают в сумме 1 400 000 (один миллион четыреста тысяч) рублей.",
                        "value": "НЕТ"
                    },
                    {
                        "property_brief": "SPECIALIZED_KNOWLEDGE_OF_FINANCE",
                        "property_name": "Я обладаю специальными знаниями в области финансов, позволяющими заключать договоры страхования жизни с инвестиционной составляющей и/или договоры накопительного страхования жизни.",
                        "value": "НЕТ"
                    }
                ],
                "ag_contract_num": "''' + str(ag_contract_num) + '''",
                "base_sum": "''' + str(base_sum) + '''",
                "bso_series": ''' + str(bso_series) + ''',
                "fund": "RUR",
                "payment_terms": "''' + payment_terms + '''",
                "policy_period_brief": "''' + policy_period_brief + '''",
                "product_brief": "''' + product_brief + '''",
                "reinvested_pol_header_id": null,
                "start_date": "''' + str(datetime.date.today()) + '''"
            },
            "save_policy": "''' + save_policy + '''"
        }
    }'''
    return policy_calculate_zapros_api

def risk__ad_avto(enable_risk):
    risk = '''
    {
        "is_enabled": true,
        "proc": null,
        "program_brief": "AD_AVTO",
        "program_name": "Смерть Застрахованного, наступившая в результате несчастного случая, а именно дорожно-транспортного происшествия (подключается при взносе от 1,5 млн. рублей)"
    },
    '''
    return risk if enable_risk == 1 else ''


def test_risk__ad_avto():
    print(risk__ad_avto(enable_risk=1))


def test_print():
    print(policy_calculate_zapros_api(dtp_risk=0, breef='INVESTOR_LUMP_4.1_BASE3_113_TM_CB_UBRIR', birth_date='2000-10-10', ag_contract_num= 91061, base_sum= 30000, bso_series = 487, payment_terms= 'Единовременно', policy_period_brief= '3_YEARS', product_brief= 'INVESTOR_LUMP_4.1_BASE3_113_TM_CB', start_date= '2022-08-15'))

def test_vznos():
    print(policy_calculate_zapros_api(dtp_risk=0, breef='INVESTOR_LUMP_4.1_BASE3_113_TM_CB_UBRIR',
                                      birth_date='2000-10-10', ag_contract_num=91061, base_sum=30000, bso_series=487,
                                      payment_terms='Единовременно', policy_period_brief='3_YEARS',
                                      product_brief='INVESTOR_LUMP_4.1_BASE3_113_TM_CB', start_date='2022-08-15',
                                      calc_only='YES', save_policy='NO')
          )
