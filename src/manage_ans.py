import json
import sys

origin_input_path = sys.argv[1]
prediction_path = sys.argv[2]
convert_path = sys.argv[3]
print("origin input file path : "+origin_input_path)
print("origin prediction file path : "+prediction_path)
print("convert prediction file path : "+convert_path)

origin_json = open(origin_input_path)
predict_json = open(prediction_path)
convert_text_file = open(convert_path,'w')

predict_data = json.load(predict_json)
origin_data_file = json.load(origin_json)

origin_data = origin_data_file['data']
origin_idx = 0
new_predict_data = {}
new_predict_text = ''
for i in range(len(predict_data)):
    if origin_data[origin_idx]['least_id'] <= i and origin_data[origin_idx]['most_id'] >= i :
        predict_question = predict_data[str(i)]
        for idx in reversed(range(len(predict_question))):
            if (predict_question[idx]=='?' or predict_question[idx]=='.') and idx != (len(predict_question)-1):
                predict_question = predict_question[idx+2:]
                break
        origin_paragraphs = origin_data[origin_idx]['paragraphs']
        origin_context = origin_paragraphs[0]['context']
        start_idx = origin_context.find(predict_question)
        ck = 0
        origin_predict = ''
        prev_text = ''
        for j in range(start_idx,0,-1):
            if origin_context[j]==':' and origin_context[j-1]=='A':
                prev_text = origin_context[j-1:start_idx]
                break
        origin_predict = prev_text + origin_predict
        for j in range(start_idx,len(origin_context)):
            if (origin_context[j] == 'B' and origin_context[j+1]==':') or (origin_context[j] == 'C' and origin_context[j+1]==':') :
                ck = 1
            if ck == 1 and origin_context[j] == 'A' and origin_context[j+1] == ':' :
                break
            origin_predict += origin_context[j]
        new_predict_data[str(i)] = origin_predict
        new_predict_text += origin_predict + '\n'
    else:
        origin_idx += 1
        predict_question = predict_data[str(i)]
        for idx in reversed(range(len(predict_question))):
            if (predict_question[idx]=='?' or predict_question[idx]=='.') and idx != (len(predict_question)-1):
                predict_question = predict_question[idx+2:]
                break
        origin_paragraphs = origin_data[origin_idx]['paragraphs']
        origin_context = origin_paragraphs[0]['context']
        start_idx = origin_context.find(predict_question)
        ck = 0
        origin_predict = ''
        prev_text = ''
        for j in range(start_idx,0,-1):
            if origin_context[j]==':' and origin_context[j-1]=='A':
                prev_text = origin_context[j-1:start_idx]
                break
        origin_predict = prev_text + origin_predict
        for j in range(start_idx,len(origin_context)):
            if (origin_context[j] == 'B' and origin_context[j+1]==':') or (origin_context[j] == 'C' and origin_context[j+1]==':') :
                ck = 1
            if ck == 1 and origin_context[j] == 'A' and origin_context[j+1] == ':' :
                break
            origin_predict += origin_context[j]
        new_predict_data[str(i)] = origin_predict
        new_predict_text += origin_predict + '\n'
        
'''
with open('whole_predictions.json','w') as json_file:
    json.dump(new_predict_data,json_file)
'''
convert_text_file.write(new_predict_text)

        
