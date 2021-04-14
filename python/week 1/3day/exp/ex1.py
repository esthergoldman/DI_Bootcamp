keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

zip_list = zip(keys,values)
print(zip_list)

num_dict = {}
for info in zip_list:
    #print(info)
    num_dict[info[0]] = info[1]
    
print(num_dict)

