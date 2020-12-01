import pandas

data = pandas.read_csv("Squirrel_data.csv")

squirel_black=len(data[data["Primary Fur Color"] == "Black"])
squirel_cinnamon= len(data[data["Primary Fur Color"] == "Cinnamon"])
squirel_gray=len(data[data["Primary Fur Color"] == "Gray"])
print("Gray",squirel_gray)
print("Cinnamon",squirel_cinnamon)
print("Black",squirel_black)

new_data= {
    "Fur_colour":["Grey","Cinnamon","Black"],
    "Count":[squirel_gray,squirel_cinnamon,squirel_black]
}
squirel_dataframe = pandas.DataFrame(new_data)
squirel_dataframe.to_csv("squirrel_count.csv")





#-----------------------------------------------------------




# data2 = {
    # "student": ["nathi", "james","sipho","tandi"],
    # "off": ["red","blue","blue","yellow"]
# }
# v=pandas.DataFrame(data2)
# count_on=v[v["off"] == "yellow"]
# print(count_on["student"].count())