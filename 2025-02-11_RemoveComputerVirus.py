# Goal: Remove files named virus or malware (aside from antivirus) from string.

v_Files = "PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, "
v_Files += "dangerousvirus.exe"

# Words we are looking for

l_VirusKey = ['virus','malware']

print ( "Base String:")
print ( v_Files )

# Convert to list. 
# Split off PC Files from the file list, then split the file list.
# Create empty list for cleaned files later.

l_Files = v_Files.split ( ": " , 1 )[1].split ( ", " )
l_CleanedFiles = []

print ("\nFile List:")
print ( l_Files )

# Virus detection function.

def isVirus ( x ) :

    if "ANTIVIRUS" in x.upper() :
        return False
    for key in l_VirusKey:
        if key.upper() in x.upper() :
            return True
    else :
        return False

# Check for antivirus in each item in the list.

for file in l_Files :
    if not isVirus ( file ) :
        l_CleanedFiles.append(file)

print ( "\nCleaned File List:")
print ( l_CleanedFiles )

# Create and print a new string.

v_NewString = ", ".join ( l_CleanedFiles )

if len ( v_NewString ) == 0 :
    v_NewString = "Empty"

print ( f"\nPC Files: {v_NewString}" )