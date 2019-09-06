
urlBase = 'https://www.googleapis.com/compute/v1/'
myProject = 'cloudadmingcpdemos'
zone = 'us-central1-a'



def GenerateConfig(unused_context):
    resources = {'resources': [{
        'name': 'template-vm-1',
        'type': 'compute.v1.instance',
        'properties': {
            'zone': zone,
            'machineType': ''.join([urlBase, 'projects/', 
                                    myProject, '/',
                                    'zones/', zone, '/',
                                     'machineTypes/f1-micro']),
            'disks':[{
                'deviceName': 'boot-disk',
                'type': 'PERSISTENT',
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': ''.join([urlBase,'projects/debian-cloud/global/images/family/debian-9'])
                }
            }],
            'networkInterfaces': [{
                'network':'$(ref.new-network.selfLink)',
                'accessConfigs':[{
                    'name': 'External NAT',
                    'type': 'ONE_TO_ONE_NAT'
                }]
            }]
        }

    }]}
    
    return resources
