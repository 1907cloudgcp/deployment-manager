

def GenerateConfig(unused_context):
    resources = {'resources':[{
        'name': 'fw',
        'type': 'compute.v1.firewall',
        'properties':{
            'network':'$(ref.new-network.selfLink)',
            'sourceRanges': ['0.0.0.0/0'],
            'allowed':[{
                'IPProtocol': 'TCP',
                'ports': [80]
            }]
        }
    }]}
    return resources