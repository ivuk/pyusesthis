"""
A simple Python 3 wrapper around The Setup's API (https://usesthis.com/api/)
"""
import urllib.request


BASE_URL = "https://usesthis.com/api"
API_VERSION = "v1"
USESTHIS_API_URL = "{}/{}".format(BASE_URL, API_VERSION)


def _get_content(content_name, content_category, year="1978"):
    """
    Craft the appropriate URL for each API call
    Retrieve the content from the URL, decode it as UTF-8
    Return the retrieved content
    """
    #  Special handling for stats category that allows
    #  specifying year as a parameter
    if content_category == 'stats' and year != '1978':
        if content_name == 'all':
            content_url = "{}/{}/{}/".format(
                USESTHIS_API_URL, content_category, year)
        else:
            content_url = "{}/{}/{}/{}/".format(
                USESTHIS_API_URL, content_category, content_name, year)
    else:
        if content_name == 'all':
            content_url = "{}/{}/".format(USESTHIS_API_URL, content_category)
        else:
            content_url = "{}/{}/{}/".format(
                USESTHIS_API_URL, content_category, content_name)

    with urllib.request.urlopen(content_url) as url:
        content = url.read().decode('utf-8')

    return content


def get_hardware(hardware_name):
    """
    Process the input so each word is separated by a dot and lowercased
    Call the _get_content() function with the proper content_category parameter
    Return the output of the _get_content() function
    """
    fixed_name = "-".join(hardware_name.lower().split())
    output = _get_content(fixed_name, "hardware")

    return output


def get_software(software_name):
    """
    Process the input so each word is separated by a dash and lowercased
    Call the _get_content() function with the proper content_category parameter
    Return the output of the _get_content() function
    """
    fixed_name = "-".join(software_name.lower().split())
    output = _get_content(fixed_name, "software")

    return output


def get_interviews(interviewee_name):
    """
    Process the input so each word is separated by a dot and lowercased
    Call the _get_content() function with the proper content_category parameter
    Return the output of the _get_content() function
    """
    fixed_name = ".".join(interviewee_name.lower().split())
    output = _get_content(fixed_name, "interviews")

    return output


def get_stats(stat_name, stat_year="1978"):
    """
    Process the input so each word is lowercased
    Call the _get_content() function with the proper content_category parameter
    If the stat_year argument is passed, pass it to the _get_content() function
    Return the output of the _get_content() function
    """
    fixed_name = stat_name.lower()

    if stat_year != '1978':
        output = _get_content(fixed_name, "stats", stat_year)
    else:
        output = _get_content(fixed_name, "stats")

    return output


def get_categories(category_name):
    """
    Process the input so each word is lowercased
    Call the _get_content() function with the proper content_category parameter
    Return the output of the _get_content() function
    """
    fixed_name = category_name.lower()
    output = _get_content(fixed_name, "categories")

    return output
