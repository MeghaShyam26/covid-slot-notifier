# Vaccination Slot Notifier

This application notifies when the slots are available for the particular pincode, age and slot number entered.

## Steps to use
- clone the repo
    ```
    git clone 
    ```
- install the requirements
    ```
    pip install -r requirements.txt
    ```
- Navigate to contants.py
    - Enter a valid email id which dosen't have mutli factor authentication in line 5
    - Enter a valid password in line 8
    - Enter the age you are looking for in line 12
    - Enter the slot number you are looking for in line 16
    - Enter the pincode required in line 20
- Navigate to app.py
    - Enter a valid 'to' address in line 62
    - If the mail has to be sent to more than 1 then copy the line and paste it below and change the 'to' address
    - Change the port number if required in line 92
- Run the server
    - Go to the root directory of this folder where app.py is present and run this command
    ```
    python app.py
    ```
- navigate to chrome and enter the url obtained with 
    - '/notify' => to run make requests to the api and get notifications if the slot is open
    - '/stop' => to stop making requests to the api
- primariy between 2-6 pm is where the slots are being opened so definetly have the server and hit '/notify' endpoint for the same time.

## Sample output
![Adding role](images/output.png)