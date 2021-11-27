from amadeus import Client, ResponseError
from amadeus import Location
from amadeus.client.response import Response
from .config import *
import time

class Dashboard:
    """
    Class containing all the methods for dashboard functions 
    """
    def __init__(self):
        self.amadeus = Client(client_id=API_KEY, client_secret=API_SECRET_KEY)

    def most_booked(self, airport, time_period):
        """
        Gives the most booked flight in a given month of a year at an airport
        """
        response = self.amadeus.travel.analytics.air_traffic.booked.get(originCityCode=airport, period=time_period)
        return response.data
    
    def most_travelled(self, airport, time_period):
        """
        Gives the most travelled flight from an airport in a given month of a year
        """
        response = self.amadeus.travel.analytics.air_traffic.traveled.get(originCityCode=airport, period=time_period)
        return response.data

    def price_analysis(self, origin, destination, date):
        """
        Gives the quartile price distribution of price of flights on a particular dates between origin destination
        """
        response = self.amadeus.analytics.itinerary_price_metrics.get(originIataCode=origin,
                                                             destinationIataCode=destination,
                                                             departureDate=date)
        return response.data

    def delay_prediction(self, origin, destination, departureDate, departureTime,
                         arrivalDate, arrivalTime, aircraftCode, carrierCode, flightNumber, duration):
        """
        Gives delay prediction for a particular flight                 
        """
        response = self.amadeus.travel.predictions.flight_delay.get(originLocationCode=origin, destinationLocationCode=destination,
                                                           departureDate=departureDate, departureTime=departureTime,
                                                           arrivalDate=arrivalDate, arrivalTime=arrivalTime,
                                                           aircraftCode=aircraftCode, carrierCode=carrierCode,
                                                           flightNumber=flightNumber, duration=duration)

        return response.data
    
    def busiest_month(self, airport, year, direction):
        """
        Gives the month with most traffic in an year in a particular direction
        """
        response = self.amadeus.travel.analytics.air_traffic.busiest_period.get(
                    cityCode=airport, period=year, direction=direction)

        return response.data
    

    def on_time_performance(self, airport, date):
        """
        Gives the on time performance of an airport on particular date
        """
        response = self.amadeus.airport.predictions.on_time.get(airportCode=airport, date=date)

        return response.data
    
    def availability_search(self, body):
        """
        Searches available flights for a particular booking query
        """
        response = self.amadeus.shopping.availability.flight_availabilities.post(body)
        
        return response.data