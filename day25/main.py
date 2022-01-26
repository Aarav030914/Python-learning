import pandas
data = pandas.read_csv("./day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirell = data[data["Primary Fur Color"] == "Gray"]
black_squirell = data[data["Primary Fur Color"] == "Black"]
cinnamon_squirell = data[data["Primary Fur Color"] == "Cinnamon"]

data_dict = {
    "colors" : ["Gray", "Black", "cinnamon"],
    "count" : [len(gray_squirell), len(black_squirell), len(cinnamon_squirell)]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("./day25/Number_of_squirrel.csv")
