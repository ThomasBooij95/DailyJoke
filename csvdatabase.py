# import pandas as pd
# df = pd.read_csv(jokes.csv)
# print(df)
from joke.models import Joke
import csv
with open('jokes.csv' ,newline = '') as f:
    reader = csv.reader(f)
    data = list(reader)

    # print(data)
    print("succesfull script")
#
for joke in data:
    Joke.objects.create(joke = joke[1])
