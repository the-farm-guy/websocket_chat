from auth.auth import logout, logged_in, login
import subprocess

prompt = input("do you want to live chat : yes / no : ")

if prompt.lower() == "no":
    print("You will be logged out now")
    logout()

elif prompt.lower() == "yes":
    try:
        if logged_in == 0:
            login()
            
        else:
            subprocess.run(["bash", "client.sh"], check=True)
            
    except subprocess.CalledProcessError as e:
        print(f"Shell script failed with error: {e}")
            
else:
    raise ValueError("No option identified")

    