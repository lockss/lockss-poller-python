# lockss_poller.ServiceApi

All URIs are relative to *https://laaws.lockss.org:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_poll**](ServiceApi.md#call_poll) | **POST** /polls | Send a request to call a poll to the poller
[**cancel_poll**](ServiceApi.md#cancel_poll) | **DELETE** /polls/{psId} | Stop a poll and remove from queue.
[**get_poll_status**](ServiceApi.md#get_poll_status) | **GET** /polls/{psId} | Get queued poll status
[**get_status**](ServiceApi.md#get_status) | **GET** /status | Get the status of the service


# **call_poll**
> str call_poll(body)

Send a request to call a poll to the poller

Use the information found in the descriptor object to initiate a  poll.

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
api_instance = lockss_poller.ServiceApi(lockss_poller.ApiClient(configuration))
body = lockss_poller.PollDesc() # PollDesc | 

try:
    # Send a request to call a poll to the poller
    api_response = api_instance.call_poll(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->call_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PollDesc**](PollDesc.md)|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_poll**
> cancel_poll(ps_id)

Stop a poll and remove from queue.

Stop a running poll and delete any schecduled polls for poll with the poll service id.

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
api_instance = lockss_poller.ServiceApi(lockss_poller.ApiClient(configuration))
ps_id = 'ps_id_example' # str | 

try:
    # Stop a poll and remove from queue.
    api_instance.cancel_poll(ps_id)
except ApiException as e:
    print("Exception when calling ServiceApi->cancel_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ps_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_poll_status**
> PollerSummary get_poll_status(ps_id)

Get queued poll status

Get the status of a previously queued poll.

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
api_instance = lockss_poller.ServiceApi(lockss_poller.ApiClient(configuration))
ps_id = 'ps_id_example' # str | 

try:
    # Get queued poll status
    api_response = api_instance.get_poll_status(ps_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->get_poll_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ps_id** | **str**|  | 

### Return type

[**PollerSummary**](PollerSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> ApiStatus get_status()

Get the status of the service

Get the status of the service

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
api_instance = lockss_poller.ServiceApi(lockss_poller.ApiClient(configuration))

try:
    # Get the status of the service
    api_response = api_instance.get_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiStatus**](ApiStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

