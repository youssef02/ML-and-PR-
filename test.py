row = ["2.3 to  4.5GH","2.5 GH"]

for i  in row:
    #if i contain "to"
    if "to" in i:
        i = i.split("to")
        
        i = i[1].split("GH")
        print(float(i[0]))
    else:
        i = i.split("GH")
        print(float(i[0]))