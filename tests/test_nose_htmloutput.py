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
    </section>
    <h1>Failure details</h1>
    <section>
        <h2>test_sample.MainTestCase (1 failures)</h2>
        <div>
                <section id="test_sample.MainTestCase:test_b">
                    <h3>test_b: <strong>exceptions.AssertionError</strong></h3>
                    <div class="test-details">
                        <h4>Traceback</h4>
                        <pre class="traceback">Traceback (most recent call last):
  File "/usr/lib/python2.7/unittest/case.py", line 327, in run
    testMethod()
  File "/home/ionel/osp/nose-htmloutput/tests/test_sample.py", line 9, in test_b
    self.assertTrue(0, "Some details")
  File "/usr/lib/python2.7/unittest/case.py", line 420, in assertTrue
    raise self.failureException(msg)
AssertionError: Some details
</pre>
                        <h4>Details</h4>
                        <pre>Some details</pre>
                    </div>
                </section>
        </div>
    </section>
    <section>
        <h2>test_sample (1 failures)</h2>
        <div>
                <section id="test_sample:test_b">
                    <h3>test_b: <strong>exceptions.AssertionError</strong></h3>
                    <div class="test-details">
                        <h4>Traceback</h4>
                        <pre class="traceback">Traceback (most recent call last):
  File "/usr/lib/python2.7/unittest/case.py", line 327, in run
    testMethod()
  File "/home/ionel/osp/nose-htmloutput/.tox/py27/local/lib/python2.7/site-packages/nose/case.py", line 197, in runTest
    self.test(*self.arg)
  File "/home/ionel/osp/nose-htmloutput/tests/test_sample.py", line 17, in test_b
    assert 0, "Some other details"
AssertionError: Some other details
</pre>
                        <h4>Details</h4>
                        <pre>Some other details</pre>
                    </div>
                </section>
        </div>
    </section>

    <h1>All tests</h1>
    <section>
        <h2>test_sample.MainTestCase (1 failures)</h2>
        <ul>
                <li><a class="success">test_a</a></li>
                <li><a class="failed" href="#test_sample.MainTestCase:test_b">test_b</a></li>
        </ul>
    </section>
    <section>
        <h2>test_sample (1 failures)</h2>
        <ul>
                <li><a class="success">test_a</a></li>
                <li><a class="failed" href="#test_sample:test_b">test_b</a></li>
        </ul>
    </section>
</body>""" in output, output
