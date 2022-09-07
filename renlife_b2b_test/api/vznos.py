

def assert_vznos_passed(response):
    return response['result']['insured'][0]['fee']

def asser_vznos_error(response):
    return response['error']['data']['status'] == 'ERROR'