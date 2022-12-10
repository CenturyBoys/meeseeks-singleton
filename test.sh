echo '```bash' > tests.md
mutatest -n 40 -s meeseeks/ -t "pytest --cov=meeseeks --cov-report term-missing" >> tests.md
echo '```' >> tests.md