#!/bin/sh

#wget --reject-regex "((.*)\?(.*))" -m -c --content-disposition -np 'https://www.allsides.com'
#wget --reject-regex "((.*)\?(.*))" --accept-regex "(news-source)|(media-bias)" -m -c --content-disposition -np 'https://www.allsides.com/media-bias/media-bias-ratings'
wget --reject-regex "((.*)\?(.*))" --accept-regex "(news-source)|(media-bias)" -m -c --content-disposition 'https://www.allsides.com/media-bias/media-bias-ratings'
