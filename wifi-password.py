import subprocess
import re


def wifi_SSID():
    while True:
        results = subprocess.check_output(["netsh", "wlan" , "show" , "profile"], shell=True)
        extract_names = re.findall(r"All User Profile\s*:\s*(.*)", str(results))
        for name in extract_names:
            wifi_names = re.sub(r"\\r\\n","",name)
        wifi = re.sub("All User Profile     :","", wifi_names)
        final_result = wifi.split("     ")
        print("This is a list of Wifi SSIDS:\n")
        for wifi_SSID in final_result:
            print(wifi_SSID)
        answer = input("\nWhich password of the Wi-fi do you want to know?\n")
     
        
        if answer in final_result:
            result = subprocess.check_output([f"netsh", "wlan" , "show" , "profile" ,'name=', answer, "key=clear"], shell=True, encoding="utf-8")
            match = re.search(r"Key Content\s*:\s*(.*)", str(result))
            print(match.group(1))
        else:
            print("That Wi-fi does not exist in this computer!")
        
        
        again = input("Do you want to check again? (y/n)\n")
        answer_again= again.lower()
        while answer_again not in ["y","n"]:
            print("Error! Wrong input")
            again = input("Do you want to check again? (y/n)\n")
            answer_again= again.lower()

        if answer_again == "y":
             continue
        elif answer_again == "n":
             break


wifi_SSID()