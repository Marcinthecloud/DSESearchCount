CREATE KEYSPACE dsecount WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}  AND durable_writes = true;

CREATE TABLE dsecount.accounts (
    key text PRIMARY KEY,
    pod_id int
) WITH bloom_filter_fp_chance = 0.01
    AND caching = '{"keys":"ALL", "rows_per_partition":"NONE"}'
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy'}
    AND compression = {'sstable_compression': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99.0PERCENTILE';


INSERT INTO dsecount.accounts (key, pod_id) VALUES ( '1', 4) ;
INSERT INTO dsecount.accounts (key, pod_id) VALUES ( '2', 3) ;
INSERT INTO dsecount.accounts (key, pod_id) VALUES ( '3', 4) ;
INSERT INTO dsecount.accounts (key, pod_id) VALUES ( '4', 4) ;
INSERT INTO dsecount.accounts (key, pod_id) VALUES ( '5', 4) ;
INSERT INTO dsecount.accounts (key, pod_id) VALUES ( '6', 4) ;
