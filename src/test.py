scores=[5,4,3,2,7,4,1,2,3,110,50,30]
sorted_scores=sorted(scores)
print((sorted_scores))
top_10=[]

for score in sorted_scores:
    top_10.append(score)

    if len(top_10) == 10:
        print(top_10)
        break