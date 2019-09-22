import json
import os
import datetime
import sys
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import argparse

# So it removes me
TURNER = "Turner Strayhorn"
# Min messages to show up
MIN_MSG = 500
messages_time_dict = dict()
directory = sys.argv[1]
directory = sys.argv[1]

# This creates a count for the number of days
def countDays(message_time_list):
	days = dict()
	num_per_day = []
	for time in message_time_list:
		if time in days:
			days[time] += 1
		else:
			days[time] = 1
	for time in message_time_list:
		num_per_day.append(days[time])
	return num_per_day

# Expects to be run like `python process_time.py ~/Downloads/facebook/messages/inbox/`
for chat_folder in os.listdir(directory):
	chat_folder_path = os.path.join(directory, chat_folder)
	if os.path.isdir(chat_folder_path):
		for chat_file in os.listdir(chat_folder_path):
			if ".json" in chat_file:
				chat_file_path = os.path.join(chat_folder_path, chat_file)
				with open(chat_file_path, 'r') as f:
					message_time_list = []
					messages_dict = json.load(f)
					if len(messages_dict["messages"]) > MIN_MSG:
						participant = [p["name"] for p in messages_dict["participants"]]
						if TURNER in participant:
							participant.remove(TURNER)
						print(participant)
						for message in messages_dict["messages"]:
							# divide into days
							message_time_list.append(message["timestamp_ms"]/(1000 * 60 * 60 * 24))
						messages_time_dict[', '.join(participant)] = (message_time_list, countDays(message_time_list))

# List of keys for legend
keys = []
for key in messages_time_dict:
	keys.append(key)
	(message_time_list, messages_per_day) = messages_time_dict[key]
	x = [datetime.datetime.fromtimestamp(message_time * 60 * 60 * 24) for message_time in message_time_list]
	plt.plot(x, messages_per_day)

fontP = FontProperties()
fontP.set_size('small')

plt.legend(keys, "Chattin' With Turner", prop=fontP)
plt.show()