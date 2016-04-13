import requests
import json
from urllib import urlencode

def test_pod_is_up(env_headers, env_base_url):
    params = {'email': 'alissa@symphonycommerce.com', 'password': 'qwerty3754'}
    url_params = urlencode(params)
    headers = {'Accept': 'application/json'}
    resp = requests.request('POST', env_base_url + '/auth/email/login', params = url_params, headers = headers)
    assert resp.status_code == 200

def test_basic_simple_products_created(env_headers, env_base_url, simple_products):
    product_ids = simple_products
    for p in range(len(product_ids)):
        resp = requests.request('GET', env_base_url + '/org/kittydemo/api/v1/productcluster/' + product_ids[p] +'/product', headers = env_headers)
        assert resp.status_code == 200

def test_simple_product_with_variant_pricing_created(env_headers, env_base_url, simple_product_with_variant_pricing):
    resp = requests.request('GET', env_base_url + '/org/kittydemo/api/v1/productcluster/' + simple_product_with_variant_pricing +'/product', headers = env_headers)
    assert resp.status_code == 200




"""
# SOME COMPLIMENTARY JUNK I DONT HAVE THE HEART TO DELETE YET

def test_get_non_existing_product(non_existing_product):
    resp = requests.request('GET', base_url + '/productcluster/' + non_existing_product +'/product', headers = headers)
    assert resp.status_code == 200
    
def test_get_exiting_product(existing_product):
    resp = requests.request('GET', base_url + '/productcluster/' + existing_product + '/product', headers = headers)
    assert resp.status_code == 200
    # print json.dumps(resp.json(), indent = 2, sort_keys = True)

      
def test_archive_existing_product(valid_pc2archive):
    resp = requests.request('GET', base_url + '/productcluster/archive?ids=' + valid_pc2archive, headers = headers)
    assert resp.status_code == 200
    
def test_archive_multiple_existing_product(multiple_valid_pc2archive):
    resp = requests.request('GET', base_url + '/productcluster/archive?ids=' + multiple_valid_pc2archive, headers = headers)
    print base_url + '/productcluster/archive?ids=' + multiple_valid_pc2archive
    assert resp.status_code == 200


def test_archive_non_existing_product(invalid_pc2archive):
    resp = requests.request('GET', base_url + '/productcluster/archive?ids=' + invalid_pc2archive, headers = headers)
    assert resp.status_code == 200

"""
