#
# bucket_class.py
# A class defining a bucket that can hold water to be used in implementing the water bucket riddle
# Last Modified: 7/30/2017
# Modified By: Andrew Roberts
#

class Bucket():
	def __init__(self, max_volume):
		self.max_volume = max_volume
		self.current_volume = 0

	@classmethod
	def empty_all_buckets(cls):
		""" Sets current_volume of all bucket instances to 0 """
		cls.current_volume = 0

	def fill_bucket(self):
		""" Sets current_volume of bucket instance to max_volume """
		self.current_volume = self.max_volume

	def empty_bucket(self):
		""" Sets current_volume of bucket instance to 0 """
		self.current_volume = 0

	def pour(self, to_bucket): 
		""" Pours as much water as possible from self to to_bucket """
		available_space = to_bucket.max_volume - to_bucket.current_volume

		if self.current_volume >= available_space:
			pour_amt = available_space
		else:
			pour_amt = self.current_volume

		self.current_volume -= pour_amt
		to_bucket.current_volume += pour_amt

