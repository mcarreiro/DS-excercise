integer_cleaners = [
    (lambda x: x is not None),
    (lambda x: x is not '.'),
    (lambda x: x >= 0),
]

natural_cleaners = integer_cleaners + [(lambda x: x > 0)]