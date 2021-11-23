from amadeus import Client, ResponseError
from amadeus import Location
from amadeus.client.response import Response
from .config import *
import time

class Dashboard:
    def __init__(self):
        self.amadeus = Client(client_id=API_KEY, client_secret=API_SECRET_KEY)

    def most_booked(self, airport, time_period):
        response = self.amadeus.travel.analytics.air_traffic.booked.get(originCityCode=airport, period=time_period)
        return response.data
    
    def most_travelled(self, airport, time_period):
        response = self.amadeus.travel.analytics.air_traffic.traveled.get(originCityCode=airport, period=time_period)
        return response.data

    def price_analysis(self, origin, destination, date):
        response = self.amadeus.analytics.itinerary_price_metrics.get(originIataCode=origin,
                                                             destinationIataCode=destination,
                                                             departureDate=date)
        return response.data

    def delay_prediction(self, origin, destination, departureDate, departureTime,
                         arrivalDate, arrivalTime, aircraftCode, carrierCode, flightNumber, duration):
        response = self.amadeus.travel.predictions.flight_delay.get(originLocationCode=origin, destinationLocationCode=destination,
                                                           departureDate=departureDate, departureTime=departureTime,
                                                           arrivalDate=arrivalDate, arrivalTime=arrivalTime,
                                                           aircraftCode=aircraftCode, carrierCode=carrierCode,
                                                           flightNumber=flightNumber, duration=duration)

        return response.data
    
    def busiest_month(self, airport, year, direction):
        response = self.amadeus.travel.analytics.air_traffic.busiest_period.get(
                    cityCode=airport, period=year, direction=direction)

        return response.data
    

    def on_time_performance(self, airport, date):
        response = self.amadeus.airport.predictions.on_time.get(airportCode=airport, date=date)

        return response.data
    
    def availability_search(self, body):
        response = self.amadeus.shopping.availability.flight_availabilities.post(body)
        
        return response.data