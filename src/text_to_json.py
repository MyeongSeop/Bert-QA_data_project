
import json
import sys

input_path = sys.argv[1]
convert_path = sys.argv[2]
print("input file path : "+input_path)
print("output json file path : "+convert_path)

input_file = open(input_path,encoding='UTF8')
prev_seq = ''
cnt = 0
cnt_id = 0
qas = []
paragraphs = []
data = []
least_id = 0
most_id = 0
while True:
    line = input_file.readline()
    if not line : break
    seq = ''
    category = ''
    ck = 0
    for i in line :
        if i == '\t':
            ck = 1
        elif i == '\n':
            continue
        elif ck :
            category += i
        else:
            seq += i
    if prev_seq == '' :
        prev_seq = seq
    elif prev_seq != seq :
        paragraphs.append({'qas':qas,'context':prev_seq})
        data.append({'paragraphs':paragraphs, 'least_id':least_id, 'most_id':cnt_id-1})
        paragraphs = []
        qas = []
        prev_seq = seq
        least_id = cnt_id
    qas.append({'id':str(cnt_id), 'question':category})
    cnt_id += 1
paragraphs.append({'qas':qas,'context':prev_seq})
data.append({'paragraphs':paragraphs, 'least_id':least_id, 'most_id':cnt_id-1})

final = {"data":data}
with open(convert_path,'w') as json_file:
    json.dump(final,json_file)

