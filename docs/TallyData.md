# TallyData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_agree** | **int** | The number of urls with agreement. | 
**agree_link** | [**LinkDesc**](LinkDesc.md) |  | [optional] 
**num_disagree** | **int** | The number of urls with disagreement. | 
**disagree_link** | [**LinkDesc**](LinkDesc.md) |  | [optional] 
**num_too_close** | **int** | The number of urls too close. | 
**too_close_link** | [**LinkDesc**](LinkDesc.md) |  | [optional] 
**num_no_quorum** | **int** | The number of urls without enough voters. | 
**no_quorum_link** | [**LinkDesc**](LinkDesc.md) |  | [optional] 
**num_error** | **int** | The number of urls without errors. | 
**error_link** | [**LinkDesc**](LinkDesc.md) |  | [optional] 
**wt_agreed** | **float** | The weighted sum agreed uris. | [optional] [default to 0.0]
**wt_disagreed** | **float** | The weighted sum of disagree uris. | [optional] [default to 0.0]
**wt_too_close** | **float** | The sum of the tooClose uris. | [optional] [default to 0.0]
**wt_no_quorum** | **float** | The weighted sum of NoQuorum uris. | [optional] [default to 0.0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


