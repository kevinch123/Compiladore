antlr4 -Dlanguage=Python3 -no-listener -visitor MiGramatica.g4
antlr4 -Dlanguage=Python3 MiGramatica.g4
python test_listener.py
python test_visitor.py

for (i = 0; i < 10; i = i + 1) { i = i + 1; };