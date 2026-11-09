.PHONY: check
check:
	python3 tools/check-methodology.py

# Shared governance check preserves the existing product/methodology corpus.
.PHONY: governance-check
governance-check:
	node tools/warden.mjs --governance
check: governance-check
