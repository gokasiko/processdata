import pickle
import json
import datetime

# class DateEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime.datetime):
#             return obj.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(obj, datetime):
#             return obj.strftime("%Y-%m-%d")
#         else:
#             return json.JSONEncoder.default(self, obj)

# with open("WebQSP.train.json", "r") as webQaTrain:
#     with open("WebQSP.test.json", "r") as webQaTest:
#         load_dictTrain = json.load(webQaTrain)
#         load_dictTest = json.load(webQaTest)
#         mytrainquestions = load_dictTrain["Questions"]
#         print(len(mytrainquestions))
#         mytestquestions = load_dictTest["Questions"]
#         print(len(mytestquestions))
#         myquestions = mytrainquestions + mytestquestions
#         print(len(myquestions))
#
#         process_questions = mytrainquestions
#
#         for q in process_questions:
#             question = q["ProcessedQuestion"]
#             Answers = []
#             id = q["QuestionId"]



# data = pickle.load(open("WebQSP_gold_data_test.pkl", 'rb'))
data = pickle.load(open("WebQSP_gold_data_train.pkl", 'rb'))
print len(data)
type_key = "infchain_2_constrained_date"
dict_data = {}
typelist = []
for item in data:
    # print item[0]
    # print item[1]
    # print item[7]
    key = item[10]

    if key == type_key:
        typelist.append(item[0])


    # if key not in dict_data:
    #     itemdict = {key: 0}
    #     dict_data.update(itemdict)
    # else:
    #     dict_data[key] += 1
print dict_data

fw = open('{0}/{0}_train.json'.format(type_key), 'w')
# fw = open('{0}/{0}_test.json'.format(type_key), 'w')
fw.writelines(json.dumps(typelist, indent=1, ensure_ascii=False))

# fw_train = open('WebQSP_gold_data_test.json', 'w')
# fw_train.writelines(json.dumps(data, indent=1, ensure_ascii=False))