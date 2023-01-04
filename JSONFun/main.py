# JSON: Javascript Object Notation
# a data format using key/value pairs (like python dictionary)
# key (aka name): string
# e.g. "id"
# value: numeric (e.g. 1234), string (e.g. "1234AZ"), array (e.g. [1, 2, 3, 4]), boolean (e.g. true), a JSON object (e.g. nesting)

# e.g. {"id": 1234}
# e.g. {"id": {"name": "jane", "age": 20}}
import json
import pandas as pd

json_arr_str = """
[
    {
      "TimestampUTC": "2020-03-24T00:27:00Z",
      "TimestampSubjectTZ": "2020-03-23T20:27:00",
      "Calories": 0.0234859050963356,
      "HR": 0.0,
      "Lux": null,
      "Steps": 0.0,
      "Wear": true,
      "x": 0,
      "y": 35,
      "z": 0,
      "AxisXCounts": 0,
      "AxisYCounts": 35,
      "AxisZCounts": 0
    },
    {
      "TimestampUTC": "2020-03-24T00:28:00Z",
      "TimestampSubjectTZ": "2020-03-23T20:28:00",
      "Calories": 0.042274629173404,
      "HR": 0.0,
      "Lux": null,
      "Steps": 0.0,
      "Wear": true,
      "x": 44,
      "y": 63,
      "z": 55,
      "AxisXCounts": 44,
      "AxisYCounts": 63,
      "AxisZCounts": 55
    },
    {
      "TimestampUTC": "2020-03-24T00:29:00Z",
      "TimestampSubjectTZ": "2020-03-23T20:29:00",
      "Calories": 0.0,
      "HR": 0.0,
      "Lux": null,
      "Steps": 0.0,
      "Wear": true,
      "x": 0,
      "y": 0,
      "z": 0,
      "AxisXCounts": 0,
      "AxisYCounts": 0,
      "AxisZCounts": 0
    },
    {
      "TimestampUTC": "2020-03-24T00:30:00Z",
      "TimestampSubjectTZ": "2020-03-23T20:30:00",
      "Calories": 0.224122637205031,
      "HR": 0.0,
      "Lux": null,
      "Steps": 0.0,
      "Wear": true,
      "x": 193,
      "y": 334,
      "z": 71,
      "AxisXCounts": 193,
      "AxisYCounts": 334,
      "AxisZCounts": 71
    },
    {
      "TimestampUTC": "2020-03-24T00:31:00Z",
      "TimestampSubjectTZ": "2020-03-23T20:31:00",
      "Calories": 0.0154335947775919,
      "HR": 0.0,
      "Lux": null,
      "Steps": 0.0,
      "Wear": true,
      "x": 30,
      "y": 23,
      "z": 0,
      "AxisXCounts": 30,
      "AxisYCounts": 23,
      "AxisZCounts": 0
    }
  ]
"""

# Let's create a json object (which will be a python list in this case)
# using the json library
json_arr = json.loads(json_arr_str) # .loads reads from a string, while .load reads from a file
print(type(json_arr))
print(json_arr)
for arr_obj in json_arr:
    print(arr_obj["TimestampSubjectTZ"], ":", arr_obj["Calories"])
    print(type(arr_obj))
    print("*****")

# Let's open it from a file
infile = open("actigraph_data.json", "r")
json_arr = json.load(infile)
print(type(json_arr))
print(json_arr)
for arr_obj in json_arr:
    print(arr_obj["TimestampSubjectTZ"], ":", arr_obj["Calories"])
    print(type(arr_obj))
    print("*****")

# Now again with pandas
json_df = pd.read_json("actigraph_data.json")
print(json_df)

# Doesn't give us correct columns
thor_df = pd.read_json("thor_itunes_search.json")
print(thor_df)

json_obj = json.load(open("thor_itunes_search.json", "r"))
print(json_obj)
result_arr = json_obj["results"]
for results_obj in result_arr:
    track_name = results_obj["trackName"]
    # task: grab the running time in miliseconds and converts it to minutes, then check your work
    track_time_millis = results_obj["trackTimeMillis"]
    track_time_mins = track_time_millis / 1000 / 60
    print(track_name, ":", track_time_mins)
    print("*****")