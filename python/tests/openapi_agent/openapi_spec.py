import json

from pytest_httpserver import HTTPServer

from gpt.openapi_agent.openapi import reduce_openapi_spec


TEST_OPENAPI_SPEC_JSON = """{"openapi":"3.0.1","info":{"title":"OpenAPI definition","version":"v0"},"servers":[{"url":"SERVER_URL","description":"Generated server url"}],"paths":{"/api/customers":{"get":{"tags":["customer-controller"],"summary":"Get list of customers (Ordered by Id in ascending order), you must specify page number and page size","operationId":"getcustomers","parameters":[{"name":"page","in":"query","description":"Page index (start from 0)","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"pageSize","in":"query","description":"Number of records per page","required":true,"schema":{"type":"integer","format":"int32"}}],"responses":{"200":{"description":"Successful Operation","content":{"application/json":{}}},"400":{"description":"Invalid parameters supplied"},"500":{"description":"Internal Error"}}},"post":{"tags":["customer-controller"],"summary":"Create a new customer","operationId":"createcustomer","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/components/schemas/Customer"}}},"required":true},"responses":{"409":{"description":"Duplicate customer name"},"201":{"description":"customer created","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Customer"}}}},"400":{"description":"Invalid id supplied"},"500":{"description":"Internal Error"},"404":{"description":"customer not found"}}}},"/api/customers/{customerId}":{"get":{"tags":["customer-controller"],"summary":"Get a customer by its id","operationId":"getcustomerById","parameters":[{"name":"customerId","in":"path","description":"id of customer to be retrieved","required":true,"schema":{"type":"integer","format":"int32"}}],"responses":{"200":{"description":"Found the customer","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Customer"}}}},"400":{"description":"Invalid id supplied"},"500":{"description":"Internal Error"},"404":{"description":"customer not found"}}},"delete":{"tags":["customer-controller"],"summary":"Delete a customer by its id","operationId":"deletecustomer","parameters":[{"name":"customerId","in":"path","description":"id of customer to be deleted","required":true,"schema":{"type":"integer","format":"int32"}}],"responses":{"202":{"description":"customer deleted"},"400":{"description":"Invalid id supplied"},"500":{"description":"Internal Error"},"404":{"description":"customer not found"}}},"patch":{"tags":["customer-controller"],"summary":"Update a customer by its id","operationId":"updatecustomer","parameters":[{"name":"customerId","in":"path","description":"id of customer to be updated","required":true,"schema":{"type":"integer","format":"int32"}}],"requestBody":{"content":{"application/json":{"schema":{"$ref":"#/components/schemas/Customer"}}},"required":true},"responses":{"409":{"description":"Duplicate customer name"},"202":{"description":"customer updated","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Customer"}}}},"400":{"description":"Invalid id supplied"},"500":{"description":"Internal Error"},"404":{"description":"customer not found"}}}}},"components":{"schemas":{"Customer":{"type":"object","properties":{"firstname":{"type":"string"},"lastname":{"type":"string"},"email":{"type":"string"},"phone":{"type":"string"},"lastUpdate":{"type":"string","format":"date-time"},"id":{"type":"integer","format":"int32"},"links":{"type":"array","items":{"$ref":"#/components/schemas/Link"}}}},"Link":{"type":"object","properties":{"rel":{"type":"string"},"href":{"type":"string"},"hreflang":{"type":"string"},"media":{"type":"string"},"title":{"type":"string"},"type":{"type":"string"},"deprecation":{"type":"string"},"profile":{"type":"string"},"name":{"type":"string"}}}}}}"""


def get_test_api_spec_for_url(base_url: str):
    return reduce_openapi_spec(
        json.loads(TEST_OPENAPI_SPEC_JSON.replace("SERVER_URL", base_url.removesuffix("/")))
    )


def get_test_api_spec(httpserver: HTTPServer):
    return get_test_api_spec_for_url(httpserver.url_for('').removesuffix("/"))
