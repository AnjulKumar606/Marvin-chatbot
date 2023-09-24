# Marvin: Your Sarcasm-Infused Coding Companion

## Description
Say Hi to Marvin, the chatbot with a twist of sarcasm and a love for all things coding! Marvin is your personal coding companion designed to make your programming journey not only informative but also incredibly entertaining. Whether you're a budding software student or an experienced coder, Marvin is here to add humor and wit to your coding conversations.

## DEMO


https://github.com/AnjulKumar606/Marvin-chatbot/assets/92917310/0377ab57-66d2-4a24-a709-e06f77742a49

## Table of Contents
- [Description](#description)
- [Demo](#demo)
- [What Marvin Does](#what-marvin-does)
- [Tech Stacks Used](#tech-stacks-used)
- [How to Run MARVIN](#how-to-run-marvin)
- [How to Train Marvin on Your Database](#how-train-marvin-on-your-database)


## What Marvin Does
**-**  **Casual Chats:** Marvin engages in relaxed conversations, making coding discussions enjoyable.

**-** **Coding Challenges:** It provides coding problems to help you practice and improve your coding skills.

**-** **Tech Updates:** You'll stay informed about the latest tech news, with a touch of humor.

**-** **Coding Advice:** Marvin offers practical tips and tricks to assist with coding challenges.

**-** **Acknowledges Achievements:** It celebrates your coding successes, big or small.

**-** **Tech Facts:** Marvin shares interesting tech facts to expand your knowledge.

## Tech Stacks Used
The following tech stacks used to create Marvin :
- **NumPy:** Used for numerical operations and data handling.
- **TensorFlow:** Empowers Marvin with machine learning capabilities for natural language processing.
- **NLTK (Natural Language Toolkit):** Enhances Marvin's language understanding and text processing abilities.
- **Pickle:** Utilized for saving and loading chatbot-related data, ensuring that your interactions with Marvin are always memorable.


## How to Run MARVIN
1. **Download this repo:** Simply download the files of this repo (Marvin is already trained with the data base present in the **`students.json`** )

2. **RUN Chatbot.py:** Run **`Chatbot.py`** in the terminal

3. **Interaction with Marvin** Simply start a conversation with Marvin, by typing in the terminal. Ask about coding challenges, seek coding advice, request a tech update, or simply engage in witty banter. 

## How train Marvin on your Database
1. **Insert Database:** insert a json file of structured as shown below and update the file name that is being used for the training in both the code of Chatbot.py and Training.py (make sure to name the objects properly)

```json
{
    "intents": [
        {
            "tag": "greetings",
            "patterns": [
                "Hey there!",
                "Hello, software genius!",
                "Well, well, look who's here!",
            ],
            "responses": [
                "Hey! Ready for some code and sarcasm?",
                "Hello, fellow code wrangler!",
                "Well, aren't you the tech-savvy one!",
            ]
        },
        {
            "tag": "farewell",
            "patterns": [
                "Goodbye for now, chatbot!",
                "Time to close the code editor.",
                "Signing off for now!"
            ],
            "responses": [
                "Farewell, coding maestro! Don't forget to save your work!",
                "Catch you on the flip side, coding virtuoso!",
                "See you soon, and remember, Ctrl+S is your friend!"
            ]
        }
    ]
}
```

2. **RUN Training.py:** Run **`Training.py`** in the terminal to train on the new database. You can also change the neural schema of the A.I. to your liking.

3. **RUN Chatbot.py:** Run **`Chatbot.py`** in the terminal

3. **Interaction with the newly trained model:** Simply start a conversation with it, by typing a conversation in the terminal.


