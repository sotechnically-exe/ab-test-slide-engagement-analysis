def clean_data(data):
    """
    TODO: Implement your "clean_heartrate_data" function from TLAB #1 & #2
    within this module. Note that this code will be *slightly* different
    from your original function.

    We need to skip the first row [0]
    """
    clean_data = []
    for row in data:
        if row != "minutes\n":
            clean_data.append(float(row.strip()))
        
    return clean_data

    #list slicing?
    