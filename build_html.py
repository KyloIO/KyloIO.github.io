from jinja2 import Environment, FileSystemLoader, select_autoescape

# variables used in the base template
footer_links = [
	{
		'name': 'Overview',
		'href': 'index.html',
       	'target': '_self',
		'sublinks': [ ]
	}, {
		'name': 'Quickstart',
		'href': 'quickstart.html',
       		'target': '_self',
		'sublinks': [
			{'name': 'Download Sandbox', 'target': '_self', 'href': 'quickstart.html'},
			{'name': 'Intro Tutorial','target': '_self', 'href': 'quickstart.html'}
		]

	}, {
       		'name': 'Tutorials',
       		'href': 'tutorials.html',
       		'target': '_self',
       		'sublinks': [ ]

       	}, {
		'name': 'Docs',
		'href': 'docs.html',
        'target': '_self',
		'sublinks': [ ]

	}, {
       		'name': 'Source',
       		'href': 'https://github.com/KyloIO/kylo',
       		'target': '_blank',
       		'sublinks': [ ]
     }, {
		'name': 'Community',
		'href': '#',
		'display_subs': 'true',
		'sublinks': [
			{'name': 'Forum Q&amp;A', 'target': '_blank', 'href': 'https://groups.google.com/forum/#!forum/kylo-community'},
			{'name': 'Issues', 'target': '_blank', 'href': 'https://kylo-io.atlassian.net/projects/KYLO'},
			{'name': 'Contributing', 'target': '_self', 'href': 'http://kylo.readthedocs.io/en/latest/developer-guides/ContributingtoKylo.html'},
		]
	},
]



key_features = [
		{
			'heading': '<span class="text-blue">Ingest</span> ',
		 	'description': 'Self-service data ingest with data cleansing, validation, and automatic profiling.',
            'long_description': 'Organizations can expend significant engineering effort moving data into Hadoop yet struggle to maintain governance and data quality. Kylo dramatically simplifies data ingest by shifting ingest to data owners through a simple guided UI. <br/><br/> Kylo can connect to most sources and infer schema from common data formats. Kylo\'s default ingest workflow moves data from source to Hive tables with advanced configuration options around field-level validation, data protection, data profiling, security, and overall governance.<br/><br/>Using Kylo\'s pipeline template mechanism, IT can extend Kylo\'s capabilities to connect to any source, any format, and load data into any target in a batch or streaming pattern. <br/><a class="btn btn-sm link-more" href="http://kylo.readthedocs.io/en/latest/about/KyloFrequentlyAskedQuestions.html#data-ingest" target="_blank" role="button">READ FAQ</a><a class="btn btn-sm link-more" href="https://youtu.be/DdlvQmyLRc8?t=44" target="_blank" role="button">WATCH VIDEO</a>'
            ,'image':'assets/feature-placeholder-1c.jpg'
		},
		{
			'heading': '<span class="text-blue">Prepare</span> ',
		 	'description': 'Wrangle data with visual sql and an interactive transform through a simple user interface.',
            'long_description': 'Preparing data is the first step in any analytics project.  Using Kylo\'s transformation feature, IT can step aside and let power users such as data analysts take control of their own data preparation tasks. Kylo leverages the latest capabilities of Apache Spark to create interactive data transformation. Organizations can throw out their old ETL tools and save hundreds of thousands of dollars in license and maintenance fees.<br/><a class="btn btn-sm link-more" href="https://youtu.be/DdlvQmyLRc8?t=307" target="_blank" role="button">WATCH VIDEO</a>'
            ,'image':'assets/feature-placeholder-2c.jpg'
		},
		{
			'heading': '<span class="text-blue">Discover</span> ',
		 	'description': 'Search and explore data and metadata, view lineage, and profile statistics.',
            'long_description': 'What\'s the point of having a data lake if users can\'t find data or trust what is there? Kylo includes an integrated metadata repository and key capabilities for data exploration. Users can perform Google-like searches against data and metadata to discover entities of interest.   Visual process lineage and provenance provides confidence in the origin of data. Automatic data profiling provides capabilities for data scientists and assurance in data quality.<br/><a class="btn btn-sm link-more" href="https://youtu.be/DdlvQmyLRc8?t=207" target="_blank" role="button">WATCH VIDEO</a>'
            ,'image':'assets/feature-placeholder-3c.jpg'
		},
		{
			'heading': '<span class="text-blue">Monitor</span>',
		 	'description': 'Monitor health of feeds and services in the data lake. Track SLAs and troubleshoot performance.',
		 	'long_description': 'IT Operations are the carekeepers of your production data lake. Kylo departs from traditional monitoring tools to provide health indicators from a feed-centric perspective.  This means Operations has not only visibility on service issues impacting availability, but can track service levels associated with data arrival and distinct quality metrics.  Using Kylo, IT can give users confidence in data maintained in the data lake.  <br/><a class="btn btn-sm link-more" href="https://youtu.be/DdlvQmyLRc8?t=798" target="_blank" role="button">WATCH VIDEO</a>'
            ,'image':'assets/feature-placeholder-4c.jpg'
		},
        {
            'heading': '<span class="text-blue">Design</span>',
            'description': 'Design batch or streaming pipeline templates in Apache NiFi and register with Kylo to enable user self-service.',
            'long_description': 'IT Designers can extend Kylo\'s feed capabilities around ingest, transformation, and export by developing new pipeline templates in Apache NiFi. NiFi provides a visual canvas with over 180 data connectors and transforms for batch and stream-based processing.  Kylo and NiFi together act as an "intelligent edge" able to orchestrate tasks between your cluster and data center.<br/><br/>Designers develop and test new pipelines in Apache NiFi and register templates with Kylo determining what properties users are allowed to configure when creating feeds.  This embodies the principle of write-once-use-many and enables data owners instead of engineers to create new feeds while IT retains control over the underlying dataflow patterns.  <br/>  <br/>Kylo adds a suite of NiFi processors for Spark, Sqoop, Hive, and special purpose data lake primitives that provide additional capabilities. <br/><a class="btn btn-sm link-more" href="https://youtu.be/DdlvQmyLRc8?t=442" target="_blank" role="button">WATCH VIDEO</a>'
            ,'image': 'assets/feature-placeholder-5c.jpg',
        }
]

testimonials = [
        {
            'speaker': 'Ka Tang',
            'title': 'Director, Enterprise Data Architecture',
            'headline': 'Discover Financial Services',
            'quote': 'Discover is focused on leveraging leading edge technology that helps us quickly bring products to market while providing exceptional customer service. Kylo has a unique framework that has the potential to accelerate development and value on new data sources that leverage Apache NiFi.',
        },
		{
			'speaker': 'Matt Hutton',
			'title': 'Director, R&amp;D',
			'headline': 'Think Big, A Teradata Company',
            'quote': 'Our commitment to open-source Kylo was a no-brainer given the tremendous benefits we have received from the Hadoop ecosystem.  Kylo\'s success in beta with over a dozen major organizations worldwide gives us confidence that this contribution will help advance the community and the organizations we serve.',		},
		{
			'speaker': 'Rick Farnell',
			'title': 'President, Think Big',
			'headline': 'Think Big, A Teradata Company',
			'quote': 'Kylo embodies our Velocity brand. Think Big leverages Kylo to help customers move quickly beyond fundamental data management hurdles to deriving business value from analytic insights.',
		},
]


def build_index():

	template = env.get_template('index-template.html')
	return template.render(features=key_features, testimonials=testimonials, footer_links=footer_links)


def build_tutorials():
## {
## "heading": "title of the tutorial"
## "description": "short desc"
## "long_description": "longer desc with Read More link"
## "video": "url to the video"
## "image": "url to an image, if no video"
## "documentation_link": " alt link to additional docs"
## }

	user_tutorials = [
		{
			"heading": "Creating a Data Ingest Feed",
			"description": "Create an data ingest feed using Kylo that ingest data from a flat file, applies cleansing and validation rules and brings it into hadoop.",
			"video": "https://www.youtube.com/embed/lLBsxXlTljo?vq=hd1080"
		},
		{
			"heading": "How to Wrangle Data (Part 1)",
			"description": "Learn how to easily transform and prepare data.",
			"video": "https://www.youtube.com/embed/BIHJGItqgac?vq=hd1080"
		},
        {
            "heading": "How to Wrangle Data (Part 2)",
            "description": "Continue on with data wrangling and learn more advanced functions and things you can do with the Kylo data wrangler. ",
            "video": "https://www.youtube.com/embed/hPEurrMk11I/vq=hd1080"
        },
        {
        	"heading": "Import and Export Feeds",
        	"description": "Learn how to export a feed from one environment and import it into another environment.",
        	"video": "https://www.youtube.com/embed/x64nzg0ZtoM?vq=hd1080"
        },
		{
			"heading": "More Features",
			"description": "Watch a summary video that explores many features of Kylo including designing and registering templates, data ingestion, and data wrangling.",
			"video": "https://www.youtube.com/embed/DdlvQmyLRc8?vq=hd1080"
		}

	]

	designer_tutorials = [
        {
            "heading": "Introduction to Templates",
            "description": "This is an introductory tutorial on the concept of templates in Kylo. Feed templates embody the principle of write once/reuse many times. ",
            "video": "https://www.youtube.com/embed/_lw3zvlqH8k?vq=hd1080"
        },
        {
            "heading": "How to Create Modular Flows",
            "description": "This tutorial looks at techniques for creating modular feeds used as services and invoked by other feeds.",
            "video": "https://www.youtube.com/embed/P6slvtxwMaM?vq=hd1080"
        },
        {
            "heading": "Templates with Conditional NiFi Routing",
            "description": "This advanced tutorial demonstrates how to take advantage of Apache NiFi routing and NiFi expressions to make templates more general purpose",
            "video": "https://www.youtube.com/embed/XbRrK24N2Do?vq=hd1080"
        },
        {
            "heading": "Connecting to a Reusable Flow",
            "description": "Learn how to create a simple feed based template and connect it to a reusable flow. ",
            "video": "https://www.youtube.com/embed/Vj641MRJCd8?vq=hd1080"
        },
        {
            "heading": "Design a Data Confidence Feed",
            "description": "Learn how to design and create a data confidence feed using Kylo.",
            "video": "https://www.youtube.com/embed/vy68_mBGqO0?vq=hd1080"
        },
        {
            "heading": "Design a Feed with Preconditions",
            "description": "Learn how to design a flow that depends upon the completion of another feed.",
            "image": "assets/trigger_feed.png",
            "documentation_link":"http://kylo.readthedocs.io/en/latest/how-to-guides/NiFiProcessorsDocs.html#triggerfeed",
        },
        {
            "heading": "Sqoop Based Ingest (Part 1)",
            "description": "In this tutorial shows how to configure and run Sqoop based ingestion in Kylo. This specific video shows template registration.",
            "documentation_link":"http://kylo.readthedocs.io/en/latest/how-to-guides/NiFiProcessorsDocs.html#importsqoop-processor",
            "video": "https://www.youtube.com/embed/9bx9JQ3ica4?vq=hd1080"
        },
        {
            "heading": "Sqoop Based Ingest (Part 2)",
            "description": "Learn how to configure and run a Sqoop based ingestion in Kylo. This video (part 2) shows how to create a feed that ingests a table for each run.",
            "video": "https://www.youtube.com/embed/TpHI7dB61Ck?vq=hd1080"
        },
        {
            "heading": "Sqoop Based Ingest (Part 3)",
            "description": "Extend upon the previous Sqoop video and learn more about how to configure it with Kylo.",
            "video": "https://www.youtube.com/embed/Ox7HD9LGbuA?vq=hd1080"
        }
	]

	admin_tutorials = [
        {
           "heading": "Kylo Installation",
            "description": "Learn how to install Kylo.",
            "documentation_link":"http://kylo.readthedocs.io/en/latest/installation/KyloDeploymentGuide.html",
            "image":"assets/kylo.png"
        },
        {
            "heading": "Encrypting Properties ",
            "description": "Learn how to encrypt configuration properties.",
            "documentation_link":"http://kylo.readthedocs.io/en/latest/installation/KyloDeploymentGuide.html#encrypting-configuration-property-values",
            "image":"assets/kylo.png"
        }
	]

	best_practices = [
        {
           "heading": "Best Practices ",
            "description": "Learn patterns and best practices for using and supporting Kylo.",
            "documentation_link":"http://kylo.readthedocs.io/en/latest/tips-tricks/KyloBestPractices.html",
            "image":"assets/checklist-2.png"
        }
	]

	tutorials = [
	    {
	        "name": "User Tutorials",
	        "tutorials": user_tutorials,
	        "href":'user_tutorials',
	        "short_name":"Users"
	    },
	    {
            "name": "Designer Tutorials",
            "tutorials": designer_tutorials,
            "href":'designer_tutorials',
            "short_name":"Designers"
        },
        {
            "name": "Administrator Tutorials",
            "tutorials": admin_tutorials,
            "href":'admin_tutorials',
            "short_name":"Administrators"
        },
        {
            "name": "Best Practices",
            "tutorials": best_practices,
            "href":'best_practices',
            "short_name":"Best Practices"
        }
]

	template = env.get_template('tutorials-template.html')
	return template.render(tutorials=tutorials, footer_links=footer_links)

def quickstart_overview():

	items = [ 
		{
			"heading": "Creating a Data Ingest feed",
			"description": "Create an data ingest feed  <a href=\"assets/userdata6.csv\">Download sample file</a>",
			"video": "https://www.youtube.com/embed/lLBsxXlTljo?vq=hd1080"
		},
		{
			"heading": "Creating a simple Wrangling feed",
			"description": "Learn how to easily transform and prepare data.",
			"video": "https://www.youtube.com/embed/BIHJGItqgac?vq=hd1080"
		},
		{
			"heading": "Watch full video for more features",
			"description": "Explore many of the features of Kylo",
			"video": "https://www.youtube.com/embed/DdlvQmyLRc8?vq=hd1080"
		}

	]

	applications = [
		{
			"name": "Appname",
			"url": "http://nameoflink:8079",
			"credentials": "username/password",
		},
		{
			"name": "Appname",
			"url": "http://nameoflink:8079",
			"credentials": "username/password",
		},
		{
			"name": "Appname",
			"url": "http://nameoflink:8079",
			"credentials": "username/password",
		},
		{
			"name": "Appname",
			"url": "http://nameoflink:8079",
			"credentials": "username/password",
		},
	]

	template = env.get_template('quickstart-template.html')
	return template.render(items=items, applications=applications, footer_links=footer_links)


def build_docs():

	template = env.get_template('docs-template.html')
	return template.render(footer_links=footer_links)

if __name__ == "__main__":
	env = Environment(
	    loader=FileSystemLoader('templates'),
	    trim_blocks=True,
	    lstrip_blocks=True,
	)

	with open('index.html', 'w') as f:
		f.write(build_index())

	with open('tutorials.html', 'w') as f:
		f.write(build_tutorials())

	with open('quickstart.html', 'w') as f:
		f.write(quickstart_overview())

	with open('docs.html', 'w') as f:
		f.write(build_docs())
