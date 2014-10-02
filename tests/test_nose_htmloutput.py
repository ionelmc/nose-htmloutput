from __future__ import print_function

from process_tests import dump_on_error
from process_tests import TestProcess
from process_tests import wait_for_strings

TIMEOUT = 10

def test_sample():
    with TestProcess(
        'coverage', 'run', 'tests/nosetests.py', '--verbose', '--with-html', '--html-file=sample.html',
        'tests/test_sample.py'
    ) as proc:
        with dump_on_error(proc.read):
            wait_for_strings(proc.read, TIMEOUT, 'Ran 9 tests in')
    output = open('sample.html').read()

    assert """<tr>
                    <td>test_sample</td>
                    <td>1</td>
                    <td>1</td>
                    <td>1</td>
                    <td>4</td>
                </tr>""" in output
    assert """<tr>
                    <td>test_sample.MainTestCase</td>
                    <td>1</td>
                    <td>0</td>
                    <td>1</td>
                    <td>2</td>
                </tr>""" in output
    assert """<tr>
                    <td>test_sample.FailedSetupTestCase</td>
                    <td>0</td>
                    <td>0</td>
                    <td>0</td>
                    <td>1</td>
                </tr>""" in output
    assert """<tr>
                    <td>test_sample.SecondTestCase</td>
                    <td>0</td>
                    <td>0</td>
                    <td>2</td>
                    <td>2</td>
                </tr>""" in output
    assert """<tr>
                <td><strong>Total</strong></td>
                <td>2</td>
                <td>1</td>
                <td>4</td>
                <td>9</td>
            </tr>""" in output


    assert "<h2>test_sample.MainTestCase (1 failures, 0 errors)</h2>" in output
    assert '<section id="test_sample.MainTestCase:test_b">' in output
    assert '<h3>test_b: <strong>' in output
    assert '<section id="test_sample:test_b">' in output
    assert '<h3>test_b: <strong>' in output
    assert '<li><a class="success">test_a</a></li>' in output
    assert '<li><a class="failed" href="#test_sample.MainTestCase:test_b">test_b</a></li>' in output
    assert '<h2>test_sample (1 failures, 1 errors)</h2>' in output
    assert '<li><a class="success">test_a</a></li>' in output
    assert '<li><a class="failed" href="#test_sample:test_b">test_b</a></li>' in output
    assert "<h2>test_sample.FailedSetupTestCase (0 failures, 1 errors)</h2>" in output
