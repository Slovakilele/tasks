import json


def json_value_parsing(values_id, key="values"):
    for values_dict in json_file2[key]:
        if values_dict["id"] == values_id:
            return values_dict["value"]


def json_parsing(json_file, key="report"):
    for array in json_file[key]:
        id_tests = array["id"]
        if "values" in array:
            json_parsing(array, "values")
        if "value" in array:
            array["value"] = json_value_parsing(id_tests)


json_tests = open("tests.json")
json_values = open("values.json")

json_file1 = json.load(json_tests)
json_file2 = json.load(json_values)

test = {"report": json_file1["tests"]}
json_parsing(test)

with open("report.json", "w") as write_file:
    json.dump(test, write_file, indent=2)

json_tests.close()
json_values.close()
