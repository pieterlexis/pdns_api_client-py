# pdns_api_client.SearchApi

All URIs are relative to *http://localhost:8081/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_data**](SearchApi.md#search_data) | **GET** /servers/{server_id}/search-data | Search the data inside PowerDNS
[**search_log**](SearchApi.md#search_log) | **GET** /servers/{server_id}/search-log | Query the log, filtered by search_term.


# **search_data**
> SearchResults search_data(server_id, q, max)

Search the data inside PowerDNS

Search the data inside PowerDNS for search_term and return at most max_results. This includes zones, records and comments. The * character can be used in search_term as a wildcard character and the ? character can be used as a wildcard for a single character.

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
api_instance = pdns_api_client.SearchApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
q = 'q_example' # str | The string to search for
max = 56 # int | Maximum number of entries to return

try: 
    # Search the data inside PowerDNS
    api_response = api_instance.search_data(server_id, q, max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **q** | **str**| The string to search for | 
 **max** | **int**| Maximum number of entries to return | 

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_log**
> list[str] search_log(server_id, q)

Query the log, filtered by search_term.

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
api_instance = pdns_api_client.SearchApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
q = 'q_example' # str | The string to search for

try: 
    # Query the log, filtered by search_term.
    api_response = api_instance.search_log(server_id, q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **q** | **str**| The string to search for | 

### Return type

**list[str]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

