# swagger_client.ServersApi

All URIs are relative to *http://localhost:8081/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_server**](ServersApi.md#list_server) | **GET** /servers/{server_id} | List a server
[**list_servers**](ServersApi.md#list_servers) | **GET** /servers | List all servers


# **list_server**
> Server list_server(server_id)

List a server

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
swagger_client.configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ServersApi()
server_id = 'server_id_example' # str | The id of the server to retrieve

try: 
    # List a server
    api_response = api_instance.list_server(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServersApi->list_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 

### Return type

[**Server**](Server.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_servers**
> list[Server] list_servers()

List all servers

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
swagger_client.configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ServersApi()

try: 
    # List all servers
    api_response = api_instance.list_servers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServersApi->list_servers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Server]**](Server.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

