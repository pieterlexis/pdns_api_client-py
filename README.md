# pdns_api_client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.12
- Package version: 0.0.10.2
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/pieterlexis/pdns_api_client-py.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/pieterlexis/pdns_api_client-py.git`)

Then import the package:
```python
import pdns_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pdns_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = pdns_api_client.ConfigApi()
server_id = 'server_id_example' # str | The id of the server to retrieve

try:
    # Returns all ConfigSettings for a single server
    api_response = api_instance.get_config(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_config: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8081/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConfigApi* | [**get_config**](docs/ConfigApi.md#get_config) | **GET** /servers/{server_id}/config | Returns all ConfigSettings for a single server
*ConfigApi* | [**get_config_setting**](docs/ConfigApi.md#get_config_setting) | **GET** /servers/{server_id}/config/{config_setting_name} | Returns a specific ConfigSetting for a single server
*SearchApi* | [**search_data**](docs/SearchApi.md#search_data) | **GET** /servers/{server_id}/search-data | Search the data inside PowerDNS
*SearchApi* | [**search_log**](docs/SearchApi.md#search_log) | **GET** /servers/{server_id}/search-log | Query the log, filtered by search_term.
*ServersApi* | [**list_server**](docs/ServersApi.md#list_server) | **GET** /servers/{server_id} | List a server
*ServersApi* | [**list_servers**](docs/ServersApi.md#list_servers) | **GET** /servers | List all servers
*StatsApi* | [**get_stats**](docs/StatsApi.md#get_stats) | **GET** /servers/{server_id}/statistics | Query statistics.
*ZonecryptokeyApi* | [**create_cryptokey**](docs/ZonecryptokeyApi.md#create_cryptokey) | **POST** /servers/{server_id}/zones/{zone_id}/cryptokeys | Creates a Cryptokey
*ZonecryptokeyApi* | [**delete_cryptokey**](docs/ZonecryptokeyApi.md#delete_cryptokey) | **DELETE** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | This method deletes a key specified by cryptokey_id.
*ZonecryptokeyApi* | [**list_cryptokey**](docs/ZonecryptokeyApi.md#list_cryptokey) | **GET** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | Returns all data about the CryptoKey, including the privatekey.
*ZonecryptokeyApi* | [**list_cryptokeys**](docs/ZonecryptokeyApi.md#list_cryptokeys) | **GET** /servers/{server_id}/zones/{zone_id}/cryptokeys | Get all CryptoKeys for a zone, except the privatekey
*ZonecryptokeyApi* | [**modify_cryptokey**](docs/ZonecryptokeyApi.md#modify_cryptokey) | **PUT** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | This method (de)activates a key from zone_name specified by cryptokey_id
*ZonemetadataApi* | [**create_metadata**](docs/ZonemetadataApi.md#create_metadata) | **POST** /servers/{server_id}/zones/{zone_id}/metadata | Creates a set of metadata entries
*ZonemetadataApi* | [**delete_metadata**](docs/ZonemetadataApi.md#delete_metadata) | **DELETE** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Delete all items of a single kind of domain metadata.
*ZonemetadataApi* | [**get_metadata**](docs/ZonemetadataApi.md#get_metadata) | **GET** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Get the content of a single kind of domain metadata as a list of MetaData objects.
*ZonemetadataApi* | [**list_metadata**](docs/ZonemetadataApi.md#list_metadata) | **GET** /servers/{server_id}/zones/{zone_id}/metadata | Get all the MetaData associated with the zone.
*ZonemetadataApi* | [**modify_metadata**](docs/ZonemetadataApi.md#modify_metadata) | **PUT** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Modify the content of a single kind of domain metadata.
*ZonesApi* | [**axfr_export_zone**](docs/ZonesApi.md#axfr_export_zone) | **GET** /servers/{server_id}/zones/{zone_id}/export | Returns the zone in AXFR format.
*ZonesApi* | [**axfr_retrieve_zone**](docs/ZonesApi.md#axfr_retrieve_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/axfr-retrieve | Send a DNS NOTIFY to all slaves.
*ZonesApi* | [**check_zone**](docs/ZonesApi.md#check_zone) | **GET** /servers/{server_id}/zones/{zone_id}/check | Verify zone contents/configuration.
*ZonesApi* | [**create_zone**](docs/ZonesApi.md#create_zone) | **POST** /servers/{server_id}/zones | Creates a new domain, returns the Zone on creation.
*ZonesApi* | [**delete_zone**](docs/ZonesApi.md#delete_zone) | **DELETE** /servers/{server_id}/zones/{zone_id} | Deletes this zone, all attached metadata and rrsets.
*ZonesApi* | [**list_zone**](docs/ZonesApi.md#list_zone) | **GET** /servers/{server_id}/zones/{zone_id} | zone managed by a server
*ZonesApi* | [**list_zones**](docs/ZonesApi.md#list_zones) | **GET** /servers/{server_id}/zones | List all Zones in a server
*ZonesApi* | [**notify_zone**](docs/ZonesApi.md#notify_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/notify | Send a DNS NOTIFY to all slaves.
*ZonesApi* | [**patch_zone**](docs/ZonesApi.md#patch_zone) | **PATCH** /servers/{server_id}/zones/{zone_id} | Modifies present RRsets and comments. Returns 204 No Content on success.
*ZonesApi* | [**put_zone**](docs/ZonesApi.md#put_zone) | **PUT** /servers/{server_id}/zones/{zone_id} | Modifies basic zone data (metadata).
*ZonesApi* | [**rectify_zone**](docs/ZonesApi.md#rectify_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/rectify | Rectify the zone data.


## Documentation For Models

 - [Comment](docs/Comment.md)
 - [ConfigSetting](docs/ConfigSetting.md)
 - [Cryptokey](docs/Cryptokey.md)
 - [Metadata](docs/Metadata.md)
 - [RRSet](docs/RRSet.md)
 - [Record](docs/Record.md)
 - [SearchResult](docs/SearchResult.md)
 - [SearchResultComment](docs/SearchResultComment.md)
 - [SearchResultRecord](docs/SearchResultRecord.md)
 - [SearchResultZone](docs/SearchResultZone.md)
 - [SearchResults](docs/SearchResults.md)
 - [Server](docs/Server.md)
 - [Servers](docs/Servers.md)
 - [StatisticItem](docs/StatisticItem.md)
 - [Zone](docs/Zone.md)
 - [Zones](docs/Zones.md)


## Documentation For Authorization


## APIKeyHeader

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header


## Author



