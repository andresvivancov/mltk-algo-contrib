import pandas as pd
from algos_contrib.OrthogonalMatchingPursuit import OrthogonalMatchingPursuit
from test.contrib_util import AlgoTestUtils




def test_algo():
    input_df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4, 5, 6],
        'c': ['a', 'b', 'c'],
    })
    options = {
        'target_variable': ['a'],
        'feature_variables': ['b', 'c'],
    }
    required_methods = (
        '__init__',
        'fit',
        'partial_fit',
        'apply',
        'summary',
        'register_codecs',
    )
    AlgoTestUtils.assert_algo_basic(OrthogonalMatchingPursuit, required_methods ,  input_df, options)