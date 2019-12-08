#encoding:utf-8
import json

# class Complex():
#     def __init__(self, n, label, questions, sql, sql2, id):
#         self.nn = n
#         self.Label = label
#         self.Question = questions
#         self.Sql = sql
#         self.Sql2 = sql2
#         self.ID = id
#
# # 带子图
# class QapairSub(object):
#     def __init__(self, question, answer, sparql, subgraph):
#         self.question = question
#         self.answer = answer
#         self.sparql = sparql
#         self.subgraph = subgraph
#
#     def obj_2_jsonsub(obj):
#         return {
#             "question": obj.question,
#             "answer": obj.answer,
#             "sparql": obj.sparql,
#             "subgraph": obj.subgraph,
#         }
#
# # 不带子图
# class Qapair(object):
#     def __init__(self, question, answer, sparql):
#         self.question = question
#         self.answer = answer
#         self.sparql = sparql
#
#     def obj_2_json(obj):
#         return {
#             "question": obj.question,
#             "answer": obj.answer,
#             "sparql": obj.sparql,
#         }
#
# #Load WebQuestions Semantic Parses
# WebQSPList = []
# with open("WebQSP.train.json", "r", encoding='UTF-8') as webQaTrain:
#     with open("WebQSP.test.json", "r", encoding='UTF-8') as webQaTest:
#         load_dictTrain = json.load(webQaTrain)
#         load_dictTest = json.load(webQaTest)
#         mytrainquestions = load_dictTrain["Questions"]
#         print(len(mytrainquestions))
#         mytestquestions = load_dictTest["Questions"]
#         print(len(mytestquestions))
#         myquestions = mytrainquestions + mytestquestions
#         print(len(myquestions))
#         for q in myquestions:
#             question = q["ProcessedQuestion"]
#             # answer = q["Parses"][0]["Answers"][0]["AnswerArgument"]
#             Answers = []
#             answerList = q["Parses"][0]["Answers"]
#             for an in answerList:
#                 Answers.append(an['AnswerArgument'])
#             # print(answer)
#             sparql = q["Parses"][0]["Sparql"]
#             # print(sparql)
#             mypair = Qapair(question, Answers, sparql)
#             WebQSPList.append(mypair)
#
# #写入转换后的json
# jsondata = json.dumps(WebQSPList, indent=1, default=Qapair.obj_2_json)
# fileObject = open('WEbqatest.json', 'w')
# fileObject.write(jsondata)
# fileObject.close()

datapath_train = "WebQSP.train.json"
datapath_test = "WebQSP.test.json"
out_train = "WebQSP_questions_train.json"
out_test = "WebQSP_questions_test.json"
with open(datapath_train, "r", encoding='UTF-8') as webQaData:
    dict2file = {}
    load_dict = json.load(webQaData)
    myquestions = load_dict["Questions"]
    for q in myquestions:
        question = q["ProcessedQuestion"]
        # answer = q["Parses"][0]["Answers"][0]["AnswerArgument"]
        Answers = []
        answerList = q["Parses"][0]["Answers"]
        for an in answerList:
            Answers.append(an['AnswerArgument'])
        # print(answer)
        sparql = q["Parses"][0]["Sparql"]
        dict_item = {}
        dict_item
        dict2file[]
    with open(datapath_train, "r", encoding='UTF-8') as webQaData:


