# lockss_poller.PollerPollsApi

All URIs are relative to *https://laaws.lockss.org:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_poller_poll_details**](PollerPollsApi.md#get_poller_poll_details) | **GET** /polls/poller/{pollKey} | PollerDetails
[**get_polls_as_poller**](PollerPollsApi.md#get_polls_as_poller) | **GET** /polls/poller | Get the list of recent polls as poller.


# **get_poller_poll_details**
> PollerDetail get_poller_poll_details(poll_key)

PollerDetails

Return the detailed information about a poll.

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
api_instance = lockss_poller.PollerPollsApi(lockss_poller.ApiClient(configuration))
poll_key = 'poll_key_example' # str | The key assigned by the PollManager.

try:
    # PollerDetails
    api_response = api_instance.get_poller_poll_details(poll_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PollerPollsApi->get_poller_poll_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_key** | **str**| The key assigned by the PollManager. | 

### Return type

[**PollerDetail**](PollerDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_polls_as_poller**
> PollerPager get_polls_as_poller(size=size, page=page)

Get the list of recent polls as poller.

Get the list of recent polls as poller from the poll queue. if size and page are passed in use those arguments to limit return data.

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
api_instance = lockss_poller.PollerPollsApi(lockss_poller.ApiClient(configuration))
size = 10 # int | Size of the page to retrieve. (optional)
page = 1 # int | Number of the page to retrieve. (optional)

try:
    # Get the list of recent polls as poller.
    api_response = api_instance.get_polls_as_poller(size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PollerPollsApi->get_polls_as_poller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Size of the page to retrieve. | [optional] 
 **page** | **int**| Number of the page to retrieve. | [optional] 

### Return type

[**PollerPager**](PollerPager.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

