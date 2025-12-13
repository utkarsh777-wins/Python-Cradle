# Open, read & close file
"""
-We have to open before reading and writing
-- f = open("file_name, "mode")
-r: read mode --open for reading(default)
-w: write mode --open for writing, truncating the file first
-x: create a new file and open it for writing
-a: open for writing, appending to the end of the file if it exists
-b: binary mode
-t: text mode(default)
-+: open a disk file for reading and writing

-r+: read + overwrite(pointer at the very beginning) --no truncate
-w+: read + overwrite --truncate
-a+: read + append(pointer at the end) --no truncate
-- without a specific mode=>by default the fie will be at read mode
-- truncating refers to overwriting a file --deleting the existing data and write

"""
