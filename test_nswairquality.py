#!/usr/bin/env python3

from src import nswairquality

if __name__ == "__main__":
    x = nswairquality.NSWAirQuality()
    print(x.toJSON(True))
