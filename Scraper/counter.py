filePath = "Kickstarter_2023-10-12T03_20_02_365Z 2.json"

def countEntries(filePath: str) -> int:
    """
    Counts the number of entries in a file.

    Args:
        filePath (str): The file to count the entries of.

    Returns:
        int: The number of entries in the file.
    """
    data = open(filePath)
    listdata = data.readlines()
    
    count = 0
    