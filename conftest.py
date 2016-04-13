# fixtures for pytest
import pytest
import requests
import json
import random
import csv


auth_tolken = 'Basic YWxpc3NhQHN5bXBob255Y29tbWVyY2UuY29tOnF3ZXJ0eTM3NTQ=='
headers = {
    'Accept': 'application/json',
    'content-type': 'application/json', 
    'Authorization': auth_tolken }

def pytest_addoption(parser):
    parser.addoption('--podname', action='store', default=None, required=True)


def pod_specific_base_url():
    podname = pytest.config.getvalue('podname')
    base_url = 'https://' + podname + '-partner.symphonycommerce.com'
    return base_url

def basic_simple_products():
    rand = str(random.randint(1,1000))
    url = "basic-simple" + rand

    with open('json_simple_product.json') as data_file:    
        payload = json.load(data_file)

    itr = 0
    id = ''
    ids = []
    
    with open('simple_products.csv') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            itr += 1
            if itr == 1:
                # overrides defined in first row of csv (as col headers)
                continue

            payload["publishState"] = row[0]
            payload["name"] = row[1]
            payload["msrpInCents"] = row[2]
            payload["variants"][0]["name"] = row[3]
            payload["productPricing"][0]["label"] = row[4]
            payload["productPricing"][0]["price"] = row[5]
            payload["productPricing"][0]["availability"] = row[6]
            payload["productPricing"][1]["label"] = row[7]
            payload["productPricing"][1]["price"] = row[8]
            payload["productPricing"][1]["availability"] = row[9]
            payload["productPricing"][2]["label"] = row[10]
            payload["productPricing"][2]["price"] = row[11]
            payload["productPricing"][2]["availability"] = row[12]

            base_url = pod_specific_base_url()
            resp = requests.request('POST', base_url + '/org/kittydemo/api/v1/productcluster', headers = headers, json = payload)
    
            id = str(resp.json()['id'])`
            ids.append(id)   
    return ids

def simple_product_variant_pricing():
    rand = str(random.randint(1,1000))
    url = "simple-variant-pricing" + rand

    with open('json_simple_with_variant_pricing.json') as data_file:    
        payload = json.load(data_file)
    
    base_url = pod_specific_base_url()
    resp = requests.request('POST', base_url + '/org/kittydemo/api/v1/productcluster', headers = headers, json = payload)
    
    # print json.dumps(resp.json()['id'], indent = 2, sort_keys = True)
    id = str(resp.json()['id'])
    print id
    return id

@pytest.fixture
def env_headers():
    return headers

@pytest.fixture
def env_base_url():
    return pod_specific_base_url()

@pytest.fixture
def simple_products():
    return basic_simple_products()

@pytest.fixture
def simple_product_with_variant_pricing():
    return simple_product_variant_pricing()





"""
# JUST SOME JUNK I DONT HAVE THE HEART TO DELETE YET
    
@pytest.fixture
def existing_product():
    id = str(166936)
    return id
    
@pytest.fixture
def non_existing_product():
    id = str(9999999999)
    return id
    
@pytest.fixture
def valid_pc2archive():
    return simple_product()
   
@pytest.fixture
def multiple_valid_pc2archive():
    products_str = ''
    for p in range(5):
        products_str += products_str + ',' + simple_product()
    print products_str
    return products_str
    
@pytest.fixture
def invalid_pc2archive():
    id = str(9999999999)
    return id

"""

    
    