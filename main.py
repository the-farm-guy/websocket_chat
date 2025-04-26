from auth.auth import login, logout
import subprocess

prompt = input("enter a button : logout / live chat : ")

if prompt.lower() == "logout":
    logout()

elif prompt.lower() == "live chat":
    try:
        is_login = login()
        if is_login == 1:
            subprocess.run(["bash", "client.sh"], check=True)
                
        else:
            raise ValueError('invalid credentials')
            
    except subprocess.CalledProcessError as e:
            print(f"Shell script failed with error: {e}")

    