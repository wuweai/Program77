sentence = input("請輸入英文句子:")
sentence = sentence.strip('.')
ans = sentence.split()
ans.reverse()
print(ans)