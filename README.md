# dataWrangler

**Data Formatting Interview Coding Test:**

**Three files with different file formats are received and need to Format/Manipulate the data to get the Output file with the proper format.**

1. PYTEST\_CSV\_1.csv
2. PYTEST\_CSV\_2.csv
3. PYTEST\_EXCEL.xlsx

**Each File has Header and the records with the Same Structure as below:**

Field1 [ID]  Type is Character

Field2 [First Name]  Type is Character

Field3 [Last Name]  Type is Character

Field4 [Phone Number]  Type is Number [10 digits]

- Remove any special character [e.x. "-" or "(" or ")"].
- Ignore the record if \< 10 digits

Field5 [Date of Birth]  Type is Date [MM/DD/YYYY]

- Ignore the Record if format is not matching [MM/DD/YYYY]

Field6 [Balance ID]  Type is Character

Field7 [Balance Amount]  Type is Number [Debit +ve]

- Ignore the Record with Zero Balance Amount

Field8 [Paid Amount]  Type is Number [Credit +ve]

Remove the Duplication and ignore duplicated records in the Output.

Check Duplication Fields  ID, Balance ID, Balance Amount and Paid Amount.

Merge and Aggregate the data in the files using the ID Column to identify the matching records. Then generate a CSV Output file with the below structure.

Output File will include one record aggregated for the same ID.

Field1 [ID]  Type is Character

Field2 [First Name]  Type is Character

Field3 [Last Name]  Type is Character

Field4 [Phone Number]  Type is Number [10 digits]

Field5 [Date of Birth]  Type is Date [MM/DD/YYYY]

Field6 [Balance Amount]  Type is Number [Debit +ve]

Field7 [Paid Amount]  Type is Number [Credit +ve]

Field7 [Remaining Balance Amount]  Type is Number [Debit +ve]

- Calculation [Balance Amount] - [Paid Amount]
- Ignore the Record with Zero Remaining Balance. Amount

Notes:

1. The output record data [fields] can be having the Value of any of the input record in case of Aggregation.
2. Panda Data frame preferred but not necessary to be used in Loading the data from different source and write the Output file.
3. Some tricky issues in the input files you need to fix to be able to generate the expected output.
