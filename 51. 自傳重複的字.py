sentence = list(input().split("，"))
sentence = "".join(sentence).split("。")
sentence = "".join(sentence)
ans = set([num for num in sentence if sentence.count(num) > 1])
print(ans)