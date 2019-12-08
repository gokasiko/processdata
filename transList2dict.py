import json

list_path = "WebQSP_ANNOTATIONS_test.json"
dict_path = "WebQSP_dict.json"
train_dict = {}
test_dict = {}
with open(list_path, "r", encoding='UTF-8') as webQaData:
    load_list = json.load(webQaData)
    for item in load_list:
        key = list(item.keys())[0]
        value = list(item.values())[0]
        print(key)
        if key.startswith("WebQTrn"):
            train_dict[key] = value
        else:
            test_dict[key] = value

    fw_train = open('webqsp_train_dict.json', 'w', encoding="UTF-8")
    fw_train.writelines(json.dumps(train_dict, indent=1, ensure_ascii=False))
    fw_test = open('webqsp_test_dict.json', 'w', encoding="UTF-8")
    fw_test.writelines(json.dumps(test_dict, indent=1, ensure_ascii=False))