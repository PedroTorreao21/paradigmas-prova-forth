PREFIX = (
    "create m1 1 , 2 , 3 , 4 ,\n"
    + "create m2 5 , 6 , 7 , 8 ,\n"
)

def test_get(io):
    assert io("questao-09.fs", [PREFIX, "m1 0 0 get", ".s"]).stack == [1]
    assert io("questao-09.fs", [PREFIX, "m1 0 1 get", ".s"]).stack == [2]
    assert io("questao-09.fs", [PREFIX, "m1 1 0 get", ".s"]).stack == [3]
    assert io("questao-09.fs", [PREFIX, "m1 1 1 get", ".s"]).stack == [4]


def test_m_at(io):
    m1 = io("questao-09.fs", [PREFIX + "m1 M@"])
    assert m1.output == "1 2 \n3 4"
    
    m2 = io("questao-09.fs", [PREFIX + "m2 M@"])
    assert m2.output == "5 6 \n7 8"
