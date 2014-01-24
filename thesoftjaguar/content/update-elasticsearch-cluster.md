Title: Update your Elasticsearch cluster without drama
Date: 2014-01-24 12:17
Tags: elasticsearch, lucene, open-source, big-data, java, search, scale
Category: programming
Slug: update-elasticsearch-cluster
Summary: Examples about different updates and migration approaches for your Elasticsearch cluster.

Even if we have a big or a small Elasticsearch (ES) cluster, we most surely want to update the ES version, Java version, cluster name, move some ES folders, or any other change, without downtime. And that, in most cases, is possible, or even with minimum downtime, depending on your requirements.

# Elasticsearch data

## How is it managed?

ES manages the data in *shards* and *replicas*.

Briefly, a cluster has indexes, each index has data, and that data has to be divided in a way, because we want to have distributed search, and that's where ES excels: it needs shards.

A *shard* is a unique part of that data, and will be identified by an integer, starting from 0.

A *replica* is just a copy of a primary shard, for redundancy and performance reasons. It will have a shard identifier, appearing multiple times in the cluster.

Is crucial to understand the [cluster, index and shard health status](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/cluster-health.html). We don't want to operate with a red cluster, even if 'sometimes' will work. We are not confident using a yellow cluster, all the shards will be there, and the cluster is operational, but if a disaster happens, we may lose data, because the redundancy is not guaranteed. And sadly, sometimes we won't achieve a green cluster, because it may take too much time (replicating data is not usually fast). And example of the last one can happen when we are rebooting some nodes.

![Assigning some shards](http://i.imgur.com/hjYzuX6.png)

## Where is it?

Before doing anything, we have to locate where ES is storing the data. We can configure it with the `path.data` setting in `elasticsearch.yml`.

`path.data` will have a folder by each cluster name. If our cluster is called `russian_videos`, it will appear there with that name. Actually, this is the folder that you want to back up (if that node is having all the shards).

And this is *very important*. If you back up the data from a node that only has 3 shards (out of 5), it doesn't make much sense. You will go to `nodes/0/indices/russian_videos_indice1` and you may see 3 folders with the shard number, but 2 of them will be missing.

However, there is one point in which we will have all the shards in one node: when the cluster has two nodes. If the cluster is green, ES will distribute the shards among those two nodes (because they will be replicated).

## How can I back up and restore my data?

Even if we can back it up copying it from the data folder when the specified node has all the shards, I don't think it will be suitable for most cases. There are many alternatives, I will specify two:

### Scan/scroll and bulk create
If you are still working with ES 0.90, this is my preferred method. Whenever you need to back up data from an index, just retrieve that data using a [scan](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-request-search-type.html#scan) search type, giving a scroll parameter. And then, you can store it in a file or wherever you want, as it comes in JSON format.

When you want to restore data from that source, just use the [bulk API](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-bulk.html). For instance, you can read JSON from a file, and for each document, buffer them in a bulk index/create operation with 1000 documents (which can be handled quite nicely in memory). The main difference between indexing and creating is that the first won't be inserted if its id already exists. *Don't index each document individually! The bulk operation is far faster than this, and is designed for this purpose.

### Snapshot & restore
Starting from ES 1.0, the [snapshot & restore](http://www.elasticsearch.org/blog/introducing-snapshot-restore/) function is introduced. This is, of course, the *recommended way*. However, if you are stuck in a previous ES version, you don't have other choice than to figure out how to make your own back ups.

# Mess with the cluster!

## Update the ES version and live for another day

First of all, check the *breaking changes* for all the ES versions that are above the current one (read the *release notes*), until the one that you want to update. This will avoid terrible surprises, but I hope that you have snapshot your data before this point.

If the new version doesn't break anything, you can just stop each node, update its ES version, and start it. The node should join the cluster again, get the shards/replicas with 0 downtime.

![Cluster's general info](http://i.imgur.com/unjTQPz.png)

I don't recommend having different ES versions in the same cluster, which is actually not always possible if they are very different, like 1.0 and 0.90, and with the previous method that will happen, at least for some time.

In that case you can always play with the firewall, using the same cluster name but avoiding the communication between nodes with different ES versions (so ES will create two different clusters with that name). At the end, if you want 0 downtime, you can always point the applications to the other cluster when you have to shut down the last node in the old cluster, this is up to you.

## Change the JVM and tell your grandchildren

This one is quite easy. Install your new JVM (for instance, from OpenJDK to Oracle's), and after restarting ES, if that JVM is the default in the system, ES will use it. If you update that JVM, an ES restart will do the trick of course.

ES can convive with nodes with different JVMs, though is always good being as much consistent as possible, it shouldn't give any problems while we update all the instances.

![JVM description](http://i.imgur.com/ZpcY1Fm.png)

And the end you have to remember that we will achieve a green cluster with two nodes, and we can survive (yellow cluster) with one node.

## Change the cluster name, don't lose data and extend your life expentancy

You can't change the cluster name. You can create a new cluster with a new name, for instance `mother_russia`, and then, if we store the stored data from `russian_videos` (remember the `path.data` setting) into `mother_russia`, you will be fine.

!['trackit' cluster data stats](http://i.imgur.com/pZ9ju9f.png))

However, you have to do that process in a node that is having all the shards. A way for achieving this can be stopping all the instances until two of them are left in the cluster, then copy the data from one cluster name to another, delete the old cluster (if you see that the data has been copied succesfully), and start the other instances. They will replicate those primary shards and giving it time, those primary shards will be distributed among the different instances.

# Conclusion

Starting from the point in which you always back up your data, the worst case scenario would be downtime. If you understand how ES manages sharding, and the communication between nodes, even if you are testing in production, you will have zero downtime because you can perform those "tests" in a single instance.

![If you know what you are doing...](http://i.imgur.com/BRnzsBa.jpg))

You will see if that node is communicating properly with the rest and extend the changes to the others if everything is fine.

Don't be afraid, don't be lazy, update your ES instances, your JVMs, do it properly and if everything explodes, call the eagles (snapshots).

![Yes, eagles...](http://i.imgur.com/52DARgZ.jpg)
