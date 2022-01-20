import requests
from datetime import datetime
import smtplib
import time


# from https://www.latlong.net/ ----> (-0.166443, -78.490290)
MY_LAT = -0.103624
MY_LONG = -78.503855
UTC = -5
parameters = {"lat": MY_LAT,
              "lng": MY_LONG,
              "formatted": 0}

wait_time = 60
keep_running = True
while keep_running:
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    # print(response) # 200 means every is going well, there are other responses for errors, like 404

    iss_data = iss_response.json()

    longitude_data = float(iss_data["iss_position"]["longitude"])
    latitude_data = float(iss_data["iss_position"]["latitude"])

    iss_position = (longitude_data, latitude_data)
    print(f"ISS Position right now is {iss_position}")
    print(f"My position is {MY_LONG, MY_LAT}")

    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    #print(sun_data)
    # print(f'The sunrise is at {sun_data["results"]["sunrise"]} and the sunset is at {sun_data["results"]["sunset"]}')

    sunrise_h = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunrise_h = sunrise_h + UTC
    sunrise_m = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[1])
    sunrise_s = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[2].split("+")[0])
    # print(f"{sunrise_h}:{sunrise_m}:{sunrise_s}")

    sunset_h = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    sunset_h = sunset_h + UTC
    sunset_m = int(sun_data["results"]["sunset"].split("T")[1].split(":")[1])
    sunset_s = int(sun_data["results"]["sunset"].split("T")[1].split(":")[2].split("+")[0])
    # print(f"{sunset_h}:{sunset_m}:{sunset_s}")


    ################################################## CHALLENGE ##################################################
    # Check if the ISS in close to my current location
    long_distance = abs(MY_LONG - longitude_data)
    lat_distance = abs(MY_LAT - latitude_data)
    my_time = datetime.now()
    print(my_time)
    if long_distance < 10 and lat_distance < 10:
        print("The ISS is near!")
        # If it is dark, send me an email to tell me to look up
        if my_time.hour > sunset_h and my_time.hour < sunrise_h:
            print("Its dark ! Send me an email!")
            with smtplib.SMTP("smtp.office365.com", port=587) as connection:
                connection.starttls()
                connection.login(user="feliperojasl.python@hotmail.com", password="artint2021FZR2303")
                connection.sendmail(from_addr="feliperojasl.python@hotmail.com", to_addrs="epilefrojasleon@hotmail.com",
                                    msg=f"Subject:ISS in range!\n\nFelipe! Mira al cielo ahorita, el ISS esta dentro "
                                        f"del rango de vision. /n ISS POSITION = {iss_position}")

    # Run the code every 60 seconds
    time.sleep(wait_time)