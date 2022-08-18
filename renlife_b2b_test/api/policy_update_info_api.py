import json


def policy_update_info_api(
	birth_date: str = '2000-10-10',
	ids: int = None,
	policy_header_id: int = None,
	product_brief: str = 'INVESTOR_LUMP_4.1_BASE3_105_TM_CB'):
	policy_update_info = '''
	{
		"method": "policy_update_info",
		"params": {
			"insured": [
				{
					"addresses": [
						{
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
					"birth_date": "''' + birth_date + '''",
					"certificates": [
						{
							"code": "132-001",
							"date": "2020-01-12",
							"num": "123456",
							"post": "ОВД ОКТЯБРЬСКОГО РАЙОНА Г. САРАНСКА",
							"ser": "1234",
							"type": "PASS_RF"
						}
					],
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
					"phones": [
						{
							"alfa3_code": "RUS",
							"num": "9625550123",
							"type": "MOBIL"
						}
					],
					"place_of_birth": "Место рождения",
					"residencies": []
				}
			],
			"insuree": {
				"addresses": [
					{
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
				"birth_date": "''' + birth_date + '''",
				"certificates": [
					{
						"code": "132-001",
						"date": "2020-01-12",
						"num": "123456",
						"post": "ОВД ОКТЯБРЬСКОГО РАЙОНА Г. САРАНСКА",
						"ser": "1234",
						"type": "PASS_RF"
					}
				],
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
				"phones": [
					{
						"alfa3_code": "RUS",
						"num": "9625550123",
						"type": "MOBIL"
					}
				],
				"place_of_birth": "фыв",
				"residencies": []
			},
			"policy": {
				"ids": ''' + str(ids) + ''',
				"is_online": 0,
				"policy_header_id": ''' + str(policy_header_id) + ''',
				"product_brief": "''' + product_brief + '''"
			}
		}
	}'''
	return policy_update_info

def test_priny():
	print(
			policy_update_info_api(
				birth_date='2000-10-10',
				ids=510276621,
				policy_header_id=510276621,
				product_brief = 'INVESTOR_LUMP_4.1_BASE3_105_TM_CB'
			))