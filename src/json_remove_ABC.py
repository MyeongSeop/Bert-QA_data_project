import json
import sys

origin_json_path = sys.argv[1]
convert_json_path = sys.argv[2]
num_times = sys.argv[3]
print("origin json file path : "+origin_json_path)
print("convert json file(remove A,B,C) path : "+convert_json_path)
print("make output file size "+convert_json_path+" times")

json_file = open(origin_json_path)
json_data = json.load(json_file)
train_data = json_data['data']
new_id = 0
new_data = []
def convert_data():
    global new_data, new_id, train_data
    for i in train_data :
        least_id = new_id
        paragraphs = i['paragraphs']
        context = paragraphs[0]['context']
        qas = paragraphs[0]['qas']
        new_context = ''
        ck = -1
        cnt = 0
        
        for idx in range(len(context)):
            if context[idx] == 'A' and context[idx+1] == ':' :
                ck = 0
                cnt = 0
            elif context[idx] == 'B' and context[idx+1] == ':':
                ck = 1
                cnt = 0
            elif context[idx] == 'C' and context[idx+1] == ':':
                ck = 1
                cnt = 0
            elif cnt <= 1:
                cnt+=1
                continue
            elif ck == 0:
                new_context+=context[idx]
        
        new_qas = []
        
        for each_qas in qas:
            ans = each_qas['answers']
            ans_text = ans[0]['text']
            ans_text = ans_text[3:]
            new_text = ''
            for idx in ans_text:
                if idx == 'B' or idx == 'C':
                    break
                new_text+=idx
            
            new_ans_start = new_context.find(new_text)
            
            new_qas.append(
                {
                    'answers': [{'text': new_text, 'answer_start': new_ans_start}],
                    'id': str(new_id),
                    'question': each_qas['question']
                }
            )
            new_id += 1
        new_paragraphs = [{'context':new_context, 'qas':new_qas}]
        new_data.append({'paragraphs':new_paragraphs, 'least_id':least_id, 'most_id':new_id})

for i in range(int(num_times)):
    convert_data()

new_train = {
    'data': new_data
}
with open(convert_json_path,'w') as json_file:
    json.dump(new_train,json_file)
    

        

