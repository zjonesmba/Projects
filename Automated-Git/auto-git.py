from git import Repo

#Establishing Inputs
comment = input('What comment would you like to commit?:')
rem_repo = input('What remote repository would you like to push to (URL or nickname)?:')

# Giving a shortcut option for the comment
if comment == "n":
    comment = "Updated Files"

# Giving a shortcult option for folder location for repeat git saves
if rem_repo == 'private':
    folder_location = "C:\\Users\\Documents\\" # Editted for security
elif rem_repo == 'public':
    folder_location = "C:\\Users\\Documents\\TEST" #Editted for security
else:
    folder_location = input("Drag the folder's location here that you would like to push:")

# Assigning the variable to a list
ls = []
ls.append(rem_repo)

# Step 1
print("Changing and Initializing the Directory. . . ")
r = Repo.init(folder_location)

# Step 2
print("Staging Files. . .")
r.git.add(A=True)

# Step 3
print("Committing Updates. . .")
r.index.commit(comment)

# Step 4
print("Pushing changes to the remote repository")
r.git.push("-u", ls[0], "HEAD:main")

print("You git push has completed successfully!")
