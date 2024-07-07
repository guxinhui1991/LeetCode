arr = ["back","backdoor", "background", "ground", "yard", "backyard", "groundwater"]
res, trie=0, dict()
for word in sorted(arr,key=len):
    cur=trie
    for w in word:
        cur=cur.setdefault(w,dict())
        res+=cur.get('#',0)
    cur['#']=cur.get('#',0)+1


print(res)