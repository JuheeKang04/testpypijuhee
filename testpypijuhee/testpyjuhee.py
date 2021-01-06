import kss

def testfuncjuhee(text):
    print('아 이것은 kss 테스트입니다!')
    split_list = kss.split_sentences(text)
    return split_list

def calculate_rouge(gold_list, pred_list):
  gold_and_pred_list = [p for p in pred_list if p in gold_list]
  return len(gold_and_pred_list)/len(gold_list)

def return_score(gold_list, pred_list):
    rouge = []
    for i in range(0, len(gold_list)):
        i_gold = gold_list[i]
        i_pred = pred_list[i]
        if len(i_gold) == 0:
            print(f'{i}번째 gold len==0')
        else:
            rouge.append(calculate_rouge(i_gold, i_pred))

    return rouge