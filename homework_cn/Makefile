name = main
questions_name = main_questions
BUILD_DIR = build
QUESTIONS_SRC_DIR = $(BUILD_DIR)/questions_src
QUESTIONS_SCRIPT = scripts/extract_questions.py
LATEX = xelatex
LATEX_FLAGS = -interaction=nonstopmode -output-directory=$(BUILD_DIR)

.PHONY: all questions prepare-questions clean

all:
	mkdir -p $(BUILD_DIR)
	$(LATEX) $(LATEX_FLAGS) $(name).tex
	$(LATEX) $(LATEX_FLAGS) $(name).tex
	cp $(BUILD_DIR)/$(name).pdf .

prepare-questions:
	mkdir -p $(QUESTIONS_SRC_DIR)
	python3 $(QUESTIONS_SCRIPT) --root . --output-dir $(QUESTIONS_SRC_DIR)

questions: prepare-questions
	mkdir -p $(BUILD_DIR)
	$(LATEX) $(LATEX_FLAGS) $(questions_name).tex
	$(LATEX) $(LATEX_FLAGS) $(questions_name).tex
	cp $(BUILD_DIR)/$(questions_name).pdf .

clean:
	rm -f $(BUILD_DIR)/$(name).aux $(BUILD_DIR)/$(name).log $(BUILD_DIR)/$(name).out $(BUILD_DIR)/$(name).toc $(BUILD_DIR)/$(name).synctex.gz
	rm -f $(BUILD_DIR)/$(questions_name).aux $(BUILD_DIR)/$(questions_name).log $(BUILD_DIR)/$(questions_name).out $(BUILD_DIR)/$(questions_name).toc $(BUILD_DIR)/$(questions_name).synctex.gz
	rm -rf $(QUESTIONS_SRC_DIR)
