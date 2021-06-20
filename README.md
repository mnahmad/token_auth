![Platform](https://img.shields.io/badge/Python-3.7.7-yellow.svg?longCache=true)
![Platform](https://img.shields.io/badge/Django-2.2.16-orange.svg?longCache=true)
![Platform](https://img.shields.io/badge/DjangRest-3.12.2-red.svg?longCache=true)
![Platform](https://img.shields.io/badge/Sqlite-3.0-orange.svg?longCache=true)


This repo contains code to test Token based authentication using REST API. The code is taken from Victor Freiatas tutorial[How to Implement Token Authenrtication using Django REST Framework](https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html) and modified whereever needed . Rest of resources used are listed below 

- [Django (3.0) Crash Course Tutorails](https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)
- [Try Django Tutoorials](https://www.youtube.com/watch?v=SNXn76SI1Ks)
- [Django REST Frmwework](https://www.django-rest-framework.org/api-guide/permissions/) official website. 

The way this repo should be used. 
1. Read Victor Freiatas tutorial[How to Implement Token Authenrtication using Django REST Framework](https://simpleisbetterthancomplex.com/tutorial/2018/11/22/
2. Clone this repo
3. Install psackages 
4. Execute `python3 manage.py makemigations` and `python3 manage.py migrate` 
5. create a user to generate token 
6. Start server by using command `python3 manage.py runserver`
7. Use curl command to check authtentiation
8. Use cur command to send data with authentication 

### Instal Packages
I used virtiual env so here are the steps to install virtual env and enable it. 

The requirement.txt contains follwoing packages.  
```
Django==2.2.16
djangorestframework==3.12.2
```

Thus install it by using the following command 

```
pip3 - r requirement.txt
```

###  create a user to generate token 
Create user which will send data to server (and for which token will be generated), by using the follwoing command. 

```
python3 manage.py createsuperuser --username user_token --email user_token@example.com
```


### test REST API using

__CURL__

```
curl http://127.0.0.1:8000/hello/ -H 'Authorization: Token token-string-for-your-user'

```


### Data Entry along with token based authentication. 

The JSON which will be used to test the code is below. 

```
{
  "first_name": "Jason",
  "last_name": "Bourn",
  "mobile": "001",
  "email": "j.bourn@gmail.com",
  "state": "Washington",
  "district": "Columbia",
  "village": "bigtown",
  "block": "2"
}

```


```
# curl -d '{"first_name": "Jason","last_name": "Bourn","mobile": "001","email": "j.bourn@gmail.com","state": "Washington","district": "Columbia","village": "bigtown","block": "2"}'  -H 'Authorization: Token token-string-for-your-user'  -X POST http://127.0.0.1:8000/register/
```
