#__utf8__
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask, request
import datetime
import sqlite3
from setuptools import setup
#implement a simple http server that can get request from and display the content client submited in the console
app = Flask(__name__)

setup(
    name='Python Simple Notebook',
    version='1.0.0',
    description='A Simple Notebook Application in Python, for internat content and file sharing.',
    author='Hegw',
    author_email='hegw@outlook.com',
    url='https://github.com/hegwout/pynb',
    packages=['pynb'],
    install_requires=[
        'flask',
        'sqlite3'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

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
        data = request.form.get('data')
        file_name = ""
        file_size = 0
        file_info = ""
        if len(request.files) > 0:
            file = request.files.get('file')
            
            if file:
                file_name = file.filename
                file_size = os.path.getsize(file.filename)

                # Save the file to the current folder
                file.save(file.filename)
                file_info = f"File Name: {file_name},<br> File Size: {file_size} bytes"
        # Display the content in the console
        print(data)

        # Connect to the SQLite database
        conn = sqlite3.connect('data.db')

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT,
                file_name TEXT,
                file_size INTEGER,
                datetime TEXT
            )
        ''')

        # Insert the data into the table
        cursor.execute('''
            INSERT INTO data (content, file_name, file_size, datetime)
            VALUES (?, ?, ?, ?)
        ''', (data, file_name, file_size, current_datetime))

        # Commit the changes to the database
        conn.commit()

        # Close the database connection
        conn.close()
        
        # Send a response back to the client, contains the content received, file name and size received, with date and time
        # Get the file name and size

        # Get the current date and time
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create the response message
        response_message = f"Content: {data}\n<br>{file_info}<br>Date and Time: {current_datetime}"
        print(response_message)

        # Send the response back to the client
        return response_message + "<hr>" + uiform

if __name__ == '__main__':
    app.run()

 