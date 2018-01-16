import re

# dd/mm/yyyy or dd-mm-yyyy format:

def date_ddmmyyyy (str):

    date = r"(\D((0?[1-9])|(1|2[0-9])|(3[0-1])).((0?[1-9])|(1[1-2])).(([0-1][0-9][0-9][0-9])|(20[0-9][0-9])))"

    match = re.search(date, str)

    if match:
        extracted_date = match.group()

        # checking if date is correct with respect to / and -

        # if format is dd/mm/yyyy 
        terms = list(extracted_date.split("/"))

        if len(terms) == 3:
            print extracted_date
    
        #if format is dd-mm-yyyy
        elif len(terms) == 1:
            terms = list(extracted_date.split("-"))
            if len(terms) == 3:
                print extracted_date
            
            #if format is dd.mm.yyyy
            elif len(terms) == 1:
                terms = list(extracted_date.split("."))
                if len(terms) == 3:
                    print extracted_date
    
    #checking for next format of date
    else:
        date_mmddyyyy (str)

 


# mm/dd/yyyy format or mm-dd-yyyy format:

def date_mmddyyyy(str):

    date = r"((0?[1-9])|(1[0-2])).(((0?[1-9])|([1-2][0-9])|(3[0-1])).(([0-1][0-9][0-9][0-9])|(20[0-9][0-9])))"

    match = re.search(date, str)

    if match:
        extracted_date = match.group()

        # checking if date is correct with respect to / and -

        # if format is mm/dd/yyyy 
        terms = list(extracted_date.split("/"))

        if len(terms) == 3:
            print extracted_date
    
        #if format is mm-dd-yyyy
        elif len(terms) == 1:
            terms = list(extracted_date.split("-"))
            if len(terms) == 3:
                print extracted_date

            #if format is mm.dd.yyyy
            elif len(terms) == 1:
                terms = list(extracted_date.split("."))
                if len(terms) == 3:
                    print extracted_date
    
    #checking for next format of date
    else:
        month_date_year (str)




# month date, year format:

def month_date_year (str):

    date =  r"((January|February|March|April|May|June|July|August|September|October|November|December) ((2?(3?1st|2nd|3rd))|([4-9]|(1[0-9])|2[4-9]|(2|30))th), (([0-1][0-9][0-9][0-9])|(20[0-9][0-9])))"
    
    #case-insensitve for name of months

    match = re.search(date, str, re.IGNORECASE)

    if match:
        extracted_date = match.group()
        print extracted_date,

    #checking for next format of date
    else:
        date_month_year (str)




# date month year format (Example: 9 november 2014):

def date_month_year (str):

    date =  r"(((0?[1-9])|([1-2][0-9])|(3[0-1])) (January|February|March|April|May|June|July|August|September|October|November|December)(,?)\s(([0-1][0-9][0-9][0-9])|(20[0-9][0-9])))"
    
    #case-insensitve for name of months

    match = re.search(date, str, re.IGNORECASE)

    if match:
        extracted_date = match.group()
        print extracted_date,

    #checking for next format of date
    else:
        date_mon_year (str)
    


# date-month-year format (Example : 29/nov/2014):

def date_mon_year (str):

    date = r"(((0?[1-9])|([1-2][0-9])|(3[0-1])).(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).(([0-1][0-9][0-9][0-9])|(20[0-9][0-9])))"

    #case-insensitive for name of months

    match = re.search(date, str, re.IGNORECASE)

    if match:
        extracted_date = match.group()

        # checking if date is correct with respect to / and -

        # if format is dd/mm/yyyy 
        terms = list(extracted_date.split("/"))

        if len(terms) == 3:
            print extracted_date
    
        #if format is dd-mm-yyyy
        elif len(terms) == 1:
            terms = list(extracted_date.split("-"))
            if len(terms) == 3:
                print extracted_date
        




# 12-hour time format:

def time_12hour (str):

    time = r"(((0?[0-9])|(1[0-2])):[0-5][0-9])(a|p)m"

    #case-insensitive for name of am/pm or AM/PM or Am/Pm

    match = re.search(time, str, re.IGNORECASE)

    if match:
        extracted_time = match.group()
        print extracted_time,
    
    #checking for next format of time
    else:
        time_24hour (str)




# 24-hour time format:

def time_24hour (str):

    time = r"(((0?[0-9])|(2[0-3])):[0-5][0-9])"

    match = re.search(time, str, re.IGNORECASE)

    if match:
        extracted_time = match.group()
        print extracted_time,



if __name__ == '__main__':

    text = raw_input()

    # extracting date
    date = date_ddmmyyyy (text)

    # extracting time
    time = time_12hour (text)
 
