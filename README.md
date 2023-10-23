# TBD - To Be Diagnosed

<p align="center">
 <img src="https://github.com/ameliefroessl/TBD/assets/9149226/a36745ff-ce4f-4bdf-a2d2-13f965694ae2" width="200">
</p>

This code was the code of the winning team for the most impactfull award in the Merantix GenAI hackathon October 12th - 13th 2023. 

Our teams application (TBD) - aims at making technical health records more accessible to everybody. The app lets you take photos of your documents and get a simplified description back. If you are not familiar with the output language you can translate the letter to your preferred language. Not only that, but you can interact with the documents by asking questions about the content of the letter.

here a small demo of what the app can do: [link](https://drive.google.com/file/d/1ZDgWtaHcMf7p8QkxOq0ArtZB1c8MZpYz/view?usp=share_link)

## Tech stack: ##

The application was powered by [firebase](https://firebase.google.com), with a [flutter](https://flutter.dev) front end and google cloud functions in the backend. 

The google cloud functions used in the backend are in the `/gcp_functions` folder.There are three main backend endpoints. 
1. `ocr` - image to text. We used the [google cloud's vision ocr](https://cloud.google.com/vision/docs/ocr) library for this.
2. `gen_ai` - Generating the simplified prognosis. We used google's [Palm 2 for text](https://forums.macrumors.com/threads/charging-a-macbook-pro-16-m1-max-with-a-67-watt-charger.2327512/) with some additional prompt engineering.
3. `translation` - translating text. We used [google cloud's text translation](https://cloud.google.com/translate/docs/basic/translating-text) for this.

The frontend code for the flutter app can be found in [this repo](https://github.com/kkotsche1/TBD_flutter_gui)

