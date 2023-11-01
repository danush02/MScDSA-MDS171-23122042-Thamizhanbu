import random
samp_dict={"dicts":[]}

for i in range(1,3):
    samp={"orderid":None,"items":[]}
    item={"itemnumber":None,"quantity":None}
    samp["orderid"]=(str(random.randint(0,9))+str(random.randint(0,9)))
    item["itemnumber"]=1
    quantity=input()
    item["quantity"]=quantity
    samp["items"].append(item)
    samp_dict["dicts"].append(samp)
    print(samp_dict)

