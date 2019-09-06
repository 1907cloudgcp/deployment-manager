

def GenerateConfig(unused_context):
    resources = {'resources':[{
        'name':'new-network',
        'type': 'compute.v1.network',
        'properties':{
            'routingConfig':{
                'routingMode': 'REGIONAL'
            },
            'autoCreateSubnetworks': True
        }
    }]}
    return resources