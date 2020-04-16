# Made by Idan Dov Vidra

import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')

# The text the analasys will be done on          
text = "Okay. So last week, ee-done and I went to the campus. Yes. And we had sandwiches with our favorite teacher. Yes. And then we saw outside off the campus. Yes. And there I think it was a robot that was developed in one of the labs in the school. Yes. And then the robot came to ee-done and told him Yes, if I remember correctly told me a Corona virus is stronger than us. We need to work together. Robots and humankind. Yes. And then we put our hands together. And then we started to sing. Yes, I remember. Gal sang in a really high pitched voice. His favorite song? Yes. And he done started to sing. Hallelujah. Yes. And it was in the same time. So didn't they sound so good? Because it was two different songs in the same time? Yes. And we realized that we left the sandwiches and back. Yes, And this made me fall into a deep depression that I'm still not over. Yes. And then I saw it done crying, and I started to give him the sandwich. Yes. And then I saw that girl was coming at me with a sandwich, and it freaked me out of it. Yes. And I started to say ee-done, please. It's me. Remember, Gal? Yes. And then I said, You know what? For old time's sake, let's fly together to Las Vegas. Yes. And we ran to the airport and we took the first flight. We could we could Yes. And then when we get to a little Caesars, the casino Gal put all of his money and red. Yes. And then there was black way. We were homeless for a few months, gathering money against to fly back home. Yes. And then the robot from the Koran, a vision came back and told us. Told you last minute. You can still continue. All right. Okay. So that yes. And the robot told us. Listen, I like you guys so much. I'm gonna sell my own body. So you have money for the flight ticket? So, yes. And then we went with the rubber to the street. Yes. And then we found some pimps to sell them. The robot? Yes. And those pimps was, uh, had problems with technology. Yes. So we helped them using our great big hearts and minds. Yes. And then we started to get some money? Yes. And then we bought the tickets back home, went to the beach and but some sandwiches. And I think this is the"

print('Calling DetectSentiment')

# Sentiment 
json_response_sentiment_dumps = json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4)

json_response_sentiment_loads = json.loads(json_response_sentiment_dumps)

# Entities
json_response_entities_dumps = json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)

json_response_entities_loads = json.loads(json_response_entities_dumps)

# Key phrases
json_response_key_phrases_dumps = json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4)

json_response_key_phrases_loads = json.loads(json_response_key_phrases_dumps)

# Concating
merged_response = json_response_entities_loads
merged_response.update(json_response_key_phrases_loads)
merged_response.update(json_response_sentiment_loads)

# Formating
merged_response_formated = json.dumps(merged_response, sort_keys=True, indent=4)

# Printing
print(merged_response_formated)
