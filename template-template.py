
def GenerateConfig(unused_context):
    resources = {'resources': [{
        'name': 'vm1',
        'type': 'vm-template.py'
    },{
        'name': 'network-1',
        'type': 'network-template.py'
    },{
        'name': 'fw1',
        'type': 'firewall-template.py'
    }
    ]}
    return resources