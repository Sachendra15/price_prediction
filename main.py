
from flask import Flask, render_template, request
from utils import CarPricePrediction
import config

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prediction_price", methods = ["GET", "POST"])
def get_predicted_price():

    if request.method == "GET":

        normalized_losses = float(request.args.get("normalized_losses"))
        fuel_type = request.args.get("fuel_type")
        aspiration = request.args.get("aspiration")
        num_of_doors = request.args.get("num_of_doors")
        drive_wheels = request.args.get("drive_wheels")
        wheel_base = float(request.args.get("wheel_base"))
        length = float(request.args.get("length"))
        width = float(request.args.get("width"))
        height = float(request.args.get("height"))
        curb_weight = float(request.args.get("curb_weight"))
        num_of_cylinders = request.args.get("num_of_cylinders")
        engine_size = float(request.args.get("engine_size"))
        fuel_system = request.args.get("fuel_system")
        bore = float(request.args.get("bore"))
        stroke = float(request.args.get("stroke"))
        compression_ratio = float(request.args.get("compression_ratio"))
        horsepower = float(request.args.get("horsepower"))
        peak_rpm = float(request.args.get("peak_rpm"))
        Mileage = float(request.args.get("Mileage"))
        make = request.args.get("make")
        body_style = request.args.get("body_style")


        class_obj = CarPricePrediction(normalized_losses,fuel_type,aspiration,num_of_doors,
                                   drive_wheels,wheel_base,length,width,height,
                                   curb_weight,num_of_cylinders,engine_size,fuel_system,bore,
                                   stroke,compression_ratio,horsepower,peak_rpm,Mileage,make,body_style)

        price = class_obj.get_predicted_price()

        return render_template("index.html", prediction = price)

    else:

        normalized_losses = float(request.form.get("normalized_losses"))
        fuel_type = request.form.get("fuel_type")
        aspiration = request.form.get("aspiration")
        num_of_doors = request.form.get("num_of_doors")
        drive_wheels = request.form.get("drive_wheels")
        wheel_base = float(request.form.get("wheel_base"))
        length = float(request.form.get("length"))
        width = float(request.form.get("width"))
        height = float(request.form.get("height"))
        curb_weight = float(request.form.get("curb_weight"))
        num_of_cylinders = request.form.get("num_of_cylinders")
        engine_size = float(request.form.get("engine_size"))
        fuel_system = request.form.get("fuel_system")
        bore = float(request.form.get("bore"))
        stroke = float(request.form.get("stroke"))
        compression_ratio = float(request.form.get("compression_ratio"))
        horsepower = float(request.form.get("horsepower"))
        peak_rpm = float(request.form.get("peak_rpm"))
        Mileage = float(request.form.get("Mileage"))
        make = request.form.get("make")
        body_style = request.form.get("body_style")


        class_obj = CarPricePrediction(normalized_losses,fuel_type,aspiration,num_of_doors,
                                   drive_wheels,wheel_base,length,width,height,
                                   curb_weight,num_of_cylinders,engine_size,fuel_system,bore,
                                   stroke,compression_ratio,horsepower,peak_rpm,Mileage,make,body_style)

        price = class_obj.get_predicted_price()

        return render_template("index.html", prediction = price)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= config.PORT_NUMBER, debug= True)
