#!/bin/sh -e
# as root
# get the data file from the remote server
# copy in the data file to /var/lib/mysql/avox as avox.txt
# then in /var/lib/mysql/avox run
# mysqlimport -u avox -r --fields-terminated-by='~' avox avox.txt

# to make this work we need a way of calculating the value of the
# extract

FRUITFILE=/home/avox/tiddlywebs/www.wiki-data.com/templates/fruitmachine.html

DATABASE=avox
DATAUSER=avox
DATATABLE=avox
DATAFILE=avox.txt
DATADIR=/var/lib/mysql/avox
EXTRACTDIR=/home/avox/dataextracts

## calculate date
TODAY=`date +%Y%m%d`

## calculate extract
FULLSTUB="mad_full_extract_$TODAY.txt"
FULLEXTRACTFILE="${1:-$FULLSTUB}"
DELTAEXTRACTFILE="mad_delta_extract_$TODAY.txt"
EXTRACTFILE="nofile$TODAY.txt"

echo $FULLEXTRACTFILE

cd $EXTRACTDIR
EXTRACTFILE=$( (sftp wiki_mad_admin@193.29.79.42:$FULLEXTRACTFILE >/dev/null \
	&& echo -n $FULLEXTRACTFILE)  \
|| (sftp wiki_mad_admin@193.29.79.42:$DELTAEXTRACTFILE >/dev/null \
	&& echo -n $DELTAEXTRACTFILE)  )

# if the file is not there exit
[ -f $EXTRACTDIR/$EXTRACTFILE ]

# set perms otherwise things go funkity
chmod 644 $EXTRACTDIR/$EXTRACTFILE

# If this is a full file, delete all the existing entries.
echo $EXTRACTFILE | grep 'mad_full' && echo "delete from $DATATABLE;" \
    | mysql -u $DATAUSER $DATABASE

cd $DATADIR
cp $EXTRACTDIR/$EXTRACTFILE $DATAFILE

mysqlimport -u $DATAUSER -r --fields-terminated-by='~' $DATABASE $DATAFILE

rm $DATAFILE

COUNTER=$(echo "select count(*) from $DATATABLE;" | \
	mysql --skip-column-names -u $DATAUSER $DATABASE)

# update the fruitmachine automagically
perl -pi -e "s/counter = '\d+'/counter = '$COUNTER'/" $FRUITFILE

echo "Total records: $COUNTER"
