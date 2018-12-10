import json

with open("output.json", "r") as file_object:
    output_dictionary = json.load(file_object)

print(output_dictionary['key4']['a'])
output_dictionary['key5'] = 'new value'
print(output_dictionary)
print(output_dictionary.get('key2'))
print(output_dictionary.get('key6'), "this key does not exist")

if 'key3' in output_dictionary:
    print("the key exists")

for key in output_dictionary:
    print(output_dictionary[key])

print(list(output_dictionary))