device_staus = "active"
temprature = 38

if device_staus == "active" : 
    if temprature > 35 : 
        print("High temprature alert!")
    else : 
        print("Temperature is normal")
else: 
    print("Device is offline")