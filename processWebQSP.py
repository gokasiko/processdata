import json
old_path = "RL_train_TR_sub_old.question"
test_path = "RL_test_TR_sub_webqsp.question"
new_dict = {}
with open(test_path, "r", encoding='UTF-8') as webQaData:
    load_dict = json.load(webQaData)
    for key, value in load_dict.items():
        if "WebQTest" not in key:
            continue
        cur_dict = {}
        cur_dict["question"] = value["question"]
        cur_dict["entity"] = value["entity"]
        cur_dict["relation"] = value["relation"]
        cur_dict["type"] = value["type"]
        cur_dict["context_ints"] = {}
        cur_dict["response_bools"] = {}
        response_entities_list = []
        for key_a in value["answers"]:
            response_entities_list.append(key_a["AnswerArgument"])
        cur_dict["response_entities"] = response_entities_list
        cur_dict["entity_mask"] = value["entity_mask"]
        cur_dict["relation_mask"] = value["relation_mask"]
        cur_dict["type_mask"] = value["type_mask"]

        orig_response_list = []
        cur_dict["orig_response"] = orig_response_list


        str_elist = []
        for i in range(len(value["entity"])):
            str_elist.append("ENTITY" + str(i+1))
        entity_str = " ".join(str_elist)
        str_rlist = []
        for i in range(len(value["relation"])):
            str_rlist.append("RELATION" + str(i + 1))
        entity_str = " ".join(str_rlist)
        str_tlist = []
        for i in range(len(value["type"])):
            str_tlist.append("TYPE" + str(i + 1))

        entity_str = " ".join(str_elist)
        r_str = " ".join(str_rlist)
        t_str = " ".join(str_tlist)

        input_str = str.format("<E> {0} </E> <R> {1} </R> <T> {2} </T> {3} ", entity_str, r_str, t_str, value["question"])
        print(input_str)

        cur_dict["input"] = input_str

        new_dict[key] = cur_dict
# fw = open('RL_train_TR_sub_webqsp.json', 'w', encoding="UTF-8")
fw = open('RL_test_TR_sub_webqsp.json', 'w', encoding="UTF-8")
fw.writelines(json.dumps(new_dict, indent=1, ensure_ascii=False))
