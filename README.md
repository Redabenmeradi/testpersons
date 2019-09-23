# Test person generator

# How to use
- Choose number of persons you want to generate
- Choose if you want to save the result to file
- Click "Run" to generate test data
You will be prompted to select a folder after
results are presented if "Save to file" was selected.

The file will be named "testdata.json", and if the file exists,
the result will be added in the end of that file.

Click "Show results" to show results up to, and
including the last run.

Clicking "Reset" will reset session results (saved files will not be removed),
and default "Save to file" to not save anything.


Each run will generate test persons with the following attributes:

- Name
- Last name
- 12 digit social security number
- 10 digit social security number
- Address in different formats
- Faked email address
- 8 characters long, randomly generated password
File format is .json with all entries as a dictionary and includes special characters for Swedish. Some characters like Åå, Ää, Öö, á, and é  will be changed to Aa, Oo and e in the email address.



# DISCLAIMERS!
**All test data is fetched from https://www.slumpa.net and is only intended for use in a test environment
The generated password is created with a static, non-secure method using digits and letters only, and is not recommended for personal use!
