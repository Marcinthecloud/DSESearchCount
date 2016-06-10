#Contact marc.selwan@datastax.com for help
__author__ = 'marcselwan'
from cassandra import ConsistencyLevel
import json

# Connection Constants
KEYSPACE = 'dsecount'
CONSISTENCY=ConsistencyLevel.LOCAL_ONE
SEED_NODES = ['127.0.0.1']
DATACENTER = None

# Cassandra Constants
TABLE = 'accounts'

# Connection class so we can reuse open connections
def connect(seeds, keyspace, datacenter=None, port=9042):
    from cassandra.io.libevreactor import LibevConnection
    from cassandra.cluster import Cluster
    from cassandra.policies import DCAwareRoundRobinPolicy, RetryPolicy, ExponentialReconnectionPolicy

    class CustomRetryPolicy(RetryPolicy):

        def on_write_timeout(self, query, consistency, write_type,
                             required_responses, received_responses, retry_num):

            # retry at most 5 times regardless of query type
            if retry_num >= 5:
                return (self.RETHROW, None)

            return (self.RETRY, consistency)


    load_balancing_policy = None
    if datacenter:
        # If you are using multiple datacenters it's important to use
        # the DCAwareRoundRobinPolicy. If not then the client will
        # make cross DC connections. This defaults to round robin
        # which means round robin across all nodes irrespective of
        # data center.
        load_balancing_policy = DCAwareRoundRobinPolicy(local_dc=datacenter)

    cluster = Cluster(contact_points=seeds,
                      port=port,
                      default_retry_policy=CustomRetryPolicy(),
                      reconnection_policy=ExponentialReconnectionPolicy(1, 60),
                      load_balancing_policy=load_balancing_policy,
                      protocol_version=3)

    cluster.connection_class = LibevConnection
    cluster.connection_class = LibevConnection
    cluster.control_connection_timeout = 10.0
    cluster.compression = False
    session = cluster.connect(keyspace)
    print 'Connection established with seed(s): %s at port: %s and keyspace: %s' %(seeds,port,keyspace)
    return session

def solr_facet(connection):
    facet = connection.execute("""SELECT * FROM %s.%s WHERE solr_query='{"q":"*:*", "facet":{"query":"pod_id:*"}}';"""% (KEYSPACE, TABLE))
    for rows in facet:
        i=rows.facet_queries
        s=json.loads(i)
        print s["pod_id:*"]
            





if __name__ == "__main__":
    # Create a single session multiple functions/casses can use
    connection = connect(SEED_NODES, keyspace=KEYSPACE, datacenter=DATACENTER)

    # Queries
    solr_facet(connection)
    print 'fin!'
