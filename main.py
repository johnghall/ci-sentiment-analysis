import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from random import shuffle
sia = SentimentIntensityAnalyzer()

sample_responses = [
    "i had trouble with the login password",
    "The animations were a little too slow, as when I had to redo the activity I had to wait the couple seconds before inputting an answer I already knew.",
    "Activity setup takes too long compared to the gameplay length; gameplay does not provide enough payoff to offset the time taken to set it up.",
    "Instructions are very very unclear and could not set up image properly",
    "I just didn't know what to do with the vpn until I emailed instructor Hah.",
    "The majority of my 'issues' centered around how to obtain the information requested by each prompt. I repeatedly searched for binwalk commands to find/identify information. Often, I simply entered random commands hoping to receive information that would help me answer the question correctly (some commands used were those listed in the terminal after executing binwalk, and other commands from websites that showed commands and the information returned for each). My experience would have been improved if we were given practice on executing commands and which commands were useful.",
    "It was unclear what all I had to download from the google drive. I ended up waiting for an hour to download everything from the drive.",
    "Looking for the information for how to do the activities was hard.",
    "N/A",
    "Importing the virtual machine",
    "I believe most setup errors were my own fault. Downloading the files from drive at once renamed some of them and messed up the configuration so I would advise students to download them one-by-one or to make sure they're named properly.",
    "The tutorial by Sergio Prado had elements that I could not figure out throughout the activity. Using dd to obtain the boot image could not be uncompressed by using unlzma. This was frustrating as I couldn't tell what I was looking for. There were also multiple files in the output folder without anything telling me which one(s) were used and for what.",
    "I did not see any real problems regarding the game itself, the set up instructions were well written, but setup itself was a little daunting looking at first.",
    "Since I had already done this for another class, I was able to skip the activity setup",
    "none",
    "I did not",
    "It took awhile for file downloads no other problems/",
    "The VPN setup was giving me problems first but then it got fixed.",
    "Setting up took a little while with the instructions not being too clear.",
    "It was tough for sure. The included article on using binwalk to look at a router firmware image was not enough for me to finish the activity. I had to search for many supplemental resources, which took hours. After the activity was completed, I was able to realize my errors. If everything with binwalk went smootly at first, this could feasibly take less than 30 minutes not including setting up the virtual machine.",
    "engaging and gave step by step instructions",
    "-Engaging to the audience -Easy to understand",
    "The style is very nice, and the instructions were pretty clear.",
    "GUI and opening narrative",
    "concept and presentation are both very interesting",
    "Great idea for project but isn't my chosen method for learning",
    "Engaging and thought-provoking",
    "Engaging, thought provoking",
    "1. Engaging: the investigation aspect kept my interest 2. Grading your progress.",
    "I learned about binwalking and what each aspect, does.",
    "It had interesting concepts and making it like a game seemed cool.",
    "The UI and layout were very nice to navigate. I also liked having the freedom to choose which option of the 9 quizes to do in the order I wished",
    "It was good at keeping the user guided from topic to topic, it presented and re-covered the general concepts well in a freeform order.",
    "Explanation Learning",
    "Visually it was appealing and good for people with multiple different learning methods. The pre-test is important so that students have to actually know what they're doing before starting the main activity.",
    "The background reading really helps understand what is going on. The game aspect challenges you to succeed.",
    "It helped me practice recalling some concepts related to operating systems in a very engaging way. It was fun enough to make me want to go out of my way and look up other some of the other things you can do with binwalk.",
    "One strong aspect of this activity is that it is highly interactive. It requires the player to learn and experiment on their own in order to complete the activity. Another strong aspect of this activity was the way it was structured. This made the activity feel more realistic, and made it more engaging.",
    "Clearly defines why obtaining and encrypting this information is useful. It is visually pleasing.",
    "The listing color and flow were very strong aspects of the activity, the text speed was also nice, the flow in general was a nice pace.",
    "Definitions were helpful. The links were nice for new content.",
    "steps of the game and the procedure",
    "It was engaging and kept track of the score, it always showed my score",
    "First it's pretty interactive and colorful there is motivation the second is that it requires you to learn.",
    "Really like the usefulness of the information we achieved, Also got very involved in the game",
    "Graphics looked good and it gives the user a chance to choose what thing they want to learn first.",
    "Engaging, difficult, makes you self-teach which is often the best way to learn.",
    "Short but informative, gamifying learning keeps users engaged"
]


def get_sentiment(response: str) -> bool:
    """True if tweet has positive compound sentiment, False otherwise."""
    score = sia.polarity_scores(response)["compound"]
    if score <= -.2:
        return "Negative"
    elif score < .2:
        return "Neutral"
    else:
        return "Positive"


shuffle(sample_responses)

sorted_sentiments = {"Negative": [], "Neutral": [], "Positive": []}

for response in sample_responses:
    sorted_sentiments[get_sentiment(response)].append(response)

print("Negative: \n")
for response in sorted_sentiments["Negative"]:
    print(response)

print("\n \n")

print("Neutral: \n")
for response in sorted_sentiments["Neutral"]:
    print(response)

print("\n \n")

print("Positive: \n")
for response in sorted_sentiments["Positive"]:
    print(response)