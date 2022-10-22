from src.counter import count_ocurrences


def test_counter():
    word_python = count_ocurrences('src/jobs.csv', 'Python')
    word_javascript = count_ocurrences('src/jobs.csv', 'Javascript')

    assert word_python == counter_fake_mock('src/jobs.csv', 'Python')
    assert word_javascript == counter_fake_mock('src/jobs.csv', 'Javascript')


def counter_fake_mock(path, word):
    with open(path, mode="r") as file:
        return file.read().lower().count(word.lower())
