from ansible import errors

#
# Additional Jinja2 filter to wrap list elements with quote
#


def wrap_list_elements(arg):
    """
        Wrap each list element with quote, to use before join filter

        :param arg: the brute list to manage
        :type arg: list
        :return: quoted elements
        :rtype: list
    """

    arg_type = type(arg)

    # Check if type is valid
    if arg_type != list:
        raise errors.AnsibleFilterError(
            'Invalid value type "%s", list expected' % arg_type)

    return ['"%s"' % element for element in arg]


class FilterModule(object):
    """ Filters to manage aptly configuration list values"""

    filter_map = {
        'wrap_list_elements': wrap_list_elements
    }

    def filters(self):
        return self.filter_map
