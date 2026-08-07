import requests

print()
print("GitPrint v1.0.0")
user = input("Enter username: ")

def getuser(name):
    global request
    print()
    url=f"https://api.github.com/users/{name}"    
    request=requests.get(url)
    pinfo = request.json()
    return pinfo


uinfo = getuser(user)
if request.status_code == 404:
    print("User could not be found. Try again.")
else:
    print("~ ACCOUNT")
    print(f"Name: {uinfo["name"]}")
    print(f"Username: {uinfo["login"]}")
    print(f"ID: {uinfo["id"]}")
    print(f"Location: {uinfo["location"]}")
    print(f"Bio: '{uinfo["bio"]}' ")
    print()
    print("~ SOCIALS")
    print(f"Email: {uinfo["email"]}")
    print(f"Twitter (X): {uinfo["twitter_username"]}")
    print(f"Company: {uinfo["company"]}")
    print()
    print("~ MISC / INFO")
    cdate = uinfo["created_at"]
    print(f"Account created at: {cdate.replace("T"," ").replace("Z","")}")
    update = uinfo["updated_at"]
    print(f"Account updated at: {update.replace("T"," ").replace("Z","")}")
    print(f"Followers: {uinfo["followers"]}")
    print(f"Following: {uinfo["following"]}")
    print(f"Public repo(s): {uinfo["public_repos"]}")
    print(f"Public gist(s): {uinfo["public_gists"]}")
    print()
