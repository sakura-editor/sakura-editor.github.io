#!/usr/bin/python

import os
import codecs
import string
import re

#  <!-- Global site tag (gtag.js) - Google Analytics -->
#  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-120820034-1"></script>
#  <script>
#    window.dataLayer = window.dataLayer || [];
#    function gtag() { dataLayer.push(arguments); }
#    gtag('js', new Date());
#    gtag('config', 'UA-120820034-1'); // kobake 所有の Google Analytics tracking code
#  </script>

# <script type="text/javascript" src="/hoge/huga/hoge.js"></script>
def replace_js_file(path, out_path, js_file):
	data = '''<!-- Start Google Analytics -->
<script type="text/javascript" src="{filename}"></script>
<!-- End Google Analytics -->
'''.format(filename=js_file)

	with codecs.open(out_path, 'w', 'utf-8') as f_out:
		startTag = False
	
		with codecs.open(path, 'r', 'utf-8') as f_in:
			for line in f_in:
				if re.search('Google Analytics', line) and re.search('<!--', line):
					startTag = True
				elif startTag and re.search('</script>', line):
					startTag = False
					f_out.write(data)
				elif not startTag:
					f_out.write(line)

js_file = os.path.abspath('googleanalytics.js')
scriptdir = os.path.dirname(os.path.realpath(__file__))
for dirpath, dirnames, filenames in os.walk(scriptdir):
	for file in filenames:
		if file.endswith('.html'):
			js_relative_path = os.path.relpath(js_file, dirpath)
			js_relative_path = js_relative_path.replace('\\', '/')
			path = os.path.join(dirpath, file)
			
			out_path = path + ".tmp"
			replace_js_file(path, out_path, js_relative_path)

			print (js_relative_path, path)
			os.remove(path)
			os.rename(out_path, path)
