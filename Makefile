.PHONY: install serve build check clean

install:
	bundle install

serve:
	bundle exec jekyll serve --livereload

build:
	bundle exec jekyll build

check:
	python3 scripts/check_site.py

clean:
	bundle exec jekyll clean
