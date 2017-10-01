<h1>HMEE API</h1>

<ol>
	<li><a href="#intro">Introduction</a></li>
	<li><a href="#endpoints">Endpoints</a>
		<ol>
			<li><a href="#parks">Parks</a></li>
			<li><a href="#lands">Lands</a></li>
			<li><a href="#attractions">Attractions</a></li>
			<li><a href="#mickeys">Mickeys</a></li>
		</ol>
		</li>
	<li><a href="#install">Installation</a></li>
	<li><a href="#testing">Testing</a></li>
</ol>

<h2 id="intro">Introduction</h2>
<p>API built with Python and PostgreSQL for Hidden Mickeys and Easter Eggs</p>

<h2 id="endpoints">Endpoints</h2>
<p>Base URL: https://hmee-api.herokuapp.com</p>

<h3 id="parks">Parks</h3>
<p>DLR parks</p>
<ul>
	<li>GET: /parks - a list of all parks</li>
	<li>GET: /parks/:id - a single park by ID</li>
</ul>

<h3 id="lands">Lands</h3>
<p>DLR lands, organized by park</p>
<ul>
	<li>GET: /lands - a list of all lands</li>
	<li>GET: /parks/:park_id/lands - a list of lands by park</li>
	<li>GET: /lands:id - a single land by ID</li>
</ul>

<h3 id="attractions">Attractions</h3>
<p>DLR attractions - organized by park and land</p>
<ul>
	<li>GET: /attractions - a list of all attractions</li>
	<li>GET: /parks/:park_id/attractions - a list of attractions by park</li>
	<li>GET: /lands/:land_id/attractions - a list of all attractions by land</li>
	<li>GET: /attractions/:id - a single attraction by ID</li>
</ul>

<h3 id="mickeys">Mickeys</h3>
<p>Hidden Mickeys and Easter Eggs. Referred henceforth as "Mickeys"</p>
<ul>
	<li>GET: /mickeys - a list of all Mickeys</li>
	<li>GET: /parks/:park_id/mickeys - list of Mickeys by park</li>
	<li>GET: /lands/:land_id/mickeys - list of all Mickeys by land</li>
	<li> GET: /attractions/:attraction_id/mickeys - list of all Mickeys by attraction</li>
	<li>GET: lands/:land_id/mickeys/none - list of Mickeys by land where attraction_id = null</li>
	<li>POST: /mickeys - add new row. *NOTE: content-type: application/json REQUIRED</li>
	<li>PUT: /mickeys/:id - updates single row. *NOTE: content-type: application/json REQUIRED</li>
	<li>DELETE: /mickeys/:id - deletes single row</li>
</ul>

<h2 id="install">Installation</h2>
<p>Installation for local development:</p>
<ul>
	<li>git clone https://github.com/Ljyockey/hmee-api.git</li>
	<li>pip install requirements.txt</li>
	<li>export APP_SETTINGS="config.DevelopmentConfig"</li>
	<li>export DATABASE_URL="https://hmee-api.herokuapp.com"</li>
	<li>python run.py</li>
	<li>localhost:5000</li>
</ul>

<h2 id="testing">Testing</h2>
<p>python manage.py test</p>

