
urlBase = 'https://www.googleapis.com/compute/v1/'
# myProject = 'cloudadmingcpdemos'
# zone = 'us-central1-a'

#context.env['deployment'] name of deployment on creation
#context.env['name'] name of the resource using the template
#context.env['project'] the id of the project the deployment is in


def GenerateConfig(context):
    resources = {'resources': [{
        'name': context.env['name'],
        'type': 'compute.v1.instance',
        'properties': {
            'zone': context.properties['zone'],
            'machineType': ''.join([urlBase, 'projects/', 
                                    context.env['project'], '/',
                                    'zones/', context.properties['zone'], '/',
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
