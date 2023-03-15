"""
Daniel Guo
CS+BioE at Stanford
danguo@stanford.edu

IdentifEYE Summer 2023 Internship Take-Home Project
"""

def add_patient(records: dict, entryList: list):
    ID = entryList[2]
    name = ' '.join(entryList[3:])
    if ID not in records.keys():
        newRecord = (name, set())
        records[ID] = newRecord

def add_exam(records: dict, examIDtoID: dict, entryList: list):
    ID = entryList[2]
    examID = entryList[3]
    if ID in records.keys():
        records[ID][1].add(examID)
        examIDtoID[examID] = ID
    
def del_patient(records: dict, entryList: list):
    ID = entryList[2]
    if ID in records.keys():
        del records[ID]

def del_exam(records: dict, examIDtoID: dict, entryList: list):
    examID = entryList[2]
    if examID in examIDtoID.keys():
        ID = examIDtoID[examID]
        records[ID][1].remove(examID)

def main():
    fileName = "test1.txt"
    file = open(fileName)
    records = {}
    examIDtoID = {}

    parsedInput = []
    for line in file:
        parsedInput.append(line.strip())

    for entry in parsedInput:
        entryList = entry.split()
        command = entryList[0].lower()
        datatype = entryList[1].lower()

        if command == "add" and datatype == "patient":
            add_patient(records, entryList)
        elif command == "add" and datatype == "exam":
            add_exam(records, examIDtoID, entryList)
        elif command == "del" and datatype == "patient":
            del_patient(records, entryList)
        elif command == "del" and datatype == "exam":
            del_exam(records, examIDtoID, entryList)

    for ID in records.keys():
        print("Name: " + records[ID][0] + ", Id: " + ID + ", Exam Count: " + str(len(records[ID][1])))
    
if __name__ == "__main__":
    main()