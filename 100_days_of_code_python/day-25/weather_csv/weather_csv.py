import pandas

data = {
    "student" :["nathi","james"],
    "score": [10,12]
}

v=pandas.DataFrame(data)
print(v)













# import pandas
# 
# 
# data = pandas.read_csv("weather_data.csv")
# value=data[data.day=="Monday"].temp =0
# 
# print(data)
# 
# 










#------------------------------------------------------------------------------------
# import pandas
# 
# 
# data =  pandas.read_csv("weather_data.csv")
# 
# value = data[data["temp"] == data["temp"].max()]
# print(value["day"])
# print(data)
# 
# 
# 
# 


#----------------------------------
# import pandas
# 
# 
# data = pandas.read_csv("weather_data.csv")
# 














# print(data[data["temp"] == data.max] )
# print(data[data["day"] =="Monday"])














# --------------------------------------------------------
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"].to_list())
# print(data["temp"].max())
# 
# -------------------------------------------------------
# import csv,pandas

# def weather_print():
    # with open("weather_data.csv") as data_file:
        # data=csv.reader(data_file)
        # temp = []
        # for k in data:
            # if k[1] != "temp":
                # temp.append(int(k[1]))
            # print(k)
    # print(temp)
# weather_print()
# data =pandas.read_csv("weather_data.csv")
# for  
# print(data["temp"][0])
