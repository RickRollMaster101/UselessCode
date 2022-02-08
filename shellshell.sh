while [ 1 ]
do
    echo " "
    whoami | lolcat
    read -p "$ " cmd
    if [ "$cmd" = "exit" ]; then
        echo "exiting...."
        break
    elif [ "$cmd" = "cls" ]; then
        clear
    else
        $cmd
    fi
done