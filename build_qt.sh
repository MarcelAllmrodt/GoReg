echo "./res/ressource.qrc"
pyside2-rcc res/ressource.qrc -o ressource_rc.py

cd ui
find . -iname "*.ui" | while read file; do
    echo "$file"
    uic-qt5 -g python -o ../src/"${file%.ui}.py" "$file"
done
