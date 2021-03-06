"""
Project 03
Team Members: Abhilash Ugaonkar, Anurag Patil, Ketaki Thatte, Vicky Rana
"""
import argparse
import os

from US01_dates_before_currentdate import *
from US02_birth_date_less_marriage_date import *
from US03_birth_before_death import *
from US04_Marriagebeforedivorce import *
from US05_marriageBeforeDeath import *
from US06_Divorcebeforedeath import *
from US07_lessThan150 import *
from US08_birth_before_marriage_of_parents import *
from US09_birth_before_death_of_parents import *
from US10_Marriage_after_14 import *
from US12_Parents_not_too_old import *
from US14_multipleBirthLessThan5 import US14_multipleBirthLessThan5
from US15_Siblingslessthan15 import *
from US16_MaleLastName import *
from US18_SiblingsnotMarry import *
from US22_UniqueID import *
from US23_unique_userName_BirthDate import *
from US25_UniqueFirstName import *
from US27_individual_age import *
from US28_listDescendingAge import *
from US29_listDeceased import US29_listDeceased
from US30_living_marriages import *
from US31_above30_single import *
from US32_multiple_births import *
from US33_listOrphans import US33_listOrphans
from US35_List_recent_births import *
from US36_List_Recent_Deaths import *
from US38_listUpcomingBirthdays import US38_listUpcomingBirthdays
from US39_upcoming_anniversary import upcoming_anniversary
from US41_Accept_Partial_Dates import US41_accpet_partial_dates
from US42_Reject_illegitimate_dates import US42_rejectIllegitimateDates
from print_data import *
from src.gedParser import GEDCOMParser

FILENAME = 'gedcom_files/myTree.ged'

connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']
people = db.people
family = db.family
db.people.remove({})
db.family.remove({})


def printPretty(individual, families):
    for i in individual:
        people.insert_one(i)

    for j in families:
        family.insert_one(j)
    # Print Individual Data
    print(print_individuals())
    print(print_families())

    # USer 01
    dates_before_current_date()
    #Print user story 02
    birth_date_less_marriage_date()
    # User Story 03
    birth_before_death()
    # Call user story 04
    check_marriagebeforedivorce()
    # Call User story 05
    US05_marriageBeforeDeath()
    # Call user story 06
    divorcebeforedeath()
    #Call User story 07
    US07_lessThan150()
    # call User story 08
    US08_birth_before_marriage_of_parents()
    # Call User Story 09
    US09_birth_before_death_of_parents()
    #US10  User story 10
    Marriage_after_14()
    # Call User Story 12
    US12_Parents_not_too_old()
    #Call User story 14
    US14_multipleBirthLessThan5()
    #Call User Story 15
    fewer_than15_siblings()
    #Call User Story 16
    male_last_names()
    #Call User Story 18
    siblingsnotmarry()
    # Call User Story 21
    #husbandwifegender()
    # Call user story 22
    unique_indids()
    unique_famids()
    # User Story 23
    unique_name_bdate()
    #Call User Story 25
    unique_first_famnames()
    # Call User story 27
    individual_age()
    # Call User story 28
    US28_listDescendingAge()
    # Call User story 29
    US29_listDeceased()
    # Call User Story 30
    living_marriages()
    # Call user story 31
    more_than_30_unmarried()
    #call user story 32
    US32_multiple_births()
    # Call User story 33
    US33_listOrphans()
    # Call User story 35
    US35_list_recent_births()
    #User 36
    recent_deaths()
    # Call User story 38
    US38_listUpcomingBirthdays()
    # Call User story 39
    upcoming_anniversary()
    # Call User story 41
    US41_accpet_partial_dates()
    # Call User story 42
    US42_rejectIllegitimateDates()

    

def main():
    deleteContent()
    parser = argparse.ArgumentParser() # Allow for args to be passed for filename
    action = parser.add_mutually_exclusive_group()
    action.add_argument("-f", "--file", nargs="?", const=FILENAME,
                        default=FILENAME,
                        help="Specify file name" + FILENAME)

    args = parser.parse_args()
    path = args.file
    if os.path.exists(path):
        #print("PATH VERIFIED...")
        individual, families = GEDCOMParser(path)
    else:
        print("[!!] FILE \"%s\" DOESN'T EXISIT.\n Terminiating..." % path)
        exit(-1)
    #printing values
    printPretty(individual, families)

if __name__ == '__main__':
    main()
