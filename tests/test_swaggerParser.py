import requests
import json
import unittest

class SwaggerParser(unittest.TestCase):
    
    @staticmethod
    def get_swagger_json(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def parse_swagger(swagger_json):
        endpoints = {}
        paths = swagger_json.get('paths', {})
        components = swagger_json.get('components', {}).get('schemas', {})

        for path, path_info in paths.items():
            for method, method_info in path_info.items():
                endpoint = {
                    'method': method.upper(),
                    'parameters': method_info.get('parameters', []),
                    'responses': {}
                }

                responses = method_info.get('responses', {})
                for status_code, response_info in responses.items():
                    content = response_info.get('content', {})
                    for content_type, content_info in content.items():
                        schema_ref = content_info.get('schema', {}).get('$ref', '')
                        if schema_ref:
                            schema_name = schema_ref.split('/')[-1]
                            endpoint['responses'][status_code] = components.get(schema_name, {})
                
                if path not in endpoints:
                    endpoints[path] = []
                endpoints[path].append(endpoint)

        return endpoints

    @staticmethod
    def display_endpoints(endpoints):
        for path, methods in endpoints.items():
            print(f"Path: {path}")
            for method in methods:
                print(f"  Method: {method['method']}")
                print("  Parameters:")
                for param in method['parameters']:
                    print(f"    - {param['name']} ({param['in']}): {param['schema']['type']}")
                print("  Responses:")
                for status_code, response in method['responses'].items():
                    print(f"    {status_code}: {json.dumps(response, indent=4)}")
            print()

    def test_swagger_parser(self):
        url = 'http://localhost:8080/swagger/v1/swagger.json'
        swagger_json = self.get_swagger_json(url)
        endpoints = self.parse_swagger(swagger_json)
        self.display_endpoints(endpoints)

if __name__ == '__main__':
    unittest.main()
