# swagger_client.CryptokeyApi

All URIs are relative to *http://localhost:8081/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_crypto_key**](CryptokeyApi.md#create_crypto_key) | **POST** /servers/{server_id}/zones/{zone_id}/cryptokeys | Creates a Cryptokey
[**delete_cryptokey**](CryptokeyApi.md#delete_cryptokey) | **DELETE** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | This method deletes a key specified by cryptokey_id.
[**list_cryptokey**](CryptokeyApi.md#list_cryptokey) | **GET** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | Returns all data about the CryptoKey, including the privatekey.
[**list_zone_crypto_keys**](CryptokeyApi.md#list_zone_crypto_keys) | **GET** /servers/{server_id}/zones/{zone_id}/cryptokeys | Get all CryptoKeys for a zone, except the privatekey
[**modify_cryptokey**](CryptokeyApi.md#modify_cryptokey) | **PUT** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | This method (de)activates a key from zone_name specified by cryptokey_id


# **create_crypto_key**
> create_crypto_key(server_id, zone_id, metadata)

Creates a Cryptokey

This method adds a new key to a zone. The key can either be generated or imported by supplying the content parameter. if content, bits and algo are null, a key will be generated based on the default-ksk-algorithm and default-ksk-size settings for a KSK and the default-zsk-algorithm and default-zsk-size options for a ZSK.

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
api_instance = swagger_client.CryptokeyApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | 
metadata = [swagger_client.Cryptokey()] # list[Cryptokey] | List of metadata to add/create

try: 
    # Creates a Cryptokey
    api_instance.create_crypto_key(server_id, zone_id, metadata)
except ApiException as e:
    print("Exception when calling CryptokeyApi->create_crypto_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**|  | 
 **metadata** | [**list[Cryptokey]**](Cryptokey.md)| List of metadata to add/create | 

### Return type

void (empty response body)

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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
swagger_client.configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CryptokeyApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve
cryptokey_id = 'cryptokey_id_example' # str | The id value of the Cryptokey

try: 
    # This method deletes a key specified by cryptokey_id.
    api_instance.delete_cryptokey(server_id, zone_id, cryptokey_id)
except ApiException as e:
    print("Exception when calling CryptokeyApi->delete_cryptokey: %s\n" % e)
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

# **list_cryptokey**
> list[Cryptokey] list_cryptokey(server_id, zone_id, cryptokey_id)

Returns all data about the CryptoKey, including the privatekey.

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
api_instance = swagger_client.CryptokeyApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve
cryptokey_id = 'cryptokey_id_example' # str | The id value of the CryptoKey

try: 
    # Returns all data about the CryptoKey, including the privatekey.
    api_response = api_instance.list_cryptokey(server_id, zone_id, cryptokey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptokeyApi->list_cryptokey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 
 **cryptokey_id** | **str**| The id value of the CryptoKey | 

### Return type

[**list[Cryptokey]**](Cryptokey.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zone_crypto_keys**
> list[Cryptokey] list_zone_crypto_keys(server_id, zone_id)

Get all CryptoKeys for a zone, except the privatekey

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
api_instance = swagger_client.CryptokeyApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | The id of the zone to retrieve

try: 
    # Get all CryptoKeys for a zone, except the privatekey
    api_response = api_instance.list_zone_crypto_keys(server_id, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptokeyApi->list_zone_crypto_keys: %s\n" % e)
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
> modify_cryptokey(server_id, zone_id, cryptokey_id)

This method (de)activates a key from zone_name specified by cryptokey_id

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
api_instance = swagger_client.CryptokeyApi()
server_id = 'server_id_example' # str | The id of the server to retrieve
zone_id = 'zone_id_example' # str | 
cryptokey_id = [swagger_client.Cryptokey()] # list[Cryptokey] | Cryptokey to manipulate

try: 
    # This method (de)activates a key from zone_name specified by cryptokey_id
    api_instance.modify_cryptokey(server_id, zone_id, cryptokey_id)
except ApiException as e:
    print("Exception when calling CryptokeyApi->modify_cryptokey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**|  | 
 **cryptokey_id** | [**list[Cryptokey]**](Cryptokey.md)| Cryptokey to manipulate | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

