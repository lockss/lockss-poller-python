# lockss_poller.VoterPollsApi

All URIs are relative to *https://laaws.lockss.org:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_polls_as_voter**](VoterPollsApi.md#get_polls_as_voter) | **GET** /polls/voter | Get the list of recent voter only polls.
[**get_voter_poll_details**](VoterPollsApi.md#get_voter_poll_details) | **GET** /polls/voter/{pollKey} | VoterDetails


# **get_polls_as_voter**
> VoterPager get_polls_as_voter(size=size, page=page)

Get the list of recent voter only polls.

Get the list of recent polls as voter from the poll queue. if size and page are passed in use those arguments to limit return data.

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
api_instance = lockss_poller.VoterPollsApi(lockss_poller.ApiClient(configuration))
size = 10 # int | Size of the page to retrieve. (optional)
page = 1 # int | Number of the page to retrieve. (optional)

try:
    # Get the list of recent voter only polls.
    api_response = api_instance.get_polls_as_voter(size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoterPollsApi->get_polls_as_voter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Size of the page to retrieve. | [optional] 
 **page** | **int**| Number of the page to retrieve. | [optional] 

### Return type

[**VoterPager**](VoterPager.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voter_poll_details**
> VoterDetail get_voter_poll_details(poll_key)

VoterDetails

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
api_instance = lockss_poller.VoterPollsApi(lockss_poller.ApiClient(configuration))
poll_key = 'poll_key_example' # str | The key assigned by the PollManager.

try:
    # VoterDetails
    api_response = api_instance.get_voter_poll_details(poll_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoterPollsApi->get_voter_poll_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_key** | **str**| The key assigned by the PollManager. | 

### Return type

[**VoterDetail**](VoterDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

