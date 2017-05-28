# Project5: New York City Traffic Analysis

Developed a Hadoop Mapper and Reducer scripts in Python that can analyse the vehicular incidents data in New York City and yields the total count per vehicle type that got involved in an incident and generate a summary statistic.

This project contains i. bindu_mapper.py - Code for mapper ii.bindu_reducer.py - Code for reducer
iii.finalout -It contains final output

Command line used on the Hadoop server to execute program:

hadoop jar /opt/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -file /home/kanakahu/bindu_mapper.py -mapper /home/kanakahu/bindu_mapper.py -file /home/kanakahu/bindu_reducer.py -reducer /home/kanakahu/bindu_reducer.py -input /data/nyc/nyc-traffic.csv -output /user/kanakahu/hw4_hadoopoutput

