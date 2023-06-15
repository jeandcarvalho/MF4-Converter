from asammdf import MDF
import os

dir = os.path.dirname(os.path.realpath(__file__))
os.path.split(dir) 
head, tail = os.path.split(dir)


for file in os.listdir(head):
    if file.endswith(".mf4"):
        file_path = os.path.splitext(file)[0]
        file_name = file_path.split('/')[-1]
        mdf_obj = MDF(os.path.join(head, file))   
        df = mdf_obj.to_dataframe(time_as_date=True, raster=1)
        df.to_csv(head + r'\\' + file_name + r'.csv', sep=',', mode='a')
        print(df.head())

