import jwt

secret = "secret"

print(jwt.encode({ "username": "abc", "admin": "true" }, secret, algorithm="HS256"))

#eyJ0eXAiOiAiSldUIiwiYWxnIjogIkhTMjU2In0
#eyJ1c2VybmFtZSI6ICJsb2wiLCAiYWRtaW4iOiAidHJ1ZSJ9

#eyJ0eXAiOiAiSldUIiwiYWxnIjogIkhTMjU2In0.eyJ1c2VybmFtZSI6ICJsb2wiLCAiYWRtaW4iOiAidHJ1ZSJ9

#hQXAP49OV3szx+vPGTAE6jmzUwx9G1gwT+8oCmcGufw

#eyJ0eXAiOiAiSldUIiwiYWxnIjogIkhTMjU2In0.eyJ1c2VybmFtZSI6ICJsb2wiLCAiYWRtaW4iOiAidHJ1ZSJ9.DnyPk+zB1UZrABx3/CmA1cc2wRzrZC6bww5ytuxp+4U