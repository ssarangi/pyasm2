python3 setup.py build
rm jitter.so
find . -name jitter.so -exec cp -rfp {} . \;