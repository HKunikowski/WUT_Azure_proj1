endpoint = 'http://6b61b730-66d6-4787-ac7b-5d6ce93d15b1.northeurope.azurecontainer.io/score'
key = 'VHqfc8xKuxNtidihPnUK1PRerHtPF62V'

import urllib.request
import json
import os
import keyboard

selected = 1

menu_options = {
    1: 'Begin prediction',
    2: 'About',
    3: 'Exit',
}

def is_number(x):
	try: 
		float(x)
		ret = True
	except:
		ret = False
	return ret
 
def is_integer(x):
	try: 
		int(x)
		ret = True
	except:
		ret = False
	return ret

def show_menu():
	os.system('cls')
	print("===========================")
	print("Check your heart condition!")
	print("===========================")
	print("Choose an option:")
	for key in menu_options.keys():
		print("{1} {0}. {3} {2}".format(key, ">" if selected == key else " ", "< "if selected == key else " ", menu_options[key]))

def up():
    global selected
    if selected == 1:
        return
    selected -= 1
    show_menu()

def down():
    global selected
    if selected == 3:
        return
    selected += 1
    show_menu()

def predict():
	input("Ready...")
	os.system('cls')
	print("What is your Age in years?")
	while(True):	
		age = input("Age: ")
		if (is_integer(age)):
			break
		else:
			print("Wrong Answer. Try Again.")

	
	os.system('cls')
	print("What is your sex?")
	while(True):
		sex = input("Sex (M/F): ")
		if (sex == 'M' or sex == 'm'):
			sex = 1
			break
		elif (sex == 'F' or sex == 'f'):
			sex = 0
			break
		
		else:
			print("Wrong Answer. Try Again.")

	os.system('cls')
	print("What kind of chest pain type do you have?")
	print("Type: ")
	print("TA for Typical Angina")
	print("ATA for Atypical Angina")
	print("NAP for Non-Anginal Pain")
	print("ASY for Asymptomatic")
	while(True):
		x0 = input("Chest pain type: ")
		if (x0 == "TA" or x0 == "ta"):
			x0_TA = 1
			x0_ATA = 0
			x0_NAP = 0
			x0_ASY = 0
			break
		if (x0 == "ATA" or x0 == "ata"):
			x0_TA = 0
			x0_ATA = 1
			x0_NAP = 0
			x0_ASY = 0
			break
		if (x0 == "NAP" or x0 == "nap"):
			x0_TA = 0
			x0_ATA = 0
			x0_NAP = 1
			x0_ASY = 0
			break
		if (x0 == "ASY" or x0 == "asy"):
			x0_TA = 0
			x0_ATA = 0
			x0_NAP = 0
			x0_ASY = 1
			break
		else:
			print("Wrong Answer. Try Again.")
	
	
	os.system('cls')
	print("What is your Resting Blood Pressure:?")
	while(True):
		resting_bp = input("Resting Blood Pressure [mm Hg]: ")
		if (is_integer(resting_bp)):
			break
		else:
			print("Wrong Answer. Try Again.")

	
	os.system('cls')
	print("What is your cholesterol?")
	while(True):
		cholesterol = input("Cholesterol [mm/dl]: ")
		if (is_integer(cholesterol)):
			break
		else:
			print("Wrong Answer. Try Again.")

	
	os.system('cls')
	print("What is your Fasting Blood Sugar?")
	print("Type:")
	print("1: if FastingBS > 120 mg/dl")
	print("0: otherwise")
	while(True):
		fasting_bs = input("Fasting Blood Sugar: ")
		if (fasting_bs == "1"):
			break
		elif (fasting_bs == "0"):
			break
		else:
			print("Wrong Answer. Try Again.")

	os.system('cls')
	print("What is your resting electocardiogram results?")
	print("Type:")
	print("NORMAL")
	print("ST for having ST-T wave abnormality")
	print("LVH for showing probable or definite left ventricular hypertrophy by Estes' criteria")
	while(True):
		x2 = input("Resting electrocardiogram results: ")
		if (x2 == "NORMAL" or x2 == "normal" or x2 == "Normal"):
			x2_Normal = 1
			x2_ST = 0
			x2_LVH = 0
			break
		elif (x2 == "LVH" or x2 == "lvh"):
			x2_Normal = 0
			x2_LVH = 1
			x2_ST = 0
			break
		elif (x2 == "ST" or x2 == "st"):
			x2_LVH = 0
			x2_Normal = 0
			x2_ST = 1
			break
		else:
			print("Wrong Answer. Try Again.")

		
	os.system('cls')
	print("What is your Maximum Heart Rate achieved?")
	print("Numeric value between 60 and 202")
	while(True):
		max_hr = input("MaxHR: ")
		if (is_integer(max_hr)):
			break
		else:
			print("Wrong Answer. Try Again.")

	
	os.system('cls')
	print("Do you have excersice angina?")
	while(True):	
		excersise_angina = input("(Y/N): ")
		if (excersise_angina == 'y' or excersise_angina == 'Y'):
			excersise_angina = "true"
			break
		elif (excersise_angina == 'n' or excersise_angina == 'N'):
			excersise_angina = "false"
			break
		else:
			print("Wrong answer. Try again: ")
	
	os.system('cls')
	print("What is your oldpeak?")
	print("Numeric value measured in depression")
	while(True):
		oldpeak = input("Oldpeak: ")
		if (is_number(oldpeak)):
			break
		else:
			print("Wrong Answer. Try Again.")

	
	os.system('cls')
	print("What is your slope of the peak exercise ST segment?")
	print("Type: ")
	print("UP for Upsloping")
	print("FLAT for Flat")
	print("DOWN for Downsloping")
	while(True):	
		x1 = input("Slope: ")
		if (x1 == "UP" or x1 == "up" or x1 == "Up"):
			x1_Up = 1
			x1_Down = 0
			x1_Flat = 0
			break
		elif (x1 == "DOWN" or x1 == "down" or x1 == "Down"):
			x1_Up = 0
			x1_Down = 1
			x1_Flat = 0
			break
		elif (x1 == "Flat" or x1 == "FLAT" or x1 == "flat"):
			x1_Down = 0
			x1_Flat = 1
			x1_Up = 0
			break
		else:
			print("Wrong answer. Try Again")

	data = {
    		"Inputs": {
        	"WebServiceInput0":
        		[
            		{
                		'Id': "100",
                		'Age': age,
                		'Sex': sex,
                		'x0_ASY': x0_ASY,
                		'x0_ATA': x0_ATA,
                		'x0_NAP': x0_NAP,
                		'x0_TA': x0_TA,
                		'RestingBP': resting_bp,
                		'Cholesterol': cholesterol,
                		'FastingBS': fasting_bs,
                		'x2_LVH': x2_LVH,
                		'x2_Normal': x2_Normal,
                		'x2_ST': x2_ST,
                		'MaxHR': max_hr,
                		'ExerciseAngina': excersise_angina,
                		'Oldpeak': oldpeak,
                		'x1_Down': x1_Down,
                		'x1_Flat': x1_Flat,
                		'x1_Up': x1_Up,
                		'HeartDisease': "0",
            		},
        		],
    		},
    		"GlobalParameters": {
    		}
	}

	body = str.encode(json.dumps(data))
	headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ key)}
	req = urllib.request.Request(endpoint, body, headers)
	
	try:
		response = urllib.request.urlopen(req)
		result = response.read()
		json_result = json.loads(result)
		output = json_result["Results"]["WebServiceOutput0"][0]
		print("You have heart disease with probability: {:.2f}%".format(output["Heart disease"]*100))
		if ( 0.0 < float(output["Heart disease"] < 0.25)):
			print("Congratulations. You are very unlikely to have heart disease")
		elif (0.25 <= float(output["Heart disease"] < 0.5 )):
			print("There is small posibility for you to have heart disease, but watch yourself")
		elif (0.5 <= float(output["Heart disease"]) < 0.75):
			print("You should contact your doctor")
		elif (0.75 <= float(output["Heart disease"])):
			print("You have to contact your doctor. You are likely to have heart disease!")
	except urllib.error.HTTPError as error:	
		print("The request failed with status code: " + str(error.code))
    	# Print the headers to help debug
		print(error.info())
		print(json.loads(error.read().decode("utf8", 'ignore')))

def main():
	while(True):
		global selected
		show_menu()
			
		keyboard.add_hotkey('up', up)
		keyboard.add_hotkey('down', down)
		keyboard.wait('enter')
		if selected == 1:
			os.system('cls')
			predict()
			input("Press...")
		elif selected == 2:
			os.system('cls')
			print("Hello in heart disease predicting using Machine Learning!")
			print("You will be asked about few things,")
			print("based on which we will try to predict your heart condition.")
			input()
			input("Press...")
		elif selected == 3:
			print("Goodbye!")
			input("Press...")
			exit()

if __name__ == "__main__":
    main()