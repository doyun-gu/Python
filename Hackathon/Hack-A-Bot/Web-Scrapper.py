# This Code is to read the location data every 0.5 second from the Camera and written by Doyun GU
# Team: Hyeongbin LEE, JaeWoo LEE, Byeongwan KANG, Doyun GU

# heading
import re                        # Redax the location
import requests                  # To send HTTP requests and receive the responses from the web server
import time                      # To read the value from the website by time
from bs4 import BeautifulSoup    # The library for parsing HTML documents and extracting information from them
from pprint import pprint

# Declare the URL
URL = "http://192.168.4.1"      # URL which is going to use

# Loop Starts; Repeat Indefinitely (unless there is a mention of "break" statement)
while True:
    # sends a GET request to the URL, gets the response content, and stores in the 'page' variable
    page=requests.get(URL)    

    # The 'BeautifulSoup' library is used to parse the HTML content of the 'page' variable and store it in the 'soup' variable
    soup = BeautifulSoup(page.content, "html.parser")

    # The 'content' variable is set to the string value of the response content
    content = str(page.content)

    # This line replaces the escape characters '\\' and '\\r' with empty strngs and also removes the closing '</body></html>' tag from the HTML content.
    # Escape characters are special characters in strings that have a specific meaning.
    # '\\n' and '\\r' are used to indicate a new line and a carriage return character respectively.
    content = content.replace("\\n", "").replace("\\r", "").replace("</body></html>'", "")

    # Thie line splits the cleaned HTML content by the '<br>' tage and discards the first two parts of the resulting list.
    # The '<br>' tag is typically used to create line breaks in HTML.
    # By splitting the content using this tag, we can extract the individual data points that we're interested in.
    content = content.split("<br>")[2:]

    # This line simply prints the extracted data points to the console, so that we can see the result
    print(content)

    # 'content' is a list of strings, where each string represents a line of text from the webpage content.
    # Each line is split by the comma (',') character and then the second
    # third and forth elements of the resulting list are assigned to the corresponding variables. 
    C1X, C1Y, C1Z = content[0].split(",")[1:]
    M2X, M2Y, M2Z = content[1].split(",")[1:]
    M24X, M24Y, M24Z = content[2].split(",")[1:]
    G43X, G43Y, G43Z = content[3].split(",")[1:]
    M27X, M27Y, M27Z = content[4].split(",")[1:]
    C0X, C0Y, C0Z = content[5].split(",")[1:]
    BX, BY, BZ = content[6].split(",")[1:]

    # Send data to Arduino via serial communication
    data = "{:.2f},{:.2f},{:.2f},{:.2f}\n".format(float(M2X), float(M2Y), float(BX), float(BY))
    ser.write(data.encode())

    # Print values to console
    print("C1X: {}, C1Y: {}, C1Z: {}".format(C1X, C1Y, C1Z))
    print("M2X: {}, M2Y: {}, M2Z: {}".format(M2X, M2Y, M2Z))
    print("M24X: {}, M24Y: {}, M24Z: {}".format(M24X, M24Y, M24Z))
    print("G43X: {}, G43Y: {}, G43Z: {}".format(G43X, G43Y, G43Z))
    print("M27X: {}, M27Y: {}, M27Z: {}".format(M27X, M27Y, M27Z))
    print("C0X: {}, C0Y: {}, C0Z: {}".format(C0X, C0Y, C0Z))
    print("BX: {}, BY: {}, BZ: {}".format(BX, BY, BZ))

    # This code execute every 0.5 second
    time.sleep(0.5)
