# PeerData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peer_id** | **str** | the peer id for this participant | 
**status** | **str** | the status of this peer | 
**agreement** | **float** | the percentage of vote agreement. | [optional] 
**num_agree** | **int** |  | [optional] 
**agree_link** | [**LinkDesc**](LinkDesc.md) |  | [optional] 
**num_disagree** | **int** |  | [optional] 
**disagree_link** | [**LinkDesc**](LinkDesc.md) |  | [optional] 
**num_poller_only** | **int** |  | [optional] 
**poller_only_link** | [**LinkDesc**](LinkDesc.md) |  | [optional] 
**num_voter_only** | **int** |  | [optional] 
**voter_only_link** | [**LinkDesc**](LinkDesc.md) |  | [optional] 
**bytes_hashed** | **int** | the number of bytes hashed. | [optional] 
**bytes_read** | **int** | the number of bytes read. | [optional] 
**wt_agreement** | **float** | the weight of vote percentage agreement. | [optional] 
**wt_num_agree** | **float** | the weight of number agree votes. | [optional] 
**wt_num_disagree** | **float** | the weight of number of disagree votes. | [optional] 
**wt_num_poller_only** | **float** | the weight of number of poller only votes. | [optional] 
**wt_num_voter_only** | **float** | the weight of number of voter only votes. | [optional] 
**state** | **str** | the state machine state. | [optional] 
**last_state_change** | **int** | the time of last state change. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


