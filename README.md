# TBD - To Be Diagnosed

This code was the code of the winning team for the most impactfull award in the Merantix GenAI hackathon October 12th - 13th 2023. 

Our teams application - aims at making technical health records and letter more accessible to everybody. The app lets you take photos of your documents and get a simplified description back. Not only that, but you can dynmically interact with the documents by asking questions about the content of the letter.

here a small demo of what the app can do: [link](https://drive.google.com/file/d/1ZDgWtaHcMf7p8QkxOq0ArtZB1c8MZpYz/view?usp=share_link)

## Tech stack: ##

The application was powered by [firebase](https://firebase.google.com), with a [flutter](https://flutter.dev) front end and google cloud functions in the backend. 

The google cloud functions used in the backend are in the `/gcp_functions` folder.There are three main backend endpoints. 
1. `ocr` - image to text. We used the [google cloud's vision ocr](https://cloud.google.com/vision/docs/ocr) library for this.
2. `gen_ai` - Generating the simplified prognosis. We used google's [Palm 2 for text](https://forums.macrumors.com/threads/charging-a-macbook-pro-16-m1-max-with-a-67-watt-charger.2327512/) with some additional prompt engineering.
3. `translation` - translating text. We used [google cloud's text translation](https://cloud.google.com/translate/docs/basic/translating-text) for this.

The frontend code for the flutter app can be found in `TODO`

* the 
