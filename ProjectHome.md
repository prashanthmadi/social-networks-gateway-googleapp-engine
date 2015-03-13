# SocioApi #

## Main Goals : ##
  * Ability to login most of Social Networks.
  * Search Engine
  * Ranking Search Results
  * Clustering Search Engine Results
  * Organize Data

### Social Login: ###
Ability to make User login to any Social Network.
<br>
<b>Demo :</b> <a href='http://socioapi.appspot.com/'>http://socioapi.appspot.com/</a>

<h3>Search Engine :</h3>
Search with query should result matched data.<br>
<br>
<b>Demo :</b> <a href='http://socioapi.appspot.com/search'>http://socioapi.appspot.com/search</a>
<br><br>
<a href='https://code.google.com/p/social-networks-gateway-googleapp-engine/source/browse/src/com/prashanth/searchengine/preprocess/PreProcesser.py'>PreProcess Steps</a>
<br>
<br>
Further planning to add ability of query expansion using WordNet<br>
<br>example : loan<br>
<br>noun.  	advance - accommodation - borrowing - debt - loaning<br>
<br>verb.  	lend - borrow<br>
<br>
<br>
<h3>Ranking Search Results :</h3>
<ul><li>Using Cosine Similarity to get the distance between query and data<br>
</li><li>Planning to Conect current scenario with Page Rank Algorithm (used in google). I had implemented a version of Page Rank in Scala, need to work on python implementation  <a href='https://code.google.com/p/page-rank-scala/source/browse/src/com/prashanth/graph/PageRank.scala'>link</a></li></ul>

<h3>Clustering Search Engine Results :</h3>
<b>Problem :</b> Manager wants some data about how many people are facing problem with insurance.. with Relational db running a query on un-organized data  wont be good idea.<br>
<br>
<b>Solution :</b> I wrote a Search Engine Few years back with an ability to cluster the Search results and query extension. Please find a flow of pictures in below link, they would make it clear about this.<br>
<br>
<a href='https://code.google.com/p/search-engine-perl/'>Project Details</a>  <a href='https://search-engine-perl.googlecode.com/files/Search_Engine.pdf'>PPT</a>  <a href='https://search-engine-perl.googlecode.com/files/Clustering_Search_Results.pdf'>PDF</a>
<br>

Above approach is based on single linkage clustering, instead planning to make use  combination of single and complete linkage clustering.<br>
<i>use previous work on<br>
<ul><li>gene sequence clustering</i> <a href='https://page-rank-scala.googlecode.com/files/Clustering_of_sequences_using_Esprit_and_CD-HIT.pdf'>link</a> (BOW MODEL)<br>
</li><li><i>Clustering Documents Using Wikipedia Minor</i> <a href='https://page-rank-scala.googlecode.com/files/clustering_documents_using_wikipedia.pdf'>link</a> (Semantic Analysis Using Wikipedia Miner)  <i>cat and bag -> 20% , cat and dog -> 75%</i></li></ul>



<h3>Organize Data :</h3>


<blockquote>This can be done n number of ways.. my intention is to split the content into two types for now.Do the post made on facebook/twitter/.. depicts positive or negative about the company. This is a kind of process automation, where we extract all the negative feedback and process it to further level.</blockquote>

<b>Problem :</b> User needs to read all the posts and organize manually as positive or negative posts and process it to other people who take the required steps.<br>
<br>
<b>Solution :</b><br> 1) I did some work few years back on polarity Detection. I made it public in <a href='http://prashanthmadi.blogspot.com/2010/11/nlp-project.html'>Blog</a>
<br>
2) Using NLTK Package to get sentiment of input data<br>
<a href='http://text-processing.com/demo/sentiment/'>link</a>