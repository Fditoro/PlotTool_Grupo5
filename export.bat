python -m PyQt5.uic.pyuic "designer/MainWindow.ui" -o "src/ui/MainWindow.py"
python -m PyQt5.uic.pyuic "designer/tf_window.ui" -o "src/ui/tf_window.py"
python -m PyQt5.uic.pyuic "designer/case_window.ui" -o "src/ui/case_window.py"
python -m PyQt5.uic.pyuic "designer/response_window.ui" -o "src/ui/response_window.py"
python -m PyQt5.uic.pyuic "designer/prompt.ui" -o "src/ui/prompt.py"
python -m PyQt5.uic.pyuic "designer/lineGenerator.ui" -o "src/ui/lineGenerator.py"
python -m PyQt5.uic.pyuic "designer/textWindow.ui" -o "src/ui/textWindow.py"
echo "DONE"