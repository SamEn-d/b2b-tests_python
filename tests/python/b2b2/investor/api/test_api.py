import os
import requests
import json
from renlife_b2b_test.api.policy_calculate_api import policy_calculate_zapros_api
from renlife_b2b_test.api.policy_update_info_api import policy_update_info_api

login_b2b = os.getenv('LOGIN_b2b2')
password_b2b = os.getenv('PASSWORD_b2b2')
auth_url = 'https://auth.cloud-test.renlife.com/auth/realms/test/protocol/openid-connect/token'
client_id = 'b2b-frontend'
body = 'grant_type=password' + '&client_id=' + client_id + '&username=' + login_b2b + '&password=' + password_b2b;
header_token_type = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}

policy_calculate_zapros = policy_calculate_zapros_api(
    breef='INVESTOR_LUMP_4.1_BASE3_113_TM_CB_UBRIR',
    b2b_user_uuid = 'e4bf4d87-c500-424f-bed6-ca2355dab7a1',
    birth_date='2000-10-10',
    ag_contract_num= 91061,
    base_sum= 30000,
    bso_series = 487,
    payment_terms= 'Единовременно',
    policy_period_brief= '3_YEARS',
    product_brief= 'INVESTOR_LUMP_4.1_BASE3_113_TM_CB',
    start_date= '2022-08-15'
)
policy_calculate_json = json.loads(policy_calculate_zapros)


def test_api_token():
    token_request = requests.post(auth_url, data=body, headers=header_token_type)
    token_request_json = json.loads(token_request.text)
    # print(token_request.text)
    # print(type(token_request))
    # print(type(token_request_json))
    # print(token_request_json['access_token'])
    access_token = token_request_json['access_token']
    return access_token



def test_policy_calculate_api():
    headers_token = {"Authorization": test_api_token()}
    # print(type(zapros))
    # print(type(parsed))
    # data = {zapros},
    # json = {zapros}
    # r = requests.post('https://gateway.cloud-test.renlife.com/api/v1/grs/rpc', data=(parsed), client_id=('grs'), client_secret=('441314ea-197d-4d2e-b693-cd002b211d55'),scope=('gateway'), grant_type=('client_credentials') )
    r = requests.post('https://gateway.cloud-test.renlife.com/api/v1/b2b/rpc', json=(policy_calculate_json), headers=headers_token)
    print(r.text)

    policy_calculate = json.loads(r.text)
    ids = policy_calculate['result']['policy']['ids']
    policy_header_id = policy_calculate['result']['policy']['policy_header_id']
    print(ids)
    print(policy_header_id)

    policy_update_info = policy_update_info_api(birth_date='2000-10-10', ids=ids, policy_header_id=policy_header_id)
    policy_update_info_json = json.loads(policy_update_info)

    r_policy_update_info = requests.post(
        'https://gateway.cloud-test.renlife.com/api/v1/b2b/rpc',
        # data=(zaebzaeb),
        json=(policy_update_info_json),
        headers=headers_token)
    print(r_policy_update_info.text)

    # # Не получается прокинуть policy_update_info - ошибка

    # policy_update = policy_update_info_api(birth_date='2000-10-10', ids=ids, policy_header_id=policy_header_id)
    # # print(policy_update)
    # # policy_update_json = json.loads(json.dumps(policy_update)).encode("utf-8")
    # policy_update_json = json.loads(json.dumps(policy_update)).encode("utf-8")
    #

    # r_policy_update_info = requests.post(
    #     'https://gateway.cloud-test.renlife.com/api/v1/b2b/rpc',
    #     data=(policy_update_json),
    #     headers=headers_token)
    # print(r_policy_update_info.text)



def test_policy_ids():
    request = '{"result":{"policy":{"guid":"E662353423F825DCE0535B0D0A0A28FA","ids":4870788670,"policy_header_id":510276621,"status_brief":"B2B_PENDING","policy_num":"4870788670","total_premium":30000,"total_fee":30000,"ins_amount":33900,"payment_term":"Единовременно","total_fee_rur":30000,"start_date":"2022-08-15T00:00:00","end_date":"2025-08-14T00:00:00","is_polling":1},"insured":[{"asset_id":40522285,"insured_type":"ASSET_PERSON","person_info":{"surname":"Фамилия","name":"Имя","midname":"Отчество","gender":"FEMALE","birth_date":"2000-10-10T00:00:00"},"fee":30000,"ins_amount":33900,"premium":30000,"programs":[{"program_name":"Дожитие Застрахованного до окончания срока действия Договора страхования","program_brief":"PEPR","program_type":"ОСН","fee":29862.96,"premium":29862.96,"ins_amount":33900,"start_date":"2022-08-15T00:00:00","end_date":"2025-08-14T00:00:00","tariff_brutto":0.8809134635562624,"tariff_netto":0.79045091187043,"tariff_loading":0.1026917573953673,"surr_sums":[{"year":1,"payment":1,"start":"2022-08-15T00:00:00","end":"2022-09-14T00:00:00","value":29862.96},{"year":1,"payment":2,"start":"2022-09-15T00:00:00","end":"2023-08-14T00:00:00","value":20411.44},{"year":2,"payment":3,"start":"2023-08-15T00:00:00","end":"2024-08-14T00:00:00","value":22998.62},{"year":3,"payment":4,"start":"2024-08-15T00:00:00","end":"2025-08-14T00:00:00","value":25795.18}]},{"program_name":"Смерть Застрахованного по любой причине","program_brief":"TERM_2","program_type":"ОБ","fee":125.29,"premium":125.29,"ins_amount":84000,"start_date":"2022-08-15T00:00:00","end_date":"2025-08-14T00:00:00","tariff_brutto":0.00149149207028859,"tariff_netto":0.0013383281284494,"tariff_loading":0.1026917573953673,"surr_sums":[{"year":1,"payment":1,"start":"2022-08-15T00:00:00","end":"2022-09-14T00:00:00","value":125.29}]},{"program_name":"Обращение Застрахованного к Страховщику/ в Сервисную компанию за помощью, требующей оказания медицинских и иных услуг","program_brief":"DMS_DD_TELEMEDICINE","program_type":"ОБ","fee":11.75,"premium":11.75,"ins_amount":3000,"start_date":"2022-08-15T00:00:00","end_date":"2023-08-14T00:00:00","tariff_brutto":0.00391608384615385,"tariff_netto":0.0025454545,"tariff_loading":0.35}]}],"save_policy":"YES","uw_grs":0},"method":"policy_calculate","id":"AC458000C1E9024AB3286EB88D321BFD","jsonrpc":"2.0"}'
    rr = json.loads(request)
    # print('__')
    # print(type(request))
    # print(type(zapros))
    # print(type(rr))
    print(rr['result']['policy']['policy_header_id'])
    ids = rr['result']['policy']['ids']
    policy_header_id = rr['result']['policy']['policy_header_id']


ydalit_na = '''	{
		"method": "policy_update_info",
		"params": {
			"insured": [{
				"addresses": [{
						"address": "Россия, г Москва, Дербеневская наб, д 7 стр 22, кв 11",
						"type": "const",
						"zip": "115114"
					},
					{
						"address": "Россия, г Москва, Дербеневская наб, д 7 стр 22, кв 11",
						"type": "fact",
						"zip": "115114"
					}
				],
				"asset_id": 40522274,
				"assignees": [],
				"assured_is_insuree": true,
				"birth_date": "2000-10-10",
				"certificates": [{
					"code": "132-001",
					"date": "2020-01-12",
					"num": "123456",
					"post": "ОВД ОКТЯБРЬСКОГО РАЙОНА Г. САРАНСКА",
					"ser": "1234",
					"type": "PASS_RF"
				}],
				"citizenships": [],
				"country_birth_alpha3": "RUS",
				"email": "w@wth.su",
				"gender": "f",
				"has_additional_citizenship": 0,
				"has_foreign_residency": 0,
				"insured_type": "ASSET_PERSON",
				"is_foreign": 0,
				"surname": "Фамилия",
				"name": "Имя",
				"midname": "Отчество",
				"pdl_list": [],
				"phones": [{
					"alfa3_code": "RUS",
					"num": "9625550123",
					"type": "MOBIL"
				}],
				"place_of_birth": "Место рождения",
				"residencies": []
			}],
			"insuree": {
				"addresses": [{
						"address": "Россия, г Москва, Дербеневская наб, д 7 стр 22, кв 11",
						"type": "const",
						"zip": "115114"
					},
					{
						"address": "Россия, г Москва, Дербеневская наб, д 7 стр 22, кв 11",
						"type": "fact",
						"zip": "115114"
					}
				],
				"birth_date": "2000-10-10",
				"certificates": [{
					"code": "132-001",
					"date": "2020-01-12",
					"num": "123456",
					"post": "ОВД ОКТЯБРЬСКОГО РАЙОНА Г. САРАНСКА",
					"ser": "1234",
					"type": "PASS_RF"
				}],
				"citizenships": [],
				"country_birth_alpha3": "RUS",
				"email": "w@wth.su",
				"gender": "f",
				"has_additional_citizenship": 0,
				"has_foreign_residency": 0,
				"is_foreign": 0,
				"surname": "Фамилия",
				"name": "Имя",
				"midname": "Отчество",
				"pdl_list": [],
				"phones": [{
					"alfa3_code": "RUS",
					"num": "9625550123",
					"type": "MOBIL"
				}],
				"place_of_birth": "фыв",
				"residencies": []
			},
			"policy": {
				"ids": 4870788818,
				"is_online": 0,
				"policy_header_id": 510279487,
				"product_brief": "INVESTOR_LUMP_4.1_BASE3_105_TM_CB"
			}
		}
	}'''

policy_update_info = policy_update_info_api(birth_date='2000-10-10', ids=4870788818, policy_header_id=510279487)
zaebzaeb = json.loads(ydalit_na)
def test_policy_policy_update_info():
    print(' ')
    # print(olicy_update_info_api)
    print(type(zaebzaeb))
    headers_token = {"Authorization": test_api_token()}
    r_policy_update_info = requests.post(
        'https://gateway.cloud-test.renlife.com/api/v1/b2b/rpc',
        # data=(zaebzaeb),
        json=(zaebzaeb),
        headers=headers_token)

    # data_to_send = json.dumps(data).encode("utf-8")
    # request_object = self.requests.put(request_ref, headers=headers, data=data_to_send)

    print(r_policy_update_info.text)



''' _________ VZNOS ________'''
min_vznos = 30000
avg_vznos = 1500000
max_vznos = 50000000


def vznos_policy_calculate_zapros_api(base_summa, dtp_risk_15kk):
    vznos_policy_calculate_zapros_api = policy_calculate_zapros_api(dtp_risk=dtp_risk_15kk,
                                                                    breef='INVESTOR_LUMP_4.1_BASE3_113_TM_CB_UBRIR',
                                                                    birth_date='2000-10-10', ag_contract_num=91061,
                                                                    base_sum=base_summa, bso_series=487,
                                                                    payment_terms='Единовременно',
                                                                    policy_period_brief='3_YEARS',
                                                                    product_brief='INVESTOR_LUMP_4.1_BASE3_113_TM_CB',
                                                                    start_date='2022-08-15',
                                                                    calc_only='YES', save_policy='NO')
    return vznos_policy_calculate_zapros_api

def policy_calculate_vznos(zapros_summa):
    headers_token = {"Authorization": test_api_token()}
    r = requests.post(
        'https://gateway.cloud-test.renlife.com/api/v1/b2b/rpc',
        json=(zapros_summa),
        headers=headers_token)
    print(r.text)
    return r.text

min_vznos_api = json.loads(vznos_policy_calculate_zapros_api(min_vznos, dtp_risk_15kk=0))
min_vznos_api_minus_001 = json.loads(vznos_policy_calculate_zapros_api(min_vznos-0.01, dtp_risk_15kk=0))
min_vznos_api_plus_001 = json.loads(vznos_policy_calculate_zapros_api(min_vznos+0.01, dtp_risk_15kk=0))

max_vznos_api = json.loads(vznos_policy_calculate_zapros_api(max_vznos, dtp_risk_15kk=1))
max_vznos_api_minus_001 = json.loads(vznos_policy_calculate_zapros_api(max_vznos-0.01, dtp_risk_15kk=1))
max_vznos_api_plus_001 = json.loads(vznos_policy_calculate_zapros_api(max_vznos+0.01, dtp_risk_15kk=1))


avg_vznos_api = json.loads(vznos_policy_calculate_zapros_api(avg_vznos, dtp_risk_15kk=0))
avg_vznos_api_minus_1_risk_off = json.loads(vznos_policy_calculate_zapros_api(avg_vznos-1, dtp_risk_15kk=0))
avg_vznos_api_plus_1_risk_off = json.loads(vznos_policy_calculate_zapros_api(avg_vznos+1, dtp_risk_15kk=0))

avg_vznos_api_risk_on = json.loads(vznos_policy_calculate_zapros_api(avg_vznos, dtp_risk_15kk=1))
avg_vznos_api_minus_1_risk_on = json.loads(vznos_policy_calculate_zapros_api(avg_vznos-1, dtp_risk_15kk=1))
avg_vznos_api_plus_1_risk_on = json.loads(vznos_policy_calculate_zapros_api(avg_vznos+1, dtp_risk_15kk=1))

''' MIN VZNOS '''
def test_policy_calculate_min_vznos():
    policy_calculate_vznos(min_vznos_api)
    assertion = json.loads(policy_calculate_vznos(min_vznos_api))
    assert assertion['result']['insured'][0]['fee'] == min_vznos

def test_policy_calculate_min_vznos_api_minus_001():
    policy_calculate_vznos(min_vznos_api_minus_001)
    assertion = json.loads(policy_calculate_vznos(min_vznos_api_minus_001))
    assert assertion['error']['data']['status'] == 'ERROR'

def test_policy_calculate_min_vznos_api_plus_001():
    policy_calculate_vznos(min_vznos_api_plus_001)
    assertion = json.loads(policy_calculate_vznos(min_vznos_api_plus_001))
    assert assertion['result']['insured'][0]['fee'] == min_vznos+0.01

''' MAX VZNOS '''
def test_policy_calculate_max_vznos():
    policy_calculate_vznos(max_vznos_api)
    assertion = json.loads(policy_calculate_vznos(max_vznos_api))
    assert assertion['result']['insured'][0]['fee'] == max_vznos

def test_policy_calculate_max_vznos_api_minus_001():
    policy_calculate_vznos(max_vznos_api_minus_001)
    assertion = json.loads(policy_calculate_vznos(max_vznos_api_minus_001))
    assert assertion['result']['insured'][0]['fee'] == max_vznos-0.01

def test_policy_calculate_max_vznos_api_plus_001():
    policy_calculate_vznos(max_vznos_api_plus_001)
    assertion = json.loads(policy_calculate_vznos(max_vznos_api_plus_001))
    assert assertion['error']['data']['status'] == 'ERROR'

''' AVG VZNOS '''
def test_policy_calculate_avg_vznos():
    policy_calculate_vznos(avg_vznos_api)
    assertion = json.loads(policy_calculate_vznos(avg_vznos_api))
    assert assertion['error']['data']['status'] == 'ERROR'

def test_policy_calculate_avg_vznos_api_minus_1_risk_off():
    policy_calculate_vznos(avg_vznos_api_minus_1_risk_off)
    assertion = json.loads(policy_calculate_vznos(avg_vznos_api_minus_1_risk_off))
    assert assertion['result']['insured'][0]['fee'] == avg_vznos - 1
    # assert assertion['error']['data']['status'] == 'ERROR'

def test_policy_calculate_avg_vznos_api_plus_1_risk_off():
    policy_calculate_vznos(avg_vznos_api_plus_1_risk_off)
    assertion = json.loads(policy_calculate_vznos(avg_vznos_api_plus_1_risk_off))
    assert assertion['error']['data']['status'] == 'ERROR'

def test_policy_calculate_avg_vznos_api_risk_on():
    policy_calculate_vznos(avg_vznos_api_risk_on)
    assertion = json.loads(policy_calculate_vznos(avg_vznos_api_risk_on))
    assert assertion['result']['insured'][0]['fee'] == avg_vznos

def test_policy_calculate_avg_vznos_api_minus_1_risk_on():
    policy_calculate_vznos(avg_vznos_api_minus_1_risk_on)
    assertion = json.loads(policy_calculate_vznos(avg_vznos_api_minus_1_risk_on))
    assert assertion['error']['data']['status'] == 'ERROR'

def test_policy_calculate_avg_vznos_api_plus_1_risk_on():
    policy_calculate_vznos(avg_vznos_api_plus_1_risk_on)
    assertion = json.loads(policy_calculate_vznos(avg_vznos_api_plus_1_risk_on))
    assert assertion['result']['insured'][0]['fee'] == avg_vznos + 1

''' __________ AGE __________ '''
import datetime
min_vozrast = 18
max_vozrast = 85

date = datetime.date.today()
year = date.year
month = date.month
if month < 10:
    month = str(0) + str(month)

day = date.day
if day < 10:
    day = str(0) + str(day)

def test_api_age(y:int = 0,d:int = 0):
    age = str(year-y) + '-' + str(month) + '-' + str(day+d)
    print(age)

def test_del_test():
    test_api_age(y=18,d=1)
    test_api_age(y=18,d=-1)

def vznos_policy_calculate_age(birth_date):
    vznos_policy_calculate_age = policy_calculate_zapros_api(dtp_risk=0,
                                                                    breef='INVESTOR_LUMP_4.1_BASE3_113_TM_CB_UBRIR',
                                                                    birth_date=birth_date, ag_contract_num=91061,
                                                                    base_sum=100000, bso_series=487,
                                                                    payment_terms='Единовременно',
                                                                    policy_period_brief='3_YEARS',
                                                                    product_brief='INVESTOR_LUMP_4.1_BASE3_113_TM_CB',
                                                                    start_date='2022-08-15',
                                                                    calc_only='YES', save_policy='NO')
    return vznos_policy_calculate_age

def policy_calculate_age(zapros_summa):
    headers_token = {"Authorization": test_api_token()}
    r = requests.post(
        'https://gateway.cloud-test.renlife.com/api/v1/b2b/rpc',
        json=(zapros_summa),
        headers=headers_token)
    print(r.text)
    return r.text

# min_age_api = json.loads(vznos_policy_calculate_zapros_api(min_vznos, dtp_risk_15kk=0))
# min_age_api = json.loads(vznos_policy_calculate_zapros_api(min_vznos, dtp_risk_15kk=0))

def test_policy_calculate_min_age():
    policy_calculate_vznos(avg_vznos_api_plus_1_risk_on)
    assertion = json.loads(policy_calculate_vznos(avg_vznos_api_plus_1_risk_on))
    assert assertion['result']['insured'][0]['fee'] == avg_vznos + 1

# def test_print():
#     print('')
#     print(zapppros)
#     # print(vznos_policy_calculate_zapros_api(30000))