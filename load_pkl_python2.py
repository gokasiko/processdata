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


# data = pickle.load(open("WebQSP_gold_data_test.pkl", 'rb'))
data = pickle.load(open("WebQSP_gold_data_train.pkl", 'rb'))
print len(data)
for item in data[0:10]:
    print item

# fw_train = open('WebQSP_gold_data_test.json', 'w')
# fw_train.writelines(json.dumps(data, indent=1, ensure_ascii=False))