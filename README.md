Simple blog webapp designed to run with two different languages (python, ruby).
This webapp is just a protype and a proof of concept it is not meant for production environmnet.

<h3>Python webapp Dependencies:</h3>
<ul>
<li>libmysqlclient-dev</li>
<li>python-dev</li>
<li>python-pip</li>
</ul>

To run with vagrant just run `vagrant up`
Once in the vagrant box run `# python setup.py install`
Make sure you setup a mysql database and to update the config.yaml.

To run the webapp you can use a process control system or run the python app manually:
`# python pyapp -c /path/to/config.yaml`

<h3>Laravel webapp(under development)</h3>
<ul>
<li>requires php5.4 and above</li>
</ul>
