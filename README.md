<h1 class="gap">0x05. AirBnB clone - RESTful API</h1>

<div class="panel panel-default">
    <div class="panel-heading">
      <h3class="panel-title">Concepts</h3>
    </div>
<div class="panel-body">
      <p>
        <em>For this project, we expect you to look at these concepts:</em>
      </p>

<ul>
    <li>
    <a href="/concepts/45">REST API</a>
    </li>
    <li>
    <a href="/concepts/74">AirBnB clone</a>
    </li>
</ul>
</div>

<div class="panel-body">
    <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><strong>REST API</strong> concept page</li>
<li><a href="/rltoken/3VSBUEevk8P0IqD9nOAufQ" title="Learn REST: A RESTful Tutorial" target="_blank">Learn REST: A RESTful Tutorial</a> </li>
<li><a href="/rltoken/AKXWhAP6aSxW5qkeiOZQ1Q" title="Designing a RESTful API with Python and Flask" target="_blank">Designing a RESTful API with Python and Flask</a> </li>
<li><a href="/rltoken/lQBbh8DvlJqZYQ5BjCoKvQ" title="HTTP access control (CORS)" target="_blank">HTTP access control (CORS)</a> </li>
<li><a href="/rltoken/z-5JbJlKFT3IgQus-PIVyQ" title="Flask cheatsheet" target="_blank">Flask cheatsheet</a> </li>
<li><a href="/rltoken/GTncJD9tIqr-vK69_elqbQ" title="What are Flask Blueprints, exactly?" target="_blank">What are Flask Blueprints, exactly?</a> </li>
<li><a href="/rltoken/A3Xk299_XVsk2YgITFSFgg" title="Flask" target="_blank">Flask</a> </li>
<li><a href="/rltoken/vr_iRcjbQkkbF6nL0_uMsw" title="Modular Applications with Blueprints" target="_blank">Modular Applications with Blueprints</a> </li>
<li><a href="/rltoken/71HoBixu8xcKGc9s1rHU5Q" title="Flask tests" target="_blank">Flask tests</a> </li>
<li><a href="/rltoken/lWP9TDsRX4Kh9OmB9w4cuA" title="Flask-CORS" target="_blank">Flask-CORS</a> </li>
<li><a href="/rltoken/NlyqPr9_qnkeUzrIZOP9cw" title="AirBnB clone - RESTful API" target="_blank">AirBnB clone - RESTful API</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/j9ZA4jU5NTvFvDdS9D5-SQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What REST means</li>
<li>What API means</li>
<li>What CORS means</li>
<li>What is an API</li>
<li>What is a REST API</li>
<li>What are other type of APIs</li>
<li>Which is the HTTP method to retrieve resource(s)</li>
<li>Which is the HTTP method to create a resource</li>
<li>Which is the HTTP method to update resource</li>
<li>Which is the HTTP method to delete resource</li>
<li>How to request REST API</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version 1.7)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h3>Python Unit Tests</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="/rltoken/rDWOaLClDSmStCix0b4kyA" title="unittest module" target="_blank">unittest module</a> </li>
<li>All your test files should be python files (extension: <code>.py</code>)</li>
<li>All your test files and folders should start by <code>test_</code></li>
<li>Your file organization in the tests folder should be the same as your project: ex: for <code>models/base_model.py</code>, unit tests must be in: <code>tests/test_models/test_base_model.py</code></li>
<li>All your tests should be executed by using this command: <code>python3 -m unittest discover tests</code></li>
<li>You can also test file by file by using this command: <code>python3 -m unittest tests/test_models/test_base_model.py</code></li>
<li>We strongly encourage you to work together on test cases, so that you don’t miss any edge cases</li>
</ul>

<h3>GitHub</h3>

<p><strong>There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.</strong></p>

<h2>More Info</h2>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/02078cd7f0573885c85a225c7436584a5afea1f9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220915%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20220915T171052Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=334de3e426b1ee8dc02b966494db838994159c2a12a176d8d0f0ff46d67c960d" alt="" loading="lazy" style=""></p>

<h3>Install Flask</h3>

<pre><code>$ pip3 install Flask
</code></pre>

  </div>
