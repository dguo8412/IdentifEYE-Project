"""
Daniel Guo
CS+BioE at Stanford
danguo@stanford.edu

IdentifEYE Summer 2023 Internship Take-Home Project
"""
# Helper function to add a patient record
def add_patient(records: dict, entryList: list):
    ID = entryList[2]
    name = ' '.join(entryList[3:])

    # edge case: ignore if the patientID already exists
    if ID not in records.keys():
        newRecord = (name, set())  # used tuple, elem 0 for name and elem 1 for set of examIDs
        records[ID] = newRecord

# Helper function to add an exam record
def add_exam(records: dict, examIDtoID: dict, entryList: list):
    ID = entryList[2]
    examID = entryList[3]

    # edge cases: 
    # 1. ignore if the patientID does NOT exist 
    # 2. ignore if examID already exists
    if ID in records.keys() and examID not in examIDtoID.keys():
        records[ID][1].add(examID)

        #ADDED an examIDtoID dict to keep track for del_exam
        examIDtoID[examID] = ID
    
# Helper function to delete a patient record
def del_patient(records: dict, examIDtoID: dict, entryList: list):
    ID = entryList[2]

    # edge case: ignore if the patientID does NOT exist
    if ID in records.keys():
        # HIDDEN edge case (due to my implementation)
        # delete all the exams associated with deleted patient in examIDtoID dict
        examIDs_to_delete = records[ID][1]
        for examID in examIDs_to_delete:
            del examIDtoID[examID]
        del records[ID]
    
# Helper function to delete an exam record
def del_exam(records: dict, examIDtoID: dict, entryList: list):
    examID = entryList[2]

    # edge case: ignore if the examID does NOT exist
    if examID in examIDtoID.keys():
        ID = examIDtoID[examID]
        records[ID][1].remove(examID)

def main():

    # Read and parse txt input file
    fileName = "input.txt" # edit this to test on different txt files
    file = open(fileName)
    records = {}
    examIDtoID = {}

    parsedInput = []
    for line in file:
        parsedInput.append(line.strip())
    file.close()

    # Execute every entry (line)
    for entry in parsedInput:
        entryList = entry.split()
        command = entryList[0].lower()
        datatype = entryList[1].lower()

        # Control flow for 4 options. Calls helper functions
        if command == "add" and datatype == "patient":
            add_patient(records, entryList)
        elif command == "add" and datatype == "exam":
            add_exam(records, examIDtoID, entryList)
        elif command == "del" and datatype == "patient":
            del_patient(records, examIDtoID, entryList)
        elif command == "del" and datatype == "exam":
            del_exam(records, examIDtoID, entryList)

    # Print out in correct format
    for ID in records.keys():
        print("Name: " + records[ID][0] + ", Id: " + ID + ", Exam Count: " + str(len(records[ID][1])))
    
if __name__ == "__main__":
    main()