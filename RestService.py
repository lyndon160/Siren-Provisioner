from flask import Flask, url_for, request, Response
import json

class RestService:

#class RestService:


    app = Flask(__name__)



    @app.route('/')
    def api_root():
        return 'Welcome'

    @app.route('/nodes', methods = ['GET'])
    def api_nodes():
        #Get these from a database or at least a dynamic data list.
        #Data needs to include list of services
        data = {
            'Nodes' : [
                {
                    'Network': 10,
                    'Location': 'Home',
                    'Ownership': 'Residence owner',
                    'Platform': 'ARM',
                    'RAM': 500,
                    'ID': 2,
                    'Services' : [
                        {
                            'ID': 443634,
                            'RAM': 20,
                            'Bandwidth': 1
                         },
                        {
                            'ID': 1251,
                            'RAM': 200,
                            'Bandwidth': 5
                        }
                    ][1,2]
                },
                {
                    'Network': 10000,
                    'Location': 'ISP core',
                    'Ownership': 'BT',
                    'Platform': 'ARM',
                    'RAM': 10000,
                    'ID': 2,
                    'Services': [
                        {
                            'ID': 145634,
                            'RAM': 20,
                            'Bandwidth': 1
                        },
                        {
                            'ID': 14534,
                            'RAM': 200,
                            'Bandwidth': 5
                        },
                        {
                            'ID': 14535,
                            'RAM': 200,
                            'Bandwidth': 5
                        },
                        {
                            'ID': 14536,
                            'RAM': 200,
                            'Bandwidth': 5
                        },
                        {
                            'ID': 14537,
                            'RAM': 200,
                            'Bandwidth': 5
                        }
                    ]

                },
                {
                    'Network': 1000,
                    'Location': 'Telephone exchange',
                    'Ownership': 'BT',
                    'Platform': 'ARM',
                    'RAM': 5000,
                    'ID': 3,
                    'Services': [
                        {
                            'ID': 125634,
                            'RAM': 20,
                            'Bandwidth': 1
                        },
                        {
                            'ID': 1451,
                            'RAM': 200,
                            'Bandwidth': 5
                        }
                    ]
                }
            ]
        }

        resp = Response(json.dumps(data))
        return resp
    #    return 'List of ' + url_for('api_nodes')

    #Just a single node at the moment
    @app.route('/nodes/<nodeid>/provision_docker', methods=['POST'])
    def api_provision_docker(self, node_ids):
        if not request.json or not 'image_name' in request.json:
            abort(400)

        self.deployer.deploy_docker(0, request.json['image_name'])

       # return "Provisioned " + request.json['docker_name'] + " to " + nodeid
        resp = Response(json.dumps({'docker_name': request.json['docker_name']}), status=200, mimetype='application/json')
        return resp


    @app.route('/nodes/provision_docker', methods=['POST'])
    def api_provision_dockers(self):
        resp = Response(json.dumps({'requests': request.json['requests']}), status=200, mimetype='application/json')
        return resp



    @app.route('/nodes/<nodeid>')
    def api_node(self, nodeid):
        # Change this to dynamically grab a node from database
        data = {
            'Network': 10,
            'Ownership': 'Residence owner',
            'Platform': 'ARM',
            'RAM': 500,
            'id': nodeid
                }
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
        return resp


    @app.route('/nodes/<nodeid>/remove_service', methods=['PUT', 'GET'])
    def api_remove_service(nodeid):
        if request.method == 'GET':
            return "You need to use DELETE to remove a container\n"
        elif request.method == 'PUT':
            return "ECHO: PUT\n"
        elif request.method == 'DELETE':
            return "TODO. Delete container on node"

        return "TODO. Delete container on node"


    @app.route('/remove_service', methods=['DELETE'])
    def api_remove_service_by_id():
        if request.method == 'GET':
            return "You need to use DELETE to remove a container\n"
        elif request.method == 'DELETE':
            resp = Response(json.dumps({'service_id': request.json['service_id']}), status=200, mimetype='application/json')
            return  resp

        return "TODO. Delete container on node"



    if __name__ == '__main__':
        app.run(port=60000)

    def __init__(self, deployer, discovery):
        self.app.run(port=60000)
        self.deployer = deployer
        self.discovery = discovery

