#This is a run file - which should be used to add things you want your
#container to do when you start it up
#
#If you do not have this then ...
#  docker-compose up ---- simply exists as there is nothing for the container to do.



trap cleanup 1 2 3 6 9 15

cleanup()
{
  echo "Caught Signal ... cleaning up."
  sleep 1s
  echo "Done  ... quitting."
  exit 1
}

# wait forever
cd /esweb
echo "Starting Flask app"
while true
do
  #tail -f /dev/null & wait ${!}
  python app.py
done
