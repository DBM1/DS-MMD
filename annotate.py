import re


def contain_substr(text, substr):
    if text is None:
        return False
    return substr in text


def extract_number(text):
    return extract_re(text, r' (\d+\.?\d*|\d*\.?\d+)[^st|^nd|^rd|^th] ')


def extract_index(text):
    return extract_re(text, r'1st|2nd|3rd|\d+th')


def extract_words(text):
    if text is not None:
        text = text.lower()
    return extract_re(text, r'[a-zA-Z-]+')


def extract_re(text, pattern):
    if text is None:
        return []
    pattern = re.compile(pattern)
    result = pattern.findall(text)
    return result


if __name__ == '__main__':
    print(extract_number(
        'does celebrity cel_1129 usually wear the kind of travel bag in the 2nd image'))
