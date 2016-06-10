# DSE Search Count Example
This is a quick and dirty demo to get you started with counting (facets) with *DSE Search*.

#####Prerequisites
* Python 2.7+ (if you want to run the simple Python script)
* [DataStax Python Driver](https://github.com/datastax/python-driver)
* >Note you may have to sudo apt-get install gcc
* [DataStax Enterprise 4.7.3 or greater](https://www.datastax.com/downloads)

#####How-to:
1. Start DataStax Enterprise in search mode
  * ```for tarball installs: bin/dse cassandra -s```
  * ```for package installs: set SOLR=1 in the /etc/default/dse file and run: service dse start```
2. Run ```easybutton.sh```
  * This will create the CQL schemas and upload the propser DSE Search files
3. Go wild!

#####Examples Queries:

`SELECT * FROM dsecount.accounts WHERE solr_query='{"q":"*:*", "facet":{"query":"pod_id:*"}}';`


Let's break it down:
`"q":"*:*"` - This means "Select everything from every column"

`"facet":{"query":"pod_id:*"}` This means "I want to count all the times pod_id occurs in 'q'""

Output looks like:
`{"pod_id:*":6}`

We can also get some other cool logic

`SELECT * FROM dsecount.accounts WHERE solr_query='{"q":"pod_id:*", "facet":{"field":"key"}}';`

This is asking: "For all of my keys, how many times does pod_id X occur?"

The output looks like:
`{"key":{"1":1,"2":1,"3":1,"4":1,"5":1,"6":1}}`
