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
def groupFilesByParents(files: list[File]) -> dict:
    parentsAndChildren = {}
    for file in files:
        parentsAndChildren.setdefault(file.parent, []).append(file)
    return parentsAndChildren


def groupFilesByCategory(files: list[File]):
    categories = {}
    for file in files:
        for category in file.categories:
            categories.setdefault(category, []).append(file.name)
    return categories


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
    return 0


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

#     assert largestFileSize(testFiles) == 20992
