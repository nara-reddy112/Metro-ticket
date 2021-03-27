from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
import datetime
from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import IsAuthenticated 
# Create your views here.

#to get single lane

class LaneDisplayView(APIView):
    def get(self,request):
        try:
            import pdb;pdb.set_trace()
            lane_id = request.query_params.get('lane_type')
            lane_name = Lane.objects.filter(lane_type = lane_id).values_list('lane_name')

            data = lane_name
            message = 'pass'
        except Exception as e:
            data = ''
            message = 'fail'
            print(e)
        
        content={
            'message':message,
            'data':data
        }

        return Response(content)

#to get all lanes 


class AllLaneDisplayView(APIView):
    def get(self,request):
        try:
            import pdb;pdb.set_trace()
            lane_name = Lane.objects.values()
            data = lane_name
            message = 'pass'
        except Exception as e:
            data = ''
            message = 'fail'
            print(e)
        
        content={
            'message':message,
            'data':data
        }

        return Response(content)

#to get whenever passenger travels in the same lane without changes any lane.

class PassengerJourny(APIView):
    def get(self,request):
        try:
            import pdb;pdb.set_trace()
            pass_id = request.query_params.get('passenger_id')
            pass_from = request.query_params.get('passenger_from')
            pass_to = request.query_params.get('passenger_to')
            pass_route_type = request.query_params.get('route_type')
            res = []
            price_count = []
            dt_now = datetime.datetime.now()
            timestamp = dt_now.replace(tzinfo=timezone.utc).timestamp()
            datetimestamp =datetime.datetime.fromtimestamp(int(timestamp),tz=timezone.utc)
            passenger = list(Lane.objects.filter(lane_type = pass_route_type).values_list('lane_name',flat = True))
            if passenger == ['bluelane']:
                passen_from = BlueLane.objects.filter(blue_stop_name = pass_from).values_list('id',flat = True)
                passen_to = BlueLane.objects.filter(blue_stop_name = pass_to).values_list('id',flat = True)
                total_stations =  abs(passen_from[0] - passen_to[0])+1
                res.append(total_stations)
                
                if total_stations <= 3:
                    p = 10
                    # price = Passenger.objects.create(price = p,current_date = datetimestamp,from_add =pass_from, to_add = pass_to,lane = pass_route_type,passenger_id = pass_id)
                    instance = Passenger.objects.get(passenger_id = pass_id)
                    instance.price = p
                    instance.save()
                elif total_stations > 3:
                    stations= total_stations - 3

                    price =  BlueLane.objects.values_list('blue_extra_price')
                    p = 10 + stations(price)
                    # total_price =  Passenger.objects.create(price = prices,current_date = datetimestamp,lane_id = pass_route_type,from_add =pass_from, to_add = pass_to,lane = passenger , passenger_id = pass_id)
                    instance = Passenger.objects.get(passenger_id = pass_id)
                    instance.price = p
                    instance.save()
                    price_count.append(p)


            elif passenger == ['redlane']:
                passen_from = RedLane.objects.filter(red_stop_name = pass_from).values_list('id',flat = True)
                passen_to = RedLane.objects.filter(red_stop_name = pass_to).values_list('id',flat = True)
                total_stations =  abs(passen_from[0] - passen_to[0])+1
                res.append(total_stations)
                if total_stations <= 3:
                    p = 10
                    # price = Passenger.objects.create(price = p,current_date = datetimestamp,from_add =pass_from, to_add = pass_to,lane = pass_route_type,passenger_id = pass_id)
                    instance = Passenger.objects.get(passenger_id = pass_id)
                    instance.price = p
                    instance.save()
                elif total_stations > 3:
                    stations= total_stations - 3

                    price =  RedLane.objects.values_list('red_extra_price')
                    p = 10 + stations(price)
                    # total_price =  Passenger.objects.create(price = prices,current_date = datetimestamp,lane_id = pass_route_type,from_add =pass_from, to_add = pass_to,lane = passenger , passenger_id = pass_id)
                    instance = Passenger.objects.get(passenger_id = pass_id)
                    instance.price = p
                    instance.save()
                    price_count.append(p)


            elif passenger == ['greenlane']:
                passen_from = GreenLane.objects.filter(green_stop_name = pass_from).values_list('id',flat = True)
                passen_to = GreenLane.objects.filter(green_stop_name = pass_to).values_list('id',flat = True)
                total_stations =  abs(passen_from[0] - passen_to[0])+1
                res.append(total_stations)
                if total_stations <= 3:
                    p = 10
                    # price = Passenger.objects.create(price = p,current_date = datetimestamp,from_add =pass_from, to_add = pass_to,lane = pass_route_type,passenger_id = pass_id)
                    instance = Passenger.objects.get(passenger_id = pass_id)
                    instance.price = p
                    instance.save()
                elif total_stations > 3:
                    stations= total_stations - 3

                    price =  GreenLane.objects.values_list('green_extra_price')
                    p = 10 + stations(price)
                    # total_price =  Passenger.objects.create(price = prices,current_date = datetimestamp,lane_id = pass_route_type,from_add =pass_from, to_add = pass_to,lane = passenger , passenger_id = pass_id)
                    instance = Passenger.objects.get(passenger_id = pass_id)
                    instance.price = p
                    instance.save()
                    price_count.append(p)



                
            data = price_count
            message = 'pass'
        except Exception as e:
            data = ''
            message = 'fail'
            print(e)

        content={
            'message':message,
            # 'data':data
        }

        return Response(content)

# class MergeLane1(APIView):
#     def get
#         Reedlan.lane_type ==

def multilane(entry_lane_type,pass_from,pass_to,pass_id):
    res = []
    price_count = []
    dt_now = datetime.datetime.now()
    timestamp = dt_now.replace(tzinfo=timezone.utc).timestamp()
    datetimestamp =datetime.datetime.fromtimestamp(int(timestamp),tz=timezone.utc)
    entry_junc_name = Junction.objects.filter(lane_type = entry_lane_type,lane_type2 = exit_lane_type).values_list('jun_name','jun_lane_type_num')
    
    passenger = list(Lane.objects.filter(lane_type = entry_lane_type).values_list('lane_name',flat = True))
    if passenger == ['bluelane']:
        passen_from = BlueLane.objects.filter(blue_stop_name = pass_from).values_list('id',flat = True)
        passen_to = BlueLane.objects.filter(blue_stop_name = entry_junc_name[0][0]).values_list('id',flat = True)
        total_stations =  abs(passen_from[0] - passen_to[0])+1
        res.append(total_stations)
        
        if total_stations <= 3:
            p = 10
            # price = Passenger.objects.create(price = p,current_date = datetimestamp,from_add =pass_from, to_add = pass_to,lane = pass_route_type,passenger_id = pass_id)
            instance = Passenger.objects.get(passenger_id = pass_id)
            instance.price = p
            instance.save()
        elif total_stations > 3:
            stations= total_stations - 3

            price =  BlueLane.objects.values_list('blue_extra_price')
            p = 10 + stations(price)
            # total_price =  Passenger.objects.create(price = prices,current_date = datetimestamp,lane_id = pass_route_type,from_add =pass_from, to_add = pass_to,lane = passenger , passenger_id = pass_id)
            instance = Passenger.objects.get(passenger_id = pass_id)
            instance.price = p
            instance.save()
            price_count.append(p)


    elif passenger == ['redlane']:
        passen_from = RedLane.objects.filter(red_stop_name = pass_from).values_list('id',flat = True)
        passen_to = RedLane.objects.filter(red_stop_name = pass_to).values_list('id',flat = True)
        total_stations =  abs(passen_from[0] - passen_to[0])+1
        res.append(total_stations)
        if total_stations <= 3:
            p = 10
            # price = Passenger.objects.create(price = p,current_date = datetimestamp,from_add =pass_from, to_add = pass_to,lane = pass_route_type,passenger_id = pass_id)
            instance = Passenger.objects.get(passenger_id = pass_id)
            instance.price = p
            instance.save()
        elif total_stations > 3:
            stations= total_stations - 3

            price =  RedLane.objects.values_list('red_extra_price')
            p = 10 + stations(price)
            # total_price =  Passenger.objects.create(price = prices,current_date = datetimestamp,lane_id = pass_route_type,from_add =pass_from, to_add = pass_to,lane = passenger , passenger_id = pass_id)
            instance = Passenger.objects.get(passenger_id = pass_id)
            instance.price = p
            instance.save()
            price_count.append(p)


    elif passenger == ['greenlane']:
        passen_from = GreenLane.objects.filter(green_stop_name = pass_from).values_list('id',flat = True)
        passen_to = GreenLane.objects.filter(green_stop_name = pass_to).values_list('id',flat = True)
        total_stations =  abs(passen_from[0] - passen_to[0])+1
        res.append(total_stations)
        if total_stations <= 3:
            p = 10
            # price = Passenger.objects.create(price = p,current_date = datetimestamp,from_add =pass_from, to_add = pass_to,lane = pass_route_type,passenger_id = pass_id)
            instance = Passenger.objects.get(passenger_id = pass_id)
            instance.price = p
            instance.save()
        elif total_stations > 3:
            stations= total_stations - 3

            price =  GreenLane.objects.values_list('green_extra_price')
            p = 10 + stations(price)
            # total_price =  Passenger.objects.create(price = prices,current_date = datetimestamp,lane_id = pass_route_type,from_add =pass_from, to_add = pass_to,lane = passenger , passenger_id = pass_id)
            instance = Passenger.objects.get(passenger_id = pass_id)
            instance.price = p
            instance.save()
            price_count.append(p)

    return price_count




#to get whenever passanger changes one lane to another lane .

class MergeLane(APIView):
    def get(self,request):
        try:
            pass_id = request.query_params.get('passenger_id')
            pass_from = request.query_params.get('passenger_from')
            pass_to = request.query_params.get('passenger_to')
            entry_lane_type = request.query_params.get('pass_lane_type')
            exit_lane_type = request.query_params.get('exit_lane_type')

           
            # pass_from_type = list(Lane.objects.filter(lane_type = entry_lane_type).values_list('lane_name',flat = True))
            # passen_from = BlueLane.objects.filter(blue_stop_name = pass_from).values_list('id',flat = True)
            # passen_to = BlueLane.objects.filter(blue_stop_name = entry_junc_name[0][0]).values_list('id',flat = True)



            # res = []
            # price_count = []
            # dt_now = datetime.datetime.now()
            # timestamp = dt_now.replace(tzinfo=timezone.utc).timestamp()
            # datetimestamp =datetime.datetime.fromtimestamp(int(timestamp),tz=timezone.utc)
            # passenger = list(Lane.objects.filter(lane_type = entry_lane_type).values_list('lane_name',flat = True))
            # if passenger == ['bluelane']:
            #     passen_from = BlueLane.objects.filter(blue_stop_name = pass_from).values_list('id',flat = True)
            #     passen_to = BlueLane.objects.filter(blue_stop_name = entry_junc_name[0][0]).values_list('id',flat = True)
            #     total_stations =  abs(passen_from[0] - passen_to[0])+1
            #     res.append(total_stations)
                
            #     if total_stations <= 3:
            #         p = 10
            #         # price = Passenger.objects.create(price = p,current_date = datetimestamp,from_add =pass_from, to_add = pass_to,lane = pass_route_type,passenger_id = pass_id)
            #         instance = Passenger.objects.get(passenger_id = pass_id)
            #         instance.price = p
            #         instance.save()
            #     elif total_stations > 3:
            #         stations= total_stations - 3

            #         price =  BlueLane.objects.values_list('blue_extra_price')
            #         p = 10 + stations(price)
            #         # total_price =  Passenger.objects.create(price = prices,current_date = datetimestamp,lane_id = pass_route_type,from_add =pass_from, to_add = pass_to,lane = passenger , passenger_id = pass_id)
            #         instance = Passenger.objects.get(passenger_id = pass_id)
            #         instance.price = p
            #         instance.save()
            #         price_count.append(p)


            # elif passenger == ['redlane']:
            #     passen_from = RedLane.objects.filter(red_stop_name = pass_from).values_list('id',flat = True)
            #     passen_to = RedLane.objects.filter(red_stop_name = pass_to).values_list('id',flat = True)
            #     total_stations =  abs(passen_from[0] - passen_to[0])+1
            #     res.append(total_stations)
            #     if total_stations <= 3:
            #         p = 10
            #         # price = Passenger.objects.create(price = p,current_date = datetimestamp,from_add =pass_from, to_add = pass_to,lane = pass_route_type,passenger_id = pass_id)
            #         instance = Passenger.objects.get(passenger_id = pass_id)
            #         instance.price = p
            #         instance.save()
            #     elif total_stations > 3:
            #         stations= total_stations - 3

            #         price =  RedLane.objects.values_list('red_extra_price')
            #         p = 10 + stations(price)
            #         # total_price =  Passenger.objects.create(price = prices,current_date = datetimestamp,lane_id = pass_route_type,from_add =pass_from, to_add = pass_to,lane = passenger , passenger_id = pass_id)
            #         instance = Passenger.objects.get(passenger_id = pass_id)
            #         instance.price = p
            #         instance.save()
            #         price_count.append(p)


            # elif passenger == ['greenlane']:
            #     passen_from = GreenLane.objects.filter(green_stop_name = pass_from).values_list('id',flat = True)
            #     passen_to = GreenLane.objects.filter(green_stop_name = pass_to).values_list('id',flat = True)
            #     total_stations =  abs(passen_from[0] - passen_to[0])+1
            #     res.append(total_stations)
            #     if total_stations <= 3:
            #         p = 10
            #         # price = Passenger.objects.create(price = p,current_date = datetimestamp,from_add =pass_from, to_add = pass_to,lane = pass_route_type,passenger_id = pass_id)
            #         instance = Passenger.objects.get(passenger_id = pass_id)
            #         instance.price = p
            #         instance.save()
            #     elif total_stations > 3:
            #         stations= total_stations - 3

            #         price =  GreenLane.objects.values_list('green_extra_price')
            #         p = 10 + stations(price)
            #         # total_price =  Passenger.objects.create(price = prices,current_date = datetimestamp,lane_id = pass_route_type,from_add =pass_from, to_add = pass_to,lane = passenger , passenger_id = pass_id)
            #         instance = Passenger.objects.get(passenger_id = pass_id)
            #         instance.price = p
            #         instance.save()
            #         price_count.append(p)

            price_count_entry =multilane(entry_lane_type,pass_from,pass_to,pass_id)

            #Has a passanger changes one lane to another lane junction will become 1st exit and also sencond entry point(exit point treated as entry point when lane to lane
            #here functions are called  twice  (one is for entry and exit that exit will now become entry for other lane and we have final exit,so here we have two entries and two exits)


            
            price_count_exit = multilane(exit_lane_type,pass_from,pass_to,pass_id)
            data = price_count_entry + price_count_exit

            message = 'pass'

        except Exception as e:
            print(e)
            message = 'fail'
            data = ''

        content={
            'message':message,
            'data':data
        }

        return Response(content)



