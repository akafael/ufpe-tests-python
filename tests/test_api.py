import pytest
from src.api import convert

class TestAPI():
    def test_same_currency(self):
        value = 10.0
        currency = "BRL"

        assert( value == convert(value,currency,currency) )

    def test_other_currency(self):
        value = 10.0
        input_currency = "BRL"
        output_currency = "USA"
        expectedRate = 1.0
        converted_value = value*expectedRate

        assert( converted_value == convert(value,input_currency,output_currency) )
