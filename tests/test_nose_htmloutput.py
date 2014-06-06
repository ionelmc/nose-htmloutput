from __future__ import print_function

import subprocess


def test_sample():
    subprocess.call(['nosetests', '--with-html', '--html-file=sample.html', 'tests/test_sample.py'])
    output = open('sample.html').read()

    assert """<body>
    <h1>Overview</h1>
    <section>
        <table>
            <tr>
                <th>Class</th>
                <th>Fail</th>
                <th>Skip</th>
                <th>Success</th>
                <th>Total</th>
            </tr>
                <tr>
                    <td>test_sample.MainTestCase</td>
                    <td>1</td>
                    <td>0</td>
                    <td>1</td>
                    <td>2</td>
                </tr>
                <tr>
                    <td>test_sample</td>
                    <td>1</td>
                    <td>0</td>
                    <td>1</td>
                    <td>2</td>
                </tr>
            <tr>
                <td><strong>Total</strong></td>
                <td>2</td>
                <td>0</td>
                <td>2</td>
                <td>4</td>
            </tr>
        </table>
    </section>""" in output
    assert "<h2>test_sample.MainTestCase (1 failures)</h2>" in output
    assert '<section id="test_sample.MainTestCase:test_b">' in output
    assert '<h3>test_b: <strong>exceptions.AssertionError</strong></h3>' in output
    assert '<h2>test_sample (1 failures)</h2>' in output
    assert '<section id="test_sample:test_b">' in output
    assert '<h3>test_b: <strong>exceptions.AssertionError</strong></h3>' in output
    assert '<h2>test_sample.MainTestCase (1 failures)</h2>' in output
    assert '<li><a class="success">test_a</a></li>' in output
    assert '<li><a class="failed" href="#test_sample.MainTestCase:test_b">test_b</a></li>' in output
    assert '<h2>test_sample (1 failures)</h2>' in output
    assert '<li><a class="success">test_a</a></li>' in output
    assert '<li><a class="failed" href="#test_sample:test_b">test_b</a></li>' in output

