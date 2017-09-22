#! /bin/sh
rm -rf ~/.git_template/hooks
mkdir -p ~/.git_template/hooks
cd ~/.git_template/hooks/

#cd /home/fcw/wfc/test
touch commit-msg
chmod 777 commit-msg

echo "#! /usr/bin/env python
import re
import sys
import os
filePath    = sys.argv[1]
regex  = '^OTMS-\d+(:|\s){1}\D+$'
file       = open(filePath)
content    = file.read(os.path.getsize(filePath))
pattern_result = re.match(regex, content)
if not pattern_result:
    print 'error --- we want the commit msg pattern of Jira ticket number: Jira ticket summary, please check it'
    exit(1)
if len(content) < 10:
    print 'error --- commit msg length should more than 10, please check it'
    exit(1)
file.close()
" >> commit-msg
echo "success create commit-msg"

git config --global init.templatedir ~/.git_template
echo "success update config"

cd ~
file_list=`find . -type d -name '.git'`
for file_path in $file_list
do
 cd $file_path/.. && git init &&  cd ~
 #echo $file_path
done
echo "success git init"

exit 0
