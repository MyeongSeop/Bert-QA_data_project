# Bert-QA_data_project

## Project Explanation

- Bert를 사용하여 QA data, 문답형 데이터를 학습시킨다. 
- Pre trained bert model을 이용하고 문답형 데이터를 사용해 fien tuning을 한다. 
- 학습과 검증에 사용될 data는 KorQuad v2.0과 동일한 형태이다. 
- Pre-trained model은 Korean Wiki data를 사용하여 train한 model이다. 
  (https://ratsgo.github.io/embedding/downloaddata.html)
- Pre-train에 사용된 code는 google-research multilingual-bert code를 이용하였다. 
  (https://github.com/google-research/bert/blob/master/multilingual.md)
- Tensorflow v1.15.0
- Python3


## Result

- Train parameter : doc_stride = 128, batch_size = 12, learning_rate = 2e-5, epochs = 4, max_seq_length = 384
- Test(dev) data Accuracy

  EM score : 84.13793103448276
  
  F1 score : 91.85130359871962
