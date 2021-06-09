class constants:

   # username, Type: String
   # this email id shouldn't have 2 factor authentication
   username = "<enter a valid email id>"

   # password, Type: String
   password = "<enter the appropriate password>"

   # to email addresses => Enter a valid to email address and this email id need not disable the 2 step verification, Type: String
   # to enter more than 1 email id append them spearated with a comma ex) ['example1@fmail.com', 'example2@outlook.com',...]
   to_addresses = ['<--to email address-->']
   
   # required age, Type: Int
   # change the age to 45 if required
   req_age = 18
   
   # required slot number, Type: Int
   # change the slot to 2 if u r looking for the second slot
   req_slot = 1
   
   # pin code, Type: Int
   # change the pincode to your area pincode or the interested one and if more than 1 then add comma to add the remaining. ex) [530040, 530020]
   pincode = [530040]

   # pin code api url, (Do not change this)
   pin_code_url = 'api/v2/appointment/sessions/public/findByPin'

   # number of days to check starting from today as 1, tomorrow as 2,..etc, Type: Int
   day_check_count = 3

   # sleep time is the time interval between each api request made and this has to be carefully scrutinized based on:
   # sleep time for peak time, Type: Int
   sleep_peak_time = 5

   # sleep time for non peak time, Type: Int
   sleep_non_peak_time = 30

   # peak hour start time, Type: Int
   start_time = 14

   # peak hour end time, Type: Int
   end_time = 18