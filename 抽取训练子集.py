import json
datapath_train = "PT_train.question"

cipitr = {}
all_list = {}
cipitr_list = []
# cipitr_path = "infchain_1/infchain_1_train.json"
# with open(cipitr_path, "r", encoding='UTF-8') as cipitr_dict:
#     cipitr = json.load(cipitr_dict)
#     with open(datapath_train, "r", encoding='UTF-8') as all_list:
#         print("datapath_train", "down")
#         for item in all_list:
#             for c_item in cipitr:
#                 if c_item in item:
#                     cipitr_list.append(item)
#
# fw = open('PT_train.webqsp.infchain_1.question', 'w')
# # fw = open('{0}/{0}_test.json'.format(type_key), 'w')
# fw.writelines(cipitr_list)

action_list = []
with open("PT_train.webqsp.infchain_1.question", "r", encoding='UTF-8') as infchain_1_question:
    with open("PT_train.action", "r", encoding='UTF-8') as actions:
        for item in infchain_1_question:
            id = item.split(" ")[0]
            for a in actions:
                if id in a:
                    action_list.append(a)
fw = open('PT_train.webqsp.infchain_1', 'w')
fw.writelines(cipitr_list)



