# swagger_client.ZonemetadataApi

All URIs are relative to *http://localhost:8081/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_zone_metadata**](ZonemetadataApi.md#create_zone_metadata) | **POST** /servers/{server_id}/zones/{zone_id}/metadata | Creates a set of metadata entries
[**delete_zone_metadata_kind**](ZonemetadataApi.md#delete_zone_metadata_kind) | **DELETE** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Delete all items of a single kind of domain metadata.
[**list_zone_metadata**](ZonemetadataApi.md#list_zone_metadata) | **GET** /servers/{server_id}/zones/{zone_id}/metadata | Get all the MetaData associated with the zone.
[**list_zone_metadata_kind**](ZonemetadataApi.md#list_zone_metadata_kind) | **GET** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Get the content of a single kind of domain metadata as a list of MetaData objects.
[**modify_zone_metadata_kind**](ZonemetadataApi.md#modify_zone_metadata_kind) | **PUT** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Modify the content of a single kind of domain metadata.


# **create_zone_metadata**
> create_zone_metadata(server_id, zone_id, metadata)

Creates a set of metadata entries

Creates a set of metadata entries of given kind for the zone. Existing metadata entries for the zone with the same kind are not overwritten.

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
api_instance = swagger_client.ZonemetadataApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | 
metadata = [swagger_client.Metadata()] # list[Metadata] | List of metadata to add/create

try: 
    # Creates a set of metadata entries
    api_instance.create_zone_metadata(server_id, zone_id, metadata)
except ApiException as e:
    print("Exception when calling ZonemetadataApi->create_zone_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**|  | 
 **metadata** | [**list[Metadata]**](Metadata.md)| List of metadata to add/create | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone_metadata_kind**
> delete_zone_metadata_kind(server_id, zone_id, metadata_kind)

Delete all items of a single kind of domain metadata.

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
api_instance = swagger_client.ZonemetadataApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve
metadata_kind = 'metadata_kind_example' # str | ???

try: 
    # Delete all items of a single kind of domain metadata.
    api_instance.delete_zone_metadata_kind(server_id, zone_id, metadata_kind)
except ApiException as e:
    print("Exception when calling ZonemetadataApi->delete_zone_metadata_kind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 
 **metadata_kind** | **str**| ??? | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zone_metadata**
> list[Metadata] list_zone_metadata(server_id, zone_id)

Get all the MetaData associated with the zone.

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
api_instance = swagger_client.ZonemetadataApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve

try: 
    # Get all the MetaData associated with the zone.
    api_response = api_instance.list_zone_metadata(server_id, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonemetadataApi->list_zone_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zone_metadata_kind**
> list[Metadata] list_zone_metadata_kind(server_id, zone_id, metadata_kind)

Get the content of a single kind of domain metadata as a list of MetaData objects.

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
api_instance = swagger_client.ZonemetadataApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve
metadata_kind = 'metadata_kind_example' # str | ???

try: 
    # Get the content of a single kind of domain metadata as a list of MetaData objects.
    api_response = api_instance.list_zone_metadata_kind(server_id, zone_id, metadata_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonemetadataApi->list_zone_metadata_kind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 
 **metadata_kind** | **str**| ??? | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_zone_metadata_kind**
> modify_zone_metadata_kind(server_id, zone_id, metadata)

Modify the content of a single kind of domain metadata.

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
api_instance = swagger_client.ZonemetadataApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | 
metadata = [swagger_client.Metadata()] # list[Metadata] | List of metadata to add/create

try: 
    # Modify the content of a single kind of domain metadata.
    api_instance.modify_zone_metadata_kind(server_id, zone_id, metadata)
except ApiException as e:
    print("Exception when calling ZonemetadataApi->modify_zone_metadata_kind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**|  | 
 **metadata** | [**list[Metadata]**](Metadata.md)| List of metadata to add/create | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

