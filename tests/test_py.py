import pytest
from main import balance
from stack import Stack

fixture = [
    ('(((([{}]))))',True),
    ('[([])((([[[]]])))]{()}',True),
    ('{{[()]}}',True),
    ('{{[(])]}}',False),
    ('[[{())}]',False)

]

class Test_Main:
    @pytest.mark.parametrize("a,result",fixture)
    def test_balance(self, a, result):

        al = list(a)
        balanc_result  = balance(al) 
        assert balanc_result == result

