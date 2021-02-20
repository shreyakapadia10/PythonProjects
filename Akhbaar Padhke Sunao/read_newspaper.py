import requests
import json
from num2words import num2words


def speak(string):
    from win32com.client import Dispatch
    speaker = Dispatch("SAPI.SpVoice")
    speaker.Speak(string)


if __name__ == '__main__':
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=7efce32c119740c0ab8d11bd4a1014cc')
    response = requests.get(url)
    news = response.text
    json_data = json.loads(news)

    speak("Today's News: ")
    for i in range(1, 11):
        speak(f"The {num2words(i, ordinal='ordinal_num')} "
              f"News is from the source: {json_data['articles'][i]['source']['name']}"
              f"The News Title is: {json_data['articles'][i]['title']}"
              # f"The News Description is: {json_data['articles'][i]['description']}"
              f"You can read entire news from URL printed in console")

        print(f"You can read entire {num2words(i, ordinal='ordinal_num')} news from URL: {json_data['articles'][i]['url']}")

    speak("Have a nice day!")