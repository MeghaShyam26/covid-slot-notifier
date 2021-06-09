import flask
import smtplib
import requests
import json
from datetime import datetime, timedelta
import time
from constants import constants
import uuid
app = flask.Flask(__name__)

''' GET request '''
# headers
headers = {
    'Content-type': 'application/json',
}

# request type
method = "GET"

# flag to check if requests should be made
operation_check = True

# flag to check if a mail was sent for an availability
mail_check = {}

def operation():

    global mail_check

    # var to load the metadata if the slots are available to send a mail
    text = ''

    # making request to the number of days mentioned 
    for day in range(constants.day_check_count):
        
        # changing the date according to the day change
        today = (str(datetime.now() + timedelta(days=day)).split(' ')[0]).split('-')
        
        scraped_date = "{}-{}-{}".format(today[2], today[1], today[0])

        if (scraped_date not in mail_check.keys()):
            mail_check[scraped_date] = {}

        # parsing through all the pincodes mentioned
        for pincode in constants.pincode:
            url = "https://cdn-api.co-vin.in/{}?pincode={}&date={}-{}-{}".format(constants.pin_code_url, pincode, today[2], today[1], today[0])
            
            # making an api request
            response =  requests.request(method, url)
            result = json.loads(response.text)
            sessions = result["sessions"]
            
            # parsing through the sessions from the api
            for session in sessions:
                
                # checking if the age limit of this session is under the required age
                if (session['min_age_limit']==constants.req_age):

                    # checking if the hospital already exists, if not append it to the dictionary
                    if (session['name']+session['address'] not in mail_check[scraped_date].keys()):
                        mail_check[scraped_date][session['name']+session['address']] = 0
                    
                        # checking if the available slots are greater than 0
                        if (session['available_capacity_dose{}'.format(constants.req_slot)]!=0):
                            
                            # checking if already a notification has been sent fot the recent slot release of that hospital
                            if (mail_check[scraped_date][session['name']+session['address']] == 0):
                                
                                mail_check[scraped_date][session['name']+session['address']] = 1
                                text = text + 'hospital:{}, address:{}, date:{}, age_limit:{}, available dose1 count:{}, available dose2 count:{}, fee:{}, vaccine:{}, slots:{}.  '.format(session['name'], session['address'], session['date'], session['min_age_limit'], session['available_capacity_dose1'], session['available_capacity_dose2'], session['fee'], session['vaccine'], session['slots'])
                                
                        # if the available slots are 0 for that hospital then the flag is made 0 to send notification on fresh allotment
                        else:
                            mail_check[scraped_date][session['name']+session['address']] = 0
                            
    # checking the text is empty to see if the slots are available to send a notification via email
    if (text != ''):
        # message for the email
        text = text + '      navigate to  https://selfregistration.cowin.gov.in/ and book the slot'
        # subject for the email
        subject = 'covid vaccine slot update id:' + str(uuid.uuid4())
        # combined message and subject for the email
        message = 'Subject: {}\n\n{}'.format(subject, text)
        # logging into the from email id
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(constants.username, constants.password)
        # enter a valid to address
        server.sendmail(constants.username,"<to address>", message)
        server.quit()
        print('[INFO] Mail sent')
        return 'exists'
    return 'not-exists'

# notify route points to the notification route
@app.route('/notify', methods=['GET'])
def main():
    global operation_check

    operation_check = True
    while operation_check:
        # extarcting the current hour
        hour = int((str(datetime.now()).split(' ')[-1]).split(':')[0])
        operation()
        sleep_count = constants.sleep_non_peak_time
        # checking if the current hour is peak hour or not
        if (hour >= constants.start_time and hour <= constants.end_time):
            sleep_count = constants.sleep_peak_time
        time.sleep(sleep_count)
    return 'success'

# stop route points to stop hitting the url
@app.route('/stop', methods=['GET'])
def stop_operations():
    global operation_check
    operation_check = False
    return 'success'

# enter a port number of choice if hosted locally or 8080 if posting via docker or other cloud/online service and make the host=0.0.0.0
if __name__ == "__main__":
    app.run(port = 8001)