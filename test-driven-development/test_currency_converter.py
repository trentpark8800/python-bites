import pytest

from currency_converter_with_tdd import convert_currency

def test_convert_currency_converts_between_two_currencies():
    mock_rates = {
        "USD": { "EUR": 0.92, "JPY": 130.0 },
        "EUR": { "USD": 1.09, "JPY": 141.0 },
        "JPY": { "USD": 0.0077, "EUR": 0.0071 }
    }
    assert convert_currency(100, "USD", "EUR", mock_rates) == 92.0

def test_convert_currency_raises_a_value_error_if_rate_not_found():
    mock_rates = {
        "USD": {"JPY": 130.0 },
        "JPY": { "USD": 0.0077}
    }
    with pytest.raises(ValueError):
        convert_currency(100, "USD", "EUR", mock_rates)

def test_convert_currency_returns_amount_if_source_and_target_currency_are_the_same():
    mock_rates = {
        "USD": {"EUR": 0.92, "JPY": 130.0 },
        "EUR": { "USD": 1.09, "JPY": 141.0 },
        "JPY": { "USD": 0.0077, "EUR": 0.0071 }
    }
    assert convert_currency(100, "USD", "USD", mock_rates) == 100.0