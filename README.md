<h1 align="center">Youtube-API-DRF 📊</h1>

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<p align="center">
<img src="https://i.ytimg.com/vi/JiBeoIs0vkU/hqdefault.jpg">
</p>


- Server call the **YouTube** API continuously in background **(async)** with some interval **(eg.10 secs)**

- Fetch the latest videos for eg a **predefined search query given below** 👇

```py
query = ["Cricket", "Football", "Badminton", "Tennis", "Baseball", "Chess"]
``` 

- It stores the data of videos in a database with **proper indexes**

- A **GET API** ``` http://localhost:8000/api/youtube/``` which returns the stored video data in a paginated response sorted in **descending order** of published datetime.

- It is scalable and optimised.

- **Added support** for supplying multiple API keys so that if **quota** is **exhausted** on one, it automatically uses the **next available key**.


![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Tech Stack 🚀 :
- 1. Django 
- 2. Django Rest Framework
- 3. React
- 4. Youtube Data API v3
- 5. Celery & Redis

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Setup 👨‍💻:


### 1.Virtual Environment Setup :

##### For Linux :

```bash
python3 -m venv env 
source env/bin/activate
```
##### For Windows :

```bash
py -m venv env
env\Scripts\activate
```

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

#### 2. Installing Dependencies:

```bash
pip install -r requirements.txt
```

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

#### 3. Create Database Tables and Superuser:

```bash
Note: For Windows Users Replace python3 with python

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


#### 4. Install Redis and Start Server

```bash
sudo apt-get install redis-server

sudo service redis-server start
```
- `[Options: {start|stop|restart|force-reload|status}]`

##### For Windows Users : 

Refer This Article : https://dev.to/divshekhar/how-to-install-redis-on-windows-10-3e99

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

#### 5. Run Celery Worker :


```bash
celery -A youtube worker -l INFO
```


##### For Windows Users : 
 https://stackoverflow.com/questions/37255548/how-to-run-celery-on-windows

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

#### 6. Run Server

```bash
python3 manage.py runserver
```

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

#### 8. Copy API key from [Google dev console](https://console.developers.google.com/) & Add API key 

```py
Navigate : http://localhost:8000/admin/api/apikey/
```

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

#### 9. Youtube API :

```py
Navigate : http://localhost:8000/api/youtube/
```
#### API Response `query : BaseBall`
```json
 {
            "id": 54,
            "video_title": "¡JUGAMOS AL BASEBALL EN GTA 5! 😱⚾ CARRERA EXTREMA en GTA 5 💥con GOHAN y DANI",
            "description": "Hoy VENGO a traerles un NUEVO VIDEO para el CANAL, donde estaremos JUGANDO AL BASEBALL pero... en GTA ⚾ ¿Quien ...",
            "publish_datetime": "2021-12-17T18:02:59Z",
            "thumbnail_url": "https://i.ytimg.com/vi/v_WQZ2UjGLw/default.jpg"
        },
        {
            "id": 55,
            "video_title": "What Joe Espada could bring to the table for the Mets | Baseball Night in NY | SNY",
            "description": "On Baseball Night in NY, Jim Duquette, Anthony Recker and Dan Graca discuss the Mets manager search. Duquette explains ...",
            "publish_datetime": "2021-12-17T18:00:33Z",
            "thumbnail_url": "https://i.ytimg.com/vi/zPUmJlD6Pz8/default.jpg"
        },
        {
            "id": 56,
            "video_title": "Reacting to Russell Wilson Playing Baseball",
            "description": "Merch: https://made-the-cut-baseball-designs.creator-spring.com/ Enjoy Reacting to Reacting to Russell Wilson Playing Baseball!",
            "publish_datetime": "2021-12-17T18:00:31Z",
            "thumbnail_url": "https://i.ytimg.com/vi/mLeUd34MNYA/default.jpg"
        },
```


![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


## Working Screenshots 🕵 :

#### API Response `api/youtube` :

![get-api-page](https://user-images.githubusercontent.com/56113566/146600054-c19a9bde-16d6-470d-a7a3-9266f8fb032b.png)

#### Result Objects :

![Screenshot from 2021-11-14 16-13-59](https://user-images.githubusercontent.com/56113566/146599468-f848f255-79e8-4e7c-b62a-ef25206721fe.png)

#### Validating API Keys & Check if it exhausted or not :

![Screenshot from 2021-11-14 16-14-04](https://user-images.githubusercontent.com/56113566/146599518-a07e10de-b40f-4a71-8657-615c20e9d945.png)

#### Filtering API Response based on `title`, `publish_datetime` :

![-------------------------------------------------------------](https://user-images.githubusercontent.com/56113566/146599565-20758fa4-2be0-44d8-8280-77057ded055c.png)

![-------------------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
