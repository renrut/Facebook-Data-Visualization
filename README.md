# Facebook-Data-Visualization
This repo contains script(s) to run on your downloaded data from facebook. It aims to offer fun data visualizations from your past messenger messages, posts, and whatever else.

See The following link to download your data.
https://www.facebook.com/help/1701730696756992?helpref=hc_global_nav

### Plot Messenger Messages

See who you talk to over time.

Takes a path to your messages inbox folder. Takes in your name, maximum group text size, and minimum number of messages in order to display. 
`python plot_messages.py ~/Downloads/facebook/messages/inbox/ --name 'My Name' --messages 250 --maxgroup 3`
