#! /bin/bash

execute_dir(){
	cd ~
	dir_array=$1
	for dir in ${dir_array[@]};do
		echo '----> '${dir}
		mkdir -p ${dir}
		echo '      done'
	done
}

echo '################ start to create folder ###################'


base_dir='tools'
array=("$base_dir/atom"
 "$base_dir/dbeaver"
  "$base_dir/elastic"
	"$base_dir/google"
	"$base_dir/intellij"
	"$base_dir/jdk"
	"$base_dir/jetty"
	"$base_dir/maven"
	"$base_dir/nginx"
	"$base_dir/rabbitmq"
	"$base_dir/script/bin"
	"$base_dir/script/login"
	"$base_dir/skype"
	"$base_dir/sougou"
	"$base_dir/sublime"
	"$base_dir/wps"
	"$base_dir/zookeeper"
	)

execute_dir "${array[*]}"
echo '################ end to create folder ###################'
