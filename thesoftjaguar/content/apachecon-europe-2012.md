Title: ApacheCon Europe 2012
Date: 2012-11-11 20:44
Tags: conference, talk, Apache, Elasticsearch, Solr, Lucene, Hoffenheim, Java
Category: programming
Slug: apachecon-europe-2012
Summary: Brief explanation of Sublime Package Control, how to easily install plugins and a recommended list.

On Wednesday it was ApacheCon day, lot of interesting stuff regarding Apache Lucene, Solr and Elasticsearch. I am not an expert with search engines, and this is a good start for establishing the basic concepts and understanding how some people have solved search problems in their systems.

![Captain Obvious strikes again](https://pbs.twimg.com/media/A7Fb2aPCAAAtQy2.jpg)

## Compound Terms Query Parser for Great Shopping Experience

This [talk](http://www.apachecon.eu/schedule/presentation/18/?utm_source=twitter&utm_medium=social&utm_content=79e580ba-95ca-43cb-9739-95693cf4770e) explained the problem of returning precise search results when there are tricky queries, based on [Space Optimizations for Total Ranking](http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&ved=0CCcQFjAA&url=http%3A%2F%2Flucene.sourceforge.net%2Fpapers%2Friao97.ps&ei=7O-fUPHRLYSh4gTA4IGQCA&usg=AFQjCNF3SmHeiPe-h1A48ztdx8Qx1R-r7w) paper, and a match spotting using the info explained by the client and facet counts.

However, there are some queries which are almost impossible to guess, like for example `red jeans` in a search system which supports colors, you will have red clothes matches, matches with trademarks whose name contains `red` or `jeans`. You can minimize the problem, and of course the client only wants exact results, not a huge list of results that he is not going to check, but at the end a nice approach will be less guessing and more freedom to the client in his queries, for instance, specifying if he want to search by color or by trademark.

## Apache Mahout in context

A nice [explanation](http://www.apachecon.eu/schedule/presentation/1/) of the Apache Mahout project as a data analysis tool, and use cases of what we can do with our huge load of data.

A good example of this is the `Frequently Bought Together` and `What Other Items Do Customers Buy After Viewing This Item?` tags in an Amazon product page.

## Big Search with Big Data Principles

Eric presented his [problem](http://www.apachecon.eu/schedule/presentation/13/), which consisted in millions of text documents that should be indexed, and they could have really strange formats.

The solution was nice, applying technologies in which they were familiar with, and then he spoke about `Solr4`. We should highlight that `Solr` is becoming a noSQL database itself (`Elasticsearch` as well), having a key/value store engine, and they used `.avro` files for the cache, which was quite interesting.

Other design choices were `ZooKeeper` over `NFS`, `SCP`, etc.. for sending files between nodes (less error prone and more obvious reasons, `ZooKeeper` is powerful), `Apache Tika` as a pipeline, handling the errors with an error query, `Solrmeter` for monitoring (the central monitoring using `Nagios` with the `Solr` plugin), a pooled environment (like for example 1 node for development, 6 for production and the rest for load testing) and a `Grim Reaper` for restarting instances which are not working as expected.

In addition, there were some problems which are still present, like the user queries analysis, done with Solrmeter or reading them in an excel file, and the cycle scavenging, which is being done with `Condor` but not without complications.</p>

![Hoffenheim Arena looks good at night](http://i.imgur.com/puR3H.jpg)

## Solr 4: The SolrCloud Architecture

And it was the turn of [showing](http://www.apachecon.eu/schedule/presentation/23/) how to hack a project that wasn't planned for distributed searching from the beggining, one of the biggest weaknesses in Solr.

I want to highlight the use of `MurmurHash` for assigning the documents to the different shards, `ZooKeeper` again (in Elasticsearch this is definitely handled in a nicer way), `PeerSync` for data replication and so on, and a last introduction to Netflix child: `Chaos Monkey`, used for testing.

SolrCloud hasn't convinced me, there are some problems when you want to scale the system, because there is a shard limit that you have to set at first, so `SolrCloud` will assign a hash range to each shard. There are some hacks for allowing this, like the shard split (so the hash range will be reassigned). That's another problem that we have in Elasticsearch, but the shard arranging is automatic.

## Personalized Search on the Largest Flash Site in America (Gilt)

Another talk regarding a [problem](http://www.apachecon.eu/schedule/presentation/21/) and how a company has solved it.

They were using Solr for getting only the items id (`skuId` and `lookId`), so Solr had only the index. Then, they enriched the search result asking the database for the rest of the params. For being able to do all of this, they created three own plugins for Solr, I didn't like this approach and in one case was a little hacky, but they know better about their own systems and at the end it was working as they expected it to work.

Like with the first talk, we had the problem of the search query: the product data is not clean, it can have distractive descriptions, poorly named colors and misleading brand names. It was interesting how tricky can be the synonyms if your search engine supports this feature. At the end we have the same conclusion: maybe it is better if you leave that choice to the user for avoiding bad results.

![Color names if you are a girl](https://pbs.twimg.com/media/A7G74L7CUAU6XLo.jpg)

## Battle of the giants: Apache Solr 4.0 vs Elasticsearch

The last [talk](http://www.apachecon.eu/schedule/presentation/24/) was the one in which I put more expectations, and it didn't convince me, maybe because I was hyped.

It was a brief explanation of each system, which is not bad, but some query examples would have helped a lot. Elasticsearch seemed really promising with the prospective search, nested objects, moving shard and replicas, more indices storage options, index structure and not needing to reload the config. And that's what Solr doesn't have.

There were also some features supported by both and well, Solr supports multilingual data handling, but is not enough. I really want to try both systems but right now, from the beginning, `Elasticsearch` is more interesting for me, especially if I want to have a distributed search environment.