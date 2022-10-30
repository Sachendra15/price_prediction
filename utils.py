
import pandas as pd
import numpy as np
import pickle
import json
import config
import warnings
warnings.filterwarnings("ignore")


class CarPricePrediction():

    def __init__(self,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,wheel_base,length,width,height,
       curb_weight,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,Mileage,make,body_style):

       self.normalized_losses = normalized_losses
       self.fuel_type = fuel_type
       self.aspiration = aspiration
       self.num_of_doors = num_of_doors
       self.drive_wheels = drive_wheels
       self.wheel_base = wheel_base
       self.length = length
       self.width = width
       self.height = height
       self.curb_weight = curb_weight
       self.num_of_cylinders = num_of_cylinders
       self.engine_size = engine_size
       self.fuel_system = fuel_system
       self.bore = bore
       self.stroke = stroke 
       self.compression_ratio = compression_ratio
       self.horsepower = horsepower
       self.peak_rpm = peak_rpm
       self.Mileage = Mileage
       self.make = "make_" + make
       self.body_style = "body_style_" + body_style

    def load_model(self):

        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.lin_model = pickle.load(f)

        with open(config.PROJECT_DATA_PATH, "r") as f:
            self.project_data = json.load(f)


    def get_predicted_price(self):

        self.load_model()

        make_index = self.project_data["columns"].index(self.make)
        body_style_index = self.project_data["columns"].index(self.body_style)

        len_array = len(self.project_data["columns"])

        user_array = np.zeros(len_array)

        user_array[0] = self.normalized_losses
        user_array[1] = self.project_data["fuel_type"][self.fuel_type]
        user_array[2] = self.project_data["aspiration"][self.aspiration]
        user_array[3] = self.project_data["num_of_doors"][self.num_of_doors]
        user_array[4] = self.project_data["drive_wheels"][self.drive_wheels]
        user_array[5] = self.wheel_base
        user_array[6] = self.length
        user_array[7] = self.width
        user_array[8] = self.height
        user_array[9] = self.curb_weight
        user_array[10] = self.project_data["num_of_cylinders"][self.num_of_cylinders]
        user_array[11] = self.engine_size
        user_array[12] = self.project_data["fuel_system"][self.fuel_system]
        user_array[13] = self.bore
        user_array[14] = self.stroke
        user_array[15] = self.compression_ratio
        user_array[16] = self.horsepower
        user_array[17] = self.peak_rpm
        user_array[18] = self.Mileage
        user_array[make_index] = 1
        user_array[body_style_index] = 1

        predicted_price = self.lin_model.predict([user_array])[0]

        print("Predicted price of your Car --> ", np.around(predicted_price, decimals=2))

        return predicted_price


if __name__ == "__main__":
    normalized_losses = 150
    fuel_type = "diesel"
    aspiration = "turbo"
    num_of_doors = "four"
    drive_wheels = "rwd"
    wheel_base = 100
    length = 180
    width = 63
    height  = 53
    curb_weight = 2400
    num_of_cylinders = 'four'
    engine_size = 100
    fuel_system = "mpfi"
    bore = 3.19
    stroke = 3.21
    compression_ratio = 10.1
    horsepower = 200
    peak_rpm = 6000
    Mileage = 23
    make = "porsche"
    body_style = "sedan"

    class_obj = CarPricePrediction(normalized_losses,fuel_type,aspiration,num_of_doors,
                                   drive_wheels,wheel_base,length,width,height,
                                   curb_weight,num_of_cylinders,engine_size,fuel_system,bore,
                                   stroke,compression_ratio,horsepower,peak_rpm,Mileage,make,body_style)

    class_obj.get_predicted_price()






