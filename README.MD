## Speker Synthesis

---

#### Project usign the [SpeechRecognition](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition) webKit, structured with [Django](https://www.djangoproject.com) framework and published in [Heroku](http://heroku.com/).

#### You can use features like
- upload an .txt file to hear the text on it
- write something and listen usign the speech synthesis
- use the speech recognition to generate text

<h3 align="center"><a href="https://speaker-synthesis.herokuapp.com">See Demo</a></h3>

---

### Commands

```bash
        # create the virtua enviroment
        $ python3 -m venv  env
```

```bash
        # enter the virtual enviroment
        $ source env/bin/activate
```

```bash
        # install the depedencies
        $ pip3 install -r requirements.txt
```

```bash
        # generate sqlite db
        $ python manage.py migrate
```

```bash
        # create admin user for use the django panel
        $ python manage.py createsuperuser
```

```bash
        # the server will run in port 8000
        $ python manage.py runserver
```

```bash
        # for leave the virtual enviroment
        $ deactivate
```

##### Enjoy 😄