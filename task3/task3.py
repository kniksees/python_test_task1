import json
import sys

def merge_values(values_file, tests_file, report_file):
    with open(values_file, 'r') as f:
        values = json.load(f)
    with open(tests_file, 'r') as f:
        tests = json.load(f)

    dict = {}


    for i in values['values']:
        dict[i['id']] = i['value']

    def fill_values(dict, tests_data):
        for test in tests_data:
            if int(test['id']) in dict:
                test['value'] = dict[int(test['id'])]
            if 'values' in test:
                fill_values(dict, test['values'])
    fill_values(dict, tests['tests'])
    
    with open(report_file, 'w') as f:
        json.dump(tests, f, indent=2)
        
if __name__ == '__main__':
    values_file, tests_file, report_file = sys.argv[1], sys.argv[2], sys.argv[3]
    merge_values(values_file, tests_file, report_file)

