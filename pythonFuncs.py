from copy import copy

def is_valid(id, feeding_habits, age, gender, ratings):

	#check id
	try:
		int(id)
		if len(id) != 8: return False

	except ValueError as e:
		return False

	#check feeding habits(assuming no restrictions)
	#valid_feeding_habits = ["Vegetarian", "Vegan", "Omnivore"]
	#if feeding_habits not in valid_feeding_habits: return False

	#check age
	try:
		age = int(age)
		if not (age >= 10 and age <= 100): return False

	except ValueError as e:
		return False

	#check gender : [assuming no restrictions on gender (newAge bullshit)]
	#if gender not in ["Woman", "Man"]: return False

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
			dict[int(id)] == copy(line)

	for key, value in dict:
		print(value)

#Returns a new Survey item with the data of a new survey file:
#survey_path: The path to the survey
def scan_survey(survey_path):
	pass
    #TODO

#Prints a python list containing the number of votes for each rating of a group according to the arguments
#s: the data of the Survey object
#choc_type: the number of the chocolate (between 0 and 4)
#gender: the gender of the group (string of "Man" or "Woman"
#min_age: the minimum age of the group (a number)
#max_age: the maximum age of the group (a number)
#eating_habits: the eating habits of the group (string of "Omnivore", "Vegan" or "Vegetarian")
def print_info(s, choc_type, gender, min_age, max_age, eating_habits):
	pass
    #TODO

#Clears a Survey object data
#s: the data of the Survey object
def clear_survey(s):
	pass
    #TODO
