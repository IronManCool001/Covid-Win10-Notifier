from confirmed import confirmed_cases
from deaths import death_cases
from recovered import recovered_cases
import win10toast as w

toast = w.ToastNotifier()

def showInfo(country):
    confirmed_cases(country)
    death_cases(country)
    recovered_cases(country)
    message=f"Confirmed cases of {country.title()}: {confirmed_cases.confirmed} \nNumber of recovery({country.title()}): {recovered_cases.recovered} \nNumber of deaths in {country.title()}: {death_cases.deaths} "
    toast.show_toast("Covid", message, duration=5, icon_path="C:\\Users\\Devaditya\\Desktop\\Python\\experiments\\api\\covid\\covid.ico")

if __name__ == "__main__":
    c = input("Enter country name: \n")
    showInfo(c)
    print("Press enter to exit")
    input("")
