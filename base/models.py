from django.db import models

# Create your models here.


#this model for lanes there are three lanes for their unique id's i;e 101,102,103(R,B,G)
class Lane(models.Model):
	lane_type = models.PositiveIntegerField()
	lane_name = models.CharField(max_length=200)

#this model is for passenger details and store final price for that praticular passenger
class Passenger(models.Model):
	passenger_id = models.AutoField(primary_key=True)
	from_add = models.CharField(max_length=200)
	lane =  models.ForeignKey(Lane, on_delete=models.CASCADE)
	price = models.FloatField(default = True)
	to_add = models.CharField(max_length=200)
	current_date = models.DateField()
	

class RedLane(models.Model):
	red_stop_name = models.CharField(max_length=200)
	red_lane_price = models.FloatField(default = True)
	lane =  models.ForeignKey(Lane, on_delete=models.CASCADE)
	red_extra_price = models.FloatField(default = 2.5)  #this lane extra price 

class BlueLane(models.Model):
	blue_stop_name = models.CharField(max_length=200)
	lane = models.ForeignKey(Lane, on_delete=models.CASCADE)
	blue_lane_price = models.FloatField(default = True)
	blue_extra_price = models.FloatField(default = 2)#this lane extra price 

class GreenLane(models.Model):
	green_stop_name = models.CharField(max_length=200)
	lane = models.ForeignKey(Lane, on_delete=models.CASCADE)
	green_lane_price = models.FloatField(default = True)
	green_extra_price = models.FloatField(default = 3)#this lane extra price 


#this model is to show the junction of every two lanes and their id's for different lanes i;e , red lane has one junction that id has 14, & blue lane has same junction id is 10.
class Junction(models.Model):
	jun_name = models.CharField(max_length=200)
	lane_type = models.PositiveIntegerField()
	lane_type2 = models.PositiveIntegerField()	
	lane = models.ForeignKey(Lane, on_delete=models.CASCADE)
	entry_jun_lane_type_num = models.PositiveIntegerField()
	exit_jun_lane_type_num2 = models.PositiveIntegerField()

