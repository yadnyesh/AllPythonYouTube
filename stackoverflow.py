import requests
request = requests.get("https://drive.google.com/uc?export=download&id=1_9On2-nsBQIw3JiY43sWbrF8EjrqrR4U")
with open(developer_survey_2018.zip, "wb") as file:
    file.write(request.con)