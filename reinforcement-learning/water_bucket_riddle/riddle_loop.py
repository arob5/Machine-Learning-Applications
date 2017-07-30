#
# riddle_loop.py --- Runs with Python 3
# A "game loop" for the bucket riddle, utilizing the Bucket class
# Last Modified: 7/30/2017
# Modified By: Andrew Roberts
#

"""
Possible actions:
f5 - Fill 5G bucket
f3 - Fill 3G bucket
e5 - Empty 5G bucket
e3 - Empty 3G bucket
35 - Pour 3G bucket into 5G bucket
53 - Pout 5G bucket into 3G bucket
"""

from bucket_class import Bucket

def main(): 
	solved_riddle = False
	bucket_5, bucket_3 = Bucket(5), Bucket(3)
	
	while not solved_riddle:
		print_bucket_status(bucket_5, bucket_3)
		action = input("Enter action: ")
		take_action(action, bucket_5, bucket_3)
		solved_riddle = (bucket_5.current_volume + bucket_3.current_volume == 4) 
	print("Congrats!") 

def print_bucket_status(b1, b2):
	print(b1.max_volume, "G Bucket:", b1.current_volume, "G")
	print(b2.max_volume, "G Bucket:", b2.current_volume, "G")

def take_action(input, b5, b3):
	if input == "f5":
		b5.fill_bucket()
	elif input == "f3":
		b3.fill_bucket()
	elif input == "e5":
		b5.empty_bucket()
	elif input == "e3": 
		b3.empty_bucket()
	elif input == "35":
		b3.pour(b5)
	elif input == "53":
		b5.pour(b3)
	else: 
		print("Invalid input") 	
			
main()


"""
SOLUTION

bucket_5 = Bucket(5)
bucket_3 = Bucket(3)
bucket_5.fill_bucket()    f5
bucket_5.pour(bucket_3)	  53
bucket_3.empty_bucket()   e3
bucket_5.pour(bucket_3)	  53
bucket_5.fill_bucket()    f5
bucket_5.pour(bucket_3)	  53
bucket_3.empty_bucket()   e3
"""
