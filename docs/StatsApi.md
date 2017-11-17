# pdns_api_client.StatsApi

All URIs are relative to *http://localhost:8081/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stats**](StatsApi.md#get_stats) | **GET** /servers/{server_id}/statistics | Query statistics.


# **get_stats**
> list[StatisticItem] get_stats(server_id)

Query statistics.

Query PowerDNS internal statistics. Returns a list of StatisticItem elements.

### Example 
```python
from __future__ import print_function
import time
import pdns_api_client
from pdns_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
pdns_api_client.configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# pdns_api_client.configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = pdns_api_client.StatsApi()
server_id = 'server_id_example' # str | The id of the server to retrieve

try: 
    # Query statistics.
    api_response = api_instance.get_stats(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 

### Return type

[**list[StatisticItem]**](StatisticItem.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

