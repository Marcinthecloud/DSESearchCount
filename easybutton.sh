echo "This is an embarrassingly simple script"

echo "creating keyspace and schemas"
cqlsh -f 'schema.cql'

echo "uploading DSE Search (solr) files"
dsetool create_core dsecount.accounts schema=schema.xml solrconfig=config.xml reindex=true

echo "done!"
