for file in $(find src/enigma/enigmapython -name "*.py" | grep -v XRay |  awk -F'/' '{ for (i=NF-1; i<=NF; i++) printf "%s%s", $i, (i<NF?FS:ORS) }');
do
	echo "[\"$file\", \"github:denismaggior8/micropython-enigma-python/$file\"]," | sed -e 's/\.py/\.mpy/g'
done