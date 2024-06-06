#__utf8__
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask, request, escape
import datetime
from setuptools import setup
#implement a simple http server that can get request from and display the content client submited in the console
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    uiform = '''
        <form method="post" enctype="multipart/form-data">
        <textarea name="data" rows="10" cols="100"></textarea><br>
        <input type="file" name="file" width="100"><br>
        <button type="submit">Submit</button>
        </form>
        '''

    if request.method == 'GET':
        # Send a response back to the client
        #
        return uiform
    
    elif request.method == 'POST':
        # Get the content from the request body
        data = escape(request.form.get('data')) 
        file_name = ""
        file_size = 0
        file_info = ""
        if len(request.files) > 0:
            file = request.files.get('file')
            print(file.filename)
            if file:
                file.save(file.filename)
                file_name = file.filename
                file_size = os.path.getsize(file.filename)
                file_info = f"File Name: {file_name},\n File Size: {file_size} bytes"
        # Display the content in the console
        print(data) 
        
        # Send a response back to the client, contains the content received, file name and size received, with date and time
        # Get the file name and size

        # Get the current date and time
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create the response message
        response_message = f"Content: <code>{data}</code>\n<br>{file_info}<br>Date and Time: {current_datetime}"
        print(response_message)

        # Send the response back to the client
        return response_message + "<hr>" + uiform

if __name__ == '__main__':
    app.run(port=8080)

 