import json
from renlife_b2b_test.path_to_directory import filename


def create_data_policy_calculate(policy_header_id, ids, uuid):
    print('')
    # policy_calculate = json.loads(r.text)
    # ids = policy_calculate['result']['policy']['ids']
    # uuid = jwt_decode(test_api_token_session)
    policy_header_id = 510294507
    ids = 4870789508
    uuid = 'e4bf4d87-c500-424f-bed6-ca2355dab7a1'
    pers_data = {'policy_header_id':policy_header_id, 'ids':ids,  'uuid':uuid}
    f = open(filename()+"/policy_calculate.json", "w")
    f.write(json.dumps(pers_data))

def read_data_create_data_policy_calculate():
    with open(filename()+"/policy_calculate.json") as file:
        int_number = file.read()
        # print(int_number)
    return (json.loads(int_number))

