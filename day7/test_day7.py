from day7 import Hand
import pytest


@pytest.mark.parametrize(
    "hand, score, joker_score",
    [ 
     ("JKKKK", 5, 6),
     ("JKKKA", 3, 5),
     ("JKKAA", 2, 4),
     ("JKKAB", 1,3),
     ("JKA23", 0, 1),
     ("JJKKK", 4, 6),
     ("JJJJJ", 6,6),
     ("JJJJA", 5,6),
     ("JJJAK", 3, 5),
     ("JJJAA", 4, 6),
     ("JJKQA", 1, 3),
     ("JJKKK", 4, 6),
     ("JJKKA",2, 5),
     ("KKKAA", 4, 4),
     ("KA234",0,0))
    ]
)
def test_scores(hand, score, joker_score):
    h = Hand(hand, 1)
    h.score
    assert h.score==score
    h.set_joker_score()
    assert h.score == joker_score
