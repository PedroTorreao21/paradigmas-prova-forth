def test_sign(io):
    assert io("questao-08.fs", ["42 sign'", ".s"]).stack == [1]
    assert io("questao-08.fs", ["-42 sign'", ".s"]).stack == [-1]
    assert io("questao-08.fs", ["0 sign'", ".s"]).stack == [0]


def test_sum(io):
    assert io("questao-08.fs", ["10 1 2 3 3 sum", ".s"]).stack == [10, 6]
    assert io("questao-08.fs", ["42 -1 0 1 3 sum", ".s"]).stack == [42, 0]


def test_sum_on_empty_array(io):
    assert io("questao-08.fs", ["1 2 3 0 sum", ".s"]).stack == [1, 2, 3, 0]


def test_has_zero_result(io):
    assert io("questao-08.fs", ["0 1 2 3 has-zero", ".s"]).tos == [-1]
    assert io("questao-08.fs", ["1 2 3 has-zero", ".s"]).tos == [0]
    assert io("questao-08.fs", ["has-zero", ".s"]).tos == [0]


def test_has_zero_result(io):
    assert io("questao-08.fs", ["0 1 2 3 has-zero", ".s"]).stack == [0, 1, 2, 3, -1]
    assert io("questao-08.fs", ["1 2 3 has-zero", ".s"]).stack == [1, 2, 3, 0]
    assert io("questao-08.fs", ["has-zero", ".s"]).stack == [0]
