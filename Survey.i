%module Survey
%{
% #include "Survey.h"
%}

typedef enum { SURVEY_ALLOCATION_FAILED, SURVEY_SUCCESS} SurveyReturnValue;

typedef struct survey_t* Survey;

Survey SurveyCreateSurvey();

SurveyReturnValue SurveyAddPerson(Survey Survey, int Id, int Age, bool Gender, int EatingHabits , int* Scores);

int* SurveyQuerySurvey(Survey survey, int ChocolateType, bool Gender, int AgeMin, int AgeMax, int EatingHabits);

void SurveyQueryDestroy(int* histogram);

void SurveyDestroySurvey(Survey survey);
