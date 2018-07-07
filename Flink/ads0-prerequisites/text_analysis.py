# ANALYSE TEXT #

# Sample from 20,000 leagues under the sea by Jules Verne
# Available in the public domain
# More substantial text available in the text_sample.txt file

# DO NOT MODIFY CONSTANTS
TEXT_SAMPLE = """
Striking an average of observations taken at different times-- rejecting those
timid estimates that gave the object a length of 200 feet, and ignoring those
exaggerated views that saw it as a mile wide and three long--you could still
assert that this phenomenal creature greatly exceeded the dimensions of
anything then known to ichthyologists, if it existed at all.
Now then, it did exist, this was an undeniable fact; and since the human mind
dotes on objects of wonder, you can understand the worldwide excitement caused
by this unearthly apparition. As for relegating it to the realm of fiction,
that charge had to be dropped.
In essence, on July 20, 1866, the steamer Governor Higginson, from the
Calcutta & Burnach Steam Navigation Co., encountered this moving mass five
miles off the eastern shores of Australia.
"""


def extract_numbers(text):
    '''
    This function finds all the numbers in the text and returns them in a list
    of floats.

    NOTE: in English, commas are used to separate thousands
    NOTE: several consecutive numbers are separated by a comma and a space

    E.g., extract_numbers("this is 1 awesome string") is [1.0]
    E.g., extract_numbers("12 days of XMas") is [12.0]
    E.g., extract_numbers("1, 2, 3, un pasito pa'lante Maria")
    is [1.0, 2.0, 3.0]

    @param text a string that forms English text
    @return the list of numbers (as floats) that are present in the text
    '''
    raise NotImplementedError


def latin_ish_words(text):
    '''
    English has words from Latin (or Spanish, Italian, French, etc.) and from
    German (or Dutch, etc.). They are often easy to tell apart. This function
    picks up some of the Latin sounding words based on some of their features.

    Latin features:
        - tion (as in navigation, isolation, or mitigation)
        - ex (as in explanation, exfiltrate, or expert)
        - ph (as in philosophy, philanthropy, or ephemera)
        - ost, ist, ast (as in hostel, distribute, past)

    NOTE: this matching method is not exact, many Germanic words include those
    features, and many Latin words lack them.
    NOTE: matching this way should ignore case.

    E.g., latin_ish_words("This works well") is []
    E.g., latin_ish_words("This functions as expected")
    is ["functions", "expected"]

    @param text a string that forms English text
    @return the set of words present in the text that have any of the Latin
    features listed above.
    '''
    raise NotImplementedError
