# Imports / dependencies
from urllib.request import urlopen
import json
import os #for clearing screen

# Clear screen upon launching applet
os.system('cls||clear')

print(
"\n",
"                   +++\n",
"            +++ __+++++\n",
"       ___/+++++    \+\n",
"     /      +++      |\n",
"   /         |%\____/++\n",
"   |         /%%%% +++\n",
"   \        |%%%%%%%_\n",
"     \_____/%%%%%%%%  \\\n",
"    | /%%%%%%%%%%%     |\n", 
"    _/__  %%%%%%%      |\n",  
"   /    \     |\______/\n",
"  |      |    /    |\n",
"   \____/____/\___/\n",
"\n",
"FOLDING@HOME STAT CHECKER\n",
"         - by -\n", 
"      TimelessFez\n",
"\nWelcome!\n",
     )

# Username
username = input("What is your F@H username? ")
str(username)

# API source
apisource = "https://api2.foldingathome.org/user/"
str(apisource)

url = apisource + username

# Open connection, and store values
response = urlopen(url)

# Store JSON info from URL
json_data = json.loads(response.read())

# Close connection, as we have already obtained the data
response.close()

#  --- Output ---  
print(
        "\n---------------------------------",
        "\n #\tUser",
        "\n---------------------------------",
        "\nName:\t\t", (json_data['name']),
        "\nID:\t\t", (json_data['id']),
        "\nScore:\t\t", "{:,d}".format((json_data['score'])),
        "\nWUs:\t\t", "{:,d}".format((json_data['wus'])),
     )

# Variables
#x = 0   #default
#selection = input("\nWhat team would you like to view? (e.g. 1) ")


#int(selection)
#int(x)
#x = int(selection) - 1

# Store requested team info in variable (dict)
#data = json_data['teams'][x]

# Header - for visual 
print(
        "\n---------------------------------",
        "\n #\tContributions",
        "\n---------------------------------"
     )

for data in json_data['teams']:
    print("\nTeam No.:\t", data['team'])
    print("Team Name:\t", data['name'])
    print("User Score:\t", "{:,d}".format(data['score']))
    print("Complete WUs:\t", "{:,d}".format(data['wus']))
    # Error handling
    def iferror(success, failure, *exceptions):
        try:
            return success()
        except exceptions or Exception:
            return failure

    # Error handling, for if API provides no displayable value
    def novalue():
        return print("Last WU:\t", data['last'])
        # If error, show this instead (below)
    print (iferror(novalue, "Last WU:\t N/A"))
    
    # For visual purposes (placed at the end of output, for team data)
    print("\n---------------------------------")
print("==============-end-==============")
