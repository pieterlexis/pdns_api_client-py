# swagger_client.ConfigApi

All URIs are relative to *http://localhost:8081/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config**](ConfigApi.md#get_config) | **GET** /servers/{server_id}/config | Returns all ConfigSettings for a single server
[**get_config_setting**](ConfigApi.md#get_config_setting) | **GET** /servers/{server_id}/config/{config_setting_name} | Returns a specific ConfigSetting for a single server


# **get_config**
> list[ConfigSetting] get_config(server_id)

Returns all ConfigSettings for a single server

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
api_instance = swagger_client.ConfigApi()
server_id = 'server_id_example' # str | The id of the server to retrieve

try: 
    # Returns all ConfigSettings for a single server
    api_response = api_instance.get_config(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 

### Return type

[**list[ConfigSetting]**](ConfigSetting.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_setting**
> ConfigSetting get_config_setting(server_id, config_setting_name)

Returns a specific ConfigSetting for a single server

NOT IMPLEMENTED

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
api_instance = swagger_client.ConfigApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
config_setting_name = 'config_setting_name_example' # str | The name of the setting to retrieve

try: 
    # Returns a specific ConfigSetting for a single server
    api_response = api_instance.get_config_setting(server_id, config_setting_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_config_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **config_setting_name** | **str**| The name of the setting to retrieve | 

### Return type

[**ConfigSetting**](ConfigSetting.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

