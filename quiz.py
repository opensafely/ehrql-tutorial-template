# Welcome to the ehrQL Quiz!

from quiz_answers import questions

from ehrql import codelist_from_csv, debug
from ehrql.tables.core import clinical_events


diabetes_codes = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-dm_cod.csv", column="code"
)
referral_codes = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-dsep_cod.csv", column="code"
)
mild_frailty_codes = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-mildfrail_cod.csv", column="code"
)
moderate_frailty_codes = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-modfrail_cod.csv", column="code"
)
severe_frailty_codes = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-sevfrail_cod.csv", column="code"
)
hba1c_codes = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-ifcchbam_cod.csv", column="code"
)

# Question 0
# Create an event frame by filtering clinical_events to find just the records indicating a diabetes
# diagnosis. (Use the diabetes_codes codelist.)
questions[0].check(
    clinical_events.where(clinical_events.snomedct_code.is_in(diabetes_codes))
)

# Question 1
# Create a patient series containing the date of each patient's earliest diabetes diagnosis.
questions[1].check(...)

# Question 2
# Create a patient series containing the date of each patient's earliest structured education
# programme referral. (Use the referral_code codelist.)
questions[2].check(...)

# Question 3
# Create a boolean patient series indicating whether the date of each patient's earliest diabetes
# diagnosis was between 1st April 2023 and 31st March 2024. If the patient does not have a
# diagnosis, the value for in this series should be False.
questions[3].check(...)

# Question 4
# Create a patient series indicating the number of months between a patient's earliest diagnosis
# and their earliest referral.
questions[4].check(...)

# Question 5
# Create a boolean patient series identifying patients who have been diagnosed with diabetes for
# the first time in the past year and who have a record of being referred to a structured education
# programme within nine months after their diagnosis.
questions[5].check(...)

# Question 6
# Create a patient series with the date of the latest record of mild frailty for each patient.
questions[6].check(...)

# Question 7
# Create a patient series with the date of the latest record of moderate or severe frailty for
# each patient.
questions[7].check(...)

# Question 8
# Create a boolean patient series indicating whether a patient's last record of severity is
# moderate or severe. If the patient does not have a record of frailty, the value in this series
# should be False.
questions[8].check(...)

# Question 9
# Create a patient series containing the latest HbA1c measurement for each patient.
questions[9].check(...)

# Question 10
# Create a boolean patient series identifying patients without moderate or severe frailty in whom
# the last IFCC-HbA1c is 58 mmol/mol or less in the preceding twelve months
questions[10].check(...)

questions.summarise()