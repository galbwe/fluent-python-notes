from ch7.decorators import count_calls, count_calls_by_signature

class TestCountCalls:
    def test_single_calls(self):
        counts = {}
        @count_calls(counts)
        def square(a):
            return a * a
        @count_calls(counts)
        def cube(a):
            return a * a * a

        assert counts['square'] == 0
        assert square(1) == 1
        assert counts['square'] == 1
        assert square(2) == 4
        assert counts['square'] == 2
        assert square(3) == 9
        assert counts['square'] == 3
        assert counts['cube'] == 0
        cube(1)
        cube(2)
        cube(3)
        assert counts['cube'] == 3

    def test_recursive_calls(self):
        counts = {}
        @count_calls(counts)
        def fib(n):
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            return fib(n - 2) + fib(n - 1)
        assert fib(5) == 5
        assert counts['fib'] == 15


class TestCountCallsBySignature:
    def test_positional_arguments(self):
        counts = {}
        @count_calls_by_signature(counts)
        def fib(n):
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            return fib(n - 2) + fib(n - 1)
        fib(5)
        assert counts['fib']['(5)'] == 1
        assert counts['fib']['(4)'] == 1
        assert counts['fib']['(3)'] == 2
        assert counts['fib']['(2)'] == 3
        assert counts['fib']['(1)'] == 5
        assert counts['fib']['(0)'] == 3

    def test_keyword_arguments(self):
        counts = {}
        @count_calls_by_signature(counts)
        def count_occurences_of_letter(letter, sentence=''):
            return sentence.count(letter)
        func_name = 'count_occurences_of_letter'
        sentence = 'The quick brown fox jumped over the sleeping dog'
        count_occurences_of_letter('a', sentence=sentence)
        count_occurences_of_letter('a', sentence=sentence)
        count_occurences_of_letter('a', sentence=sentence)
        count_occurences_of_letter('b', sentence=sentence)
        count_occurences_of_letter('b', sentence=sentence)
        assert counts[func_name][f'(a, sentence={sentence})'] == 3
        assert counts[func_name][f'(b, sentence={sentence})'] == 2
