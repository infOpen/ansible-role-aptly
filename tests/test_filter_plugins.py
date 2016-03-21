import pytest
from ansible import errors
from filter_plugins.wrap_list_elements import wrap_list_elements


# =============================================================================
# Tests
# =============================================================================

#
# Tests about wrap_list_elements
#
@pytest.mark.parametrize('arg', [
    (['True']),
    ([True])
])
def test_true_wrap_list_elements(arg):
    assert wrap_list_elements(arg) == ['"True"']


@pytest.mark.parametrize('arg', [
    ([])
])
def test_empty_wrap_list_elements(arg):
    assert wrap_list_elements(arg) == []


@pytest.mark.parametrize('arg', [
    (),
    (()),
    ('foo'),
    (42)
])
def test_bad_type_wrap_list_elements(arg):
    with pytest.raises(errors.AnsibleFilterError) as errorInfo:
        wrap_list_elements(arg)

    assert 'Invalid value type' in str(errorInfo.value)
