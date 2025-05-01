FRUIT=$1
if [ $FRUIT = APPLE ]; then
  echo "You selected an apple."
elif [ $FRUIT = BANANA ]; then
  echo "You selected a banana."
elif [ $FRUIT = ORANGE ]; then
  echo "You selected an orange."
else
  echo "Unknown fruit."
fi