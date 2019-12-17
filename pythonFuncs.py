from copy import copy
import Survey

valid_feeding_habits = ["Vegan", "Vegetarian", "Omnivore"]
genders = ["Woman", "Man"]

def is_valid(id, feeding_habits, age, gender, ratings):

	#check id
	try:
		int(id)
		if len(id) != 8: return False

	except ValueError as e:
		return False

	#check feeding habits(assuming no restrictions)
	if feeding_habits not in valid_feeding_habits: return False

	#check age
	try:
		age = int(age)
		if not (age >= 10 and age <= 100): return False

	except ValueError as e:
		return False

	#check gender :
	if gender not in genders: return False

	#check ratings
	try:
		for rating in ratings:
			ratin = int(rating)
			if(not ( ratin <= 10 and ratin >= 1)): return False
	except ValueError as e:
		return False

	#everything should be okay now:
	return True

#Filters a survey and prints to screen the corrected answers:
#old_survey_path: The path to the unfiltered survey
def correct_myfile(old_survey_path):

	f = open(old_survey_path, 'r')
	if f is None: return

	survey = f.readlines()
	f.close()

	dict = {}
	for line in survey:
		organized = line.split()
		if len(organized) != 9: continue

		id = organized[0]
		feeding_habits = organized[1]
		age = organized[2]
		gender = organized[3]
		ratings = organized[4:]

		if(not is_valid(id, feeding_habits, age, gender, ratings)): continue
		else:
			dict[int(id)] = copy(line.replace("\n", "").replace("\r", ""))

	for key in sorted(dict.keys()):
		print(dict[key])

#Returns a new Survey item with the data of a new survey file:
#survey_path: The path to the survey
def scan_survey(survey_path):
	survey = Survey.SurveyCreateSurvey()
	file = open(survey_path, 'r')
	lines = file.readlines()
	file.close()

	for line in lines:
		organized = line.split()
		if len(organized) != 9: continue

		id = organized[0]
		feeding_habits = organized[1]
		age = organized[2]
		gender = organized[3]
		ratings = organized[4:]

		if(not is_valid(id, feeding_habits, age, gender, ratings)): continue
		Survey.SurveyAddPerson(survey, int(id), int(age), gender == "Woman", valid_feeding_habits.index(feeding_habits), [int(rating) for rating in ratings])

	return survey


#Prints a python list containing the number of votes for each rating of a group according to the arguments
#s: the data of the Survey object
#choc_type: the number of the chocolate (between 0 and 4)
#gender: the gender of the group (string of "Man" or "Woman"
#min_age: the minimum age of the group (a number)
#max_age: the maximum age of the group (a number)
#eating_habits: the eating habits of the group (string of "Omnivore", "Vegan" or "Vegetarian")
def print_info(s, choc_type, gender, min_age, max_age, eating_habits):
	query = Survey.SurveyQuerySurvey(s, choc_type, gender == "Woman", min_age, max_age, valid_feeding_habits.index(eating_habits))
	print(query)
	Survey.SurveyQueryDestroy(query)
	#TODO

#Clears a Survey object data
#s: the data of the Survey object
def clear_survey(s):
	Survey.SurveyDestroySurvey(s)
    #TODO
