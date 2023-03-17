#
#


def filter_cond(line_dict):
    """Filter function
    Takes a dict with field names as argument
    Returns True if conditions are satisfied
    """
    cond_match = (
      (int(line_dict["if1"].isdigit()) > 20) and (int(line_dict["if1"].isdigit()) < 40)
    ) 
    return True if cond_match else False

