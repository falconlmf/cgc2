def get_folders(dir):
    black_list = ['.git', '__pycache__', 'env']
    filenames= os.listdir (dir)
    result = []
    for filename in filenames: # loop through all the files and folders
        if os.path.isdir(os.path.join(os.path.abspath("."), filename)): # check whether the current object is a folder or not
            if filename not in black_list:
                result.append(filename)
    return result