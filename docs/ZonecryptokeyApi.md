# pdns_api_client.ZonecryptokeyApi

All URIs are relative to *http://localhost:8081/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cryptokey**](ZonecryptokeyApi.md#create_cryptokey) | **POST** /servers/{server_id}/zones/{zone_id}/cryptokeys | Creates a Cryptokey
[**delete_cryptokey**](ZonecryptokeyApi.md#delete_cryptokey) | **DELETE** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | This method deletes a key specified by cryptokey_id.
[**get_cryptokey**](ZonecryptokeyApi.md#get_cryptokey) | **GET** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | Returns all data about the CryptoKey, including the privatekey.
[**list_cryptokeys**](ZonecryptokeyApi.md#list_cryptokeys) | **GET** /servers/{server_id}/zones/{zone_id}/cryptokeys | Get all CryptoKeys for a zone, except the privatekey
[**modify_cryptokey**](ZonecryptokeyApi.md#modify_cryptokey) | **PUT** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | This method (de)activates a key from zone_name specified by cryptokey_id


# **create_cryptokey**
> Cryptokey create_cryptokey(server_id, zone_id, cryptokey)

Creates a Cryptokey

This method adds a new key to a zone. The key can either be generated or imported by supplying the content parameter. if content, bits and algo are null, a key will be generated based on the default-ksk-algorithm and default-ksk-size settings for a KSK and the default-zsk-algorithm and default-zsk-size options for a ZSK.

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
api_instance = pdns_api_client.ZonecryptokeyApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | 
cryptokey = pdns_api_client.Cryptokey() # Cryptokey | Add a Cryptokey

try: 
    # Creates a Cryptokey
    api_response = api_instance.create_cryptokey(server_id, zone_id, cryptokey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonecryptokeyApi->create_cryptokey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**|  | 
 **cryptokey** | [**Cryptokey**](Cryptokey.md)| Add a Cryptokey | 

### Return type

[**Cryptokey**](Cryptokey.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cryptokey**
> delete_cryptokey(server_id, zone_id, cryptokey_id)

This method deletes a key specified by cryptokey_id.

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
api_instance = pdns_api_client.ZonecryptokeyApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve
cryptokey_id = 'cryptokey_id_example' # str | The id value of the Cryptokey

try: 
    # This method deletes a key specified by cryptokey_id.
    api_instance.delete_cryptokey(server_id, zone_id, cryptokey_id)
except ApiException as e:
    print("Exception when calling ZonecryptokeyApi->delete_cryptokey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 
 **cryptokey_id** | **str**| The id value of the Cryptokey | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cryptokey**
> Cryptokey get_cryptokey(server_id, zone_id, cryptokey_id)

Returns all data about the CryptoKey, including the privatekey.

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
api_instance = pdns_api_client.ZonecryptokeyApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve
cryptokey_id = 'cryptokey_id_example' # str | The id value of the CryptoKey

try: 
    # Returns all data about the CryptoKey, including the privatekey.
    api_response = api_instance.get_cryptokey(server_id, zone_id, cryptokey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonecryptokeyApi->get_cryptokey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 
 **cryptokey_id** | **str**| The id value of the CryptoKey | 

### Return type

[**Cryptokey**](Cryptokey.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cryptokeys**
> list[Cryptokey] list_cryptokeys(server_id, zone_id)

Get all CryptoKeys for a zone, except the privatekey

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
api_instance = pdns_api_client.ZonecryptokeyApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve

try: 
    # Get all CryptoKeys for a zone, except the privatekey
    api_response = api_instance.list_cryptokeys(server_id, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonecryptokeyApi->list_cryptokeys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

### Return type

[**list[Cryptokey]**](Cryptokey.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_cryptokey**
> modify_cryptokey(server_id, zone_id, cryptokey_id, cryptokey)

This method (de)activates a key from zone_name specified by cryptokey_id

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
api_instance = pdns_api_client.ZonecryptokeyApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | 
cryptokey_id = 'cryptokey_id_example' # str | Cryptokey to manipulate
cryptokey = pdns_api_client.Cryptokey() # Cryptokey | the Cryptokey

try: 
    # This method (de)activates a key from zone_name specified by cryptokey_id
    api_instance.modify_cryptokey(server_id, zone_id, cryptokey_id, cryptokey)
except ApiException as e:
    print("Exception when calling ZonecryptokeyApi->modify_cryptokey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**|  | 
 **cryptokey_id** | **str**| Cryptokey to manipulate | 
 **cryptokey** | [**Cryptokey**](Cryptokey.md)| the Cryptokey | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

