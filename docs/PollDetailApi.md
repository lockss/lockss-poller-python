# lockss_poller.PollDetailApi

All URIs are relative to *https://laaws.lockss.org:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_poll_peer_vote_urls**](PollDetailApi.md#get_poll_peer_vote_urls) | **GET** /polls/{pollKey}/peer/{peerId} | Poll Peer Data
[**get_repair_queue_data**](PollDetailApi.md#get_repair_queue_data) | **GET** /polls/{pollKey}/repairs | Poll Repairs
[**get_tally_urls**](PollDetailApi.md#get_tally_urls) | **GET** /polls/{pollKey}/tallies | Page Tally


# **get_poll_peer_vote_urls**
> UrlPager get_poll_peer_vote_urls(poll_key, peer_id, urls, page=page, size=size)

Poll Peer Data

### Example
```python
from __future__ import print_function
import time
import lockss_poller
from lockss_poller.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = lockss_poller.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lockss_poller.PollDetailApi(lockss_poller.ApiClient(configuration))
poll_key = 'poll_key_example' # str | The pollKey from the PollDetail.
peer_id = 'peer_id_example' # str | The peerId from the Poll Detail.PeerData.
urls = 'urls_example' # str | The voter urls to return.
page = 56 # int | The page number (optional)
size = 56 # int | The page size (optional)

try:
    # Poll Peer Data
    api_response = api_instance.get_poll_peer_vote_urls(poll_key, peer_id, urls, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PollDetailApi->get_poll_peer_vote_urls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_key** | **str**| The pollKey from the PollDetail. | 
 **peer_id** | **str**| The peerId from the Poll Detail.PeerData. | 
 **urls** | **str**| The voter urls to return. | 
 **page** | **int**| The page number | [optional] 
 **size** | **int**| The page size | [optional] 

### Return type

[**UrlPager**](UrlPager.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repair_queue_data**
> RepairPager get_repair_queue_data(poll_key, repair, page=page, size=size)

Poll Repairs

### Example
```python
from __future__ import print_function
import time
import lockss_poller
from lockss_poller.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = lockss_poller.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lockss_poller.PollDetailApi(lockss_poller.ApiClient(configuration))
poll_key = 'poll_key_example' # str | The pollKey as listed in the PollDetail object.
repair = 'repair_example' # str | The repair queue elements to return.
page = 56 # int | The page number. (optional)
size = 56 # int | The size of the page. (optional)

try:
    # Poll Repairs
    api_response = api_instance.get_repair_queue_data(poll_key, repair, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PollDetailApi->get_repair_queue_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_key** | **str**| The pollKey as listed in the PollDetail object. | 
 **repair** | **str**| The repair queue elements to return. | 
 **page** | **int**| The page number. | [optional] 
 **size** | **int**| The size of the page. | [optional] 

### Return type

[**RepairPager**](RepairPager.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tally_urls**
> UrlPager get_tally_urls(poll_key, tally, page=page, size=size)

Page Tally

### Example
```python
from __future__ import print_function
import time
import lockss_poller
from lockss_poller.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = lockss_poller.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lockss_poller.PollDetailApi(lockss_poller.ApiClient(configuration))
poll_key = 'poll_key_example' # str | The pollKey as listed in the PollDetail object.
tally = 'tally_example' # str | The kind of tally element to return.
page = 56 # int | The page number. (optional)
size = 56 # int | The size of the page. (optional)

try:
    # Page Tally
    api_response = api_instance.get_tally_urls(poll_key, tally, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PollDetailApi->get_tally_urls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_key** | **str**| The pollKey as listed in the PollDetail object. | 
 **tally** | **str**| The kind of tally element to return. | 
 **page** | **int**| The page number. | [optional] 
 **size** | **int**| The size of the page. | [optional] 

### Return type

[**UrlPager**](UrlPager.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

