#!/usr/bin/env python3

__author__ = 'Detrich with help from david richardson'

import requests
import turtle
import time

Lat = 39.7684
Long = -86.1581


def in_space():
    response = requests.get("http://api.open-notify.org/astros.json")
    json_res = response.json()
    print("There are currently {} people in space:".format(json_res["number"]))
    for p in json_res["people"]:
        print("{} is currently on the {}".format(p["name"], p["craft"]))


def find_pass():
    isspass_res = requests.get(
        f"http://api.open-notify.org/iss-pass.json?lat={Lat}&lon={Long}")
    date_of_pass = isspass_res.json()["response"][1]["risetime"]
    return time.ctime(date_of_pass)


def geo():
    resp = requests.get("http://api.open-notify.org/iss-now.json")
    json_res = resp.json()
    iss_pos = json_res["iss_position"]
    return(iss_pos)


def iss_turtle():
    screen = turtle.Screen()
    screen.setup(710, 360)
    screen.bgpic("map.gif")
    screen.setworldcoordinates(-170, -80, 180, 90)
    turtle.title("The next time the ISS goes over Indiana")
    turtle.penup()
    turtle.goto(Long, Lat)
    turtle.color("white")
    turtle.write(find_pass(), font=("Arial", 20, "normal"))
    turtle.dot(5, "yellow")
    screen.addshape("iss.gif")
    turtle.shape("iss.gif")
    while True:
        turtle.goto(float(geo()["longitude"]), float(geo()["latitude"]))
        time.sleep(2)


def main():
    in_space()
    iss_turtle()


if __name__ == '__main__':
    main()
