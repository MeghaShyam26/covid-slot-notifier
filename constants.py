class constants:

   # username
   # this email id shouldn't have 2 factor authentication
   username = "<enter a valid email id>"

   # password
   password = "<enter the appropriate password>"
   
   # required age
   # change the age to 45 if required
   req_age = 18
   
   # required slot number
   # change the slot to 2 if u r looking for the second slot
   req_slot = 1
   
   # pin code
   # change the pincode to your area pincode or the interested one and if more than 1 then add comma to add the remaining. ex) [530040, 530020]
   pincode = [530040]

   # pin code api url
   pin_code_url = 'api/v2/appointment/sessions/public/findByPin'

   # number of days to check starting from today as 1, tomorrow as 2,..etc
   day_check_count = 3

   # sleep time is the time interval between each api request made and this has to be carefully scrutinized based on:
   # internet speed, parallell tasks running, compute capacity, etc.

   # sleep time when there are slots available in the previous call made
   # (Reccomendation) To check more quickly for the slot update when there are slots or at the peak time when there can be slots u can reduce the number to 1-30 
   sleep_availability_count_check = 60

   # sleep time when there are no slots available in the previosu call made
   # (Reccomendation) To check more quickly for the slot availability at the peak time or generally as well, u can reduce the number to 30-60
   sleep_availability_check = 300