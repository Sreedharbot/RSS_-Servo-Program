
#required packages for using the program 

PACKAGES=(
    "numpy"
    "RPi.GPIO"
    "spidev"
    )

echo installing packages.......

for PACKAGE in "${PACKAGES[@]}"
do 
    pip install "$PACKAGE"
done

#additional package for runing the application 

sudo apt-get install libopenblas-dev

echo intsalling required packages are done


