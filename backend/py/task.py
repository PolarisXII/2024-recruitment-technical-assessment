from dataclasses import dataclass

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Helpers
"""

'''
    Group files together into a dict, 
    keys being the ids of the parent files and values being their corresponding children files
'''
def groupFilesByParents(files: list[File]) -> dict:
    parentsAndChildren = {}
    for file in files:
        parentsAndChildren.setdefault(file.parent, []).append(file)
    return parentsAndChildren

'''
    Group files into a dict, 
    keys being categories and values files under each corresponding category
'''
def groupFilesByCategory(files: list[File]):
    categories = {}
    for file in files:
        for category in file.categories:
            categories.setdefault(category, []).append(file.name)
    return categories

'''
    Given a file, find all its descendants (children files, grandchildren files etc)
    If the file has no descendants, return an empty list
'''
def findDescendants(file: File, files_by_parent: dict[int, list[File]]) -> list[File]:
    descendants = []
    children = files_by_parent.get(file.id, [])

    if len(children) > 0:
        for child in children:
            descendants.append(child)
            descendants.extend(findDescendants(child, files_by_parent))

    return descendants

'''
    Group files into a dict, 
    keys being filenames and values being their descendants 
'''
def groupByDescendants(files:list[File], filesByParents: dict):
    filesByParents = groupFilesByParents(files)
    filesByDescendants = {}

    for file in files:
        filesByDescendants[file.name] = findDescendants(file, filesByParents)
    
    return filesByDescendants
        
def findSizeByName(files: list[File], name:str):
    size = [file.size for file in files if file.name == name]
    return size[0]

"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    filesByParents = groupFilesByParents(files)
    leafFiles = [file.name for file in files if file.id not in filesByParents]
    return sorted(leafFiles)


"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    categories = groupFilesByCategory(files)
    sortedCategories = sorted(categories.items(), key=lambda x: (-len(x[1]), x[0]))

    if k >= len(sortedCategories):
        return [category[0] for category in sortedCategories]
    
    result = []
    for i in range(0, k):
        result.append(sortedCategories[i][0])
    return result


"""
Task 3
"""
def largestFileSize(files: list[File]) -> int:
    filesByParents = groupFilesByParents(files)
    filesByDescendents = groupByDescendants(files, filesByParents)

    sizes = []
    for filename, descendants in filesByDescendents.items():
        size = findSizeByName(files, filename)
        if len(descendants) == 0:
            sizes.append(size)
        else:
            total = size + sum(file.size for file in descendants)
            sizes.append(total)
    
    return max(sizes)


if __name__ == '__main__':
    testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
    ]

    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]

    assert kLargestCategories(testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992
