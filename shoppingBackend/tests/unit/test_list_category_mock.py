import pytest
from unittest.mock import patch, Mock
from businessRules.CategoryBR import CategoryBR

@patch('businessRules.CategoryBR.CategoryBR.getCategories')
async def test_getCategories(mock_getCategories):
    mock_getCategories.return_value = []
    br = CategoryBR()
    result = await br.getCategories()
    mock_getCategories.assert_called_once_with()
    assert result == []