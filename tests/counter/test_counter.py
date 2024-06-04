from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'

    word_python = "Python"
    word_js = "Javascript"

    count_python_lower = count_ocurrences(path, word_python.lower())
    count_python_upper = count_ocurrences(path, word_python.upper())

    assert count_python_lower == count_python_upper, (
        f"Contagens de '{word_python.lower()}' ({count_python_lower}) "
        f"e '{word_python.upper()}' ({count_python_upper}) devem ser iguais"
    )

    assert count_python_lower == 1639, (
        f"Esperado 1639 ocorrências de 'python', mas encontrado "
        f"{count_python_lower}"
    )

    count_js = count_ocurrences(path, word_js.lower())

    assert count_js == 122, (
        f"Esperado 122 ocorrências de 'javascript', mas encontrado {count_js}"
    )
